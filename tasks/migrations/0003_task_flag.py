# Generated by Django 5.1.3 on 2024-11-25 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_user_machine'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='flag',
            field=models.CharField(default=1, max_length=255, verbose_name='ответ'),
            preserve_default=False,
        ),
    ]
