from django.db import models
from django.urls import reverse

# Create your models here.





class Machine(models.Model):
    """Model definition for Machine."""

    title = models.CharField(verbose_name='название', max_length=255)

    class Meta:
        """Meta definition for Machine."""

        verbose_name = 'Machine'
        verbose_name_plural = 'Machines'

    def __str__(self):
        return f'{self.title}'


class Ctf(models.Model):
    """Model definition for Ctf."""

    title = models.CharField(verbose_name='название', max_length=255)
    description = models.TextField(verbose_name='описание', null=True, blank=True)

    class Meta:
        """Meta definition for Ctf."""

        verbose_name = 'Ctf'
        verbose_name_plural = 'Ctfs'

    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return reverse('show_ctf', kwargs={'id': self.pk})


class Task(models.Model):
    """Model definition for Task."""

    
    title = models.CharField(verbose_name='название', max_length=255)
    description = models.TextField(verbose_name='описание', null=True, blank=True)
    flag = models.CharField(verbose_name='ответ', max_length=255)
    floor = models.SmallIntegerField(verbose_name='этаж')
    
    ctf = models.ForeignKey('tasks.Ctf', on_delete=models.CASCADE, verbose_name='ctf', related_name='tasks')

    class Meta:
        """Meta definition for Task."""

        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return f'{self.title}'


class Answer(models.Model):
    """Model definition for Answer."""

    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='пользователь', related_name='answers')
    task = models.ForeignKey('tasks.Task', on_delete=models.CASCADE, verbose_name='задание', related_name='tasks')
    status = models.BooleanField(verbose_name='статус', default=False)
    
    class Meta:
        """Meta definition for Answer."""

        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __str__(self):
        return f'{self.user} - {self.task}'


