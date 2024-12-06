import os
from django.db import models
from django.urls import reverse

# Create your models here.


class Setting(models.Model):
    
    file_name = models.CharField(max_length=255)
    active_ctf = models.ForeignKey('tasks.Ctf', on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
        """Meta definition for Machine."""

        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'

    def __str__(self):
        return f'Setting'

class Machine(models.Model):
    """Model definition for Machine."""

    title = models.CharField(max_length=255)
    hostname = models.CharField( max_length=255)
    password = models.CharField( max_length=255)
    username = models.CharField( max_length=255)

    class Meta:
        """Meta definition for Machine."""

        verbose_name = 'Machine'
        verbose_name_plural = 'Machines'

    def __str__(self):
        return f'{self.title}'


class Ctf(models.Model):
    """Model definition for Ctf."""

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        """Meta definition for Ctf."""

        verbose_name = 'Ctf'
        verbose_name_plural = 'Ctfs'

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse('show_ctf', kwargs={'id': self.pk})



def get_upload_to(instance, filename):
    folder_name = instance.title.replace(' ', '_') 
    return os.path.join('tasks', folder_name, filename)
    
class Task(models.Model):
    """Model definition for Task."""
    
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    flag = models.CharField(max_length=255)
    floor = models.SmallIntegerField()
    file = models.FileField(upload_to=get_upload_to, null=True, blank=True)
    
    ctf = models.ForeignKey('tasks.Ctf', on_delete=models.CASCADE, verbose_name='ctf', related_name='tasks')

    class Meta:
        """Meta definition for Task."""

        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return f'{self.title}'


class Answer(models.Model):
    """Model definition for Answer."""

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='answers')
    task = models.ForeignKey('tasks.Task', on_delete=models.CASCADE, related_name='tasks')
    status = models.BooleanField(verbose_name='статус', default=False)
    
    class Meta:
        """Meta definition for Answer."""

        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __str__(self):
        return f'{self.user} - {self.task}'


