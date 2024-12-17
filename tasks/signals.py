from django.db.models.signals import post_save
from django.dispatch import receiver
from tasks.models import Answer, Setting
import paramiko

from tasks.mqtt import publish_message


@receiver(post_save, sender=Answer)
def send_answer(sender, instance, created, **kwargs):
    setting = Setting.objects.latest('id')
    if instance.task.ctf == setting.active_ctf:
        floor = instance.task.floor
        topic = f"house/{instance.user.machine_id}/floor/{floor}"
        payload = {"action": "off"}

        # Публикация в MQTT
        publish_message(topic, payload)