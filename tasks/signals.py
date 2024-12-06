from django.db.models.signals import post_save
from django.dispatch import receiver
from tasks.models import Answer, Setting
import paramiko


@receiver(post_save, sender=Answer)
def send_answer(sender, instance, created, **kwargs):
    setting = Setting.objects.latest('id')
    if instance.task.ctf == setting.active_ctf:
        hostname = instance.user.machine.hostname
        username = instance.user.machine.username
        password = instance.user.machine.password
        floor = instance.tasks.floor
        remote_script_path = setting.file_name
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            
            ssh_client.connect(hostname=hostname, username=username, password=password)
            print(f"Connected to {hostname}")

            stdin, stdout, stderr = ssh_client.exec_command(f"python3 {remote_script_path} {floor}")
            
            print("Output:")
            print(stdout.read().decode())
            print("Errors:")
            print(stderr.read().decode())
            
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            ssh_client.close()
            print("Connection closed.")