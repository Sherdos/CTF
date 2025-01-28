from django.db.models.signals import post_save
from django.dispatch import receiver
from tasks.models import Answer, Setting
from tasks.mqtt import publish_message
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


@receiver(post_save, sender=Answer)
def send_answer(sender, instance, created, **kwargs):
    setting = Setting.objects.latest('id')
    if instance.task.ctf == setting.active_ctf:
        floor = instance.task.floor
        topic = f"house/{instance.user.machine_id}/floor/{floor}"
        payload = {"action": "off"}

        # Публикация в MQTT
        publish_message(topic, payload)
    if created:
        channel_layer = get_channel_layer()
        ctf_id = instance.task.ctf.id
        first_blood = not Answer.objects.filter(task=instance.task).exclude(id=instance.id).exists()

        # Отправка сообщения через WebSocket
        async_to_sync(channel_layer.group_send)(
            f'ctf_{ctf_id}',
            {
                'type': 'ctf_message',
                'message': {
                    'type': 'first_blood' if first_blood else 'progress',
                    'task_title': instance.task.title,
                    'user': instance.user.username,
                },
            }
        )
