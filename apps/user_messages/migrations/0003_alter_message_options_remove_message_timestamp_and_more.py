# Generated by Django 4.1.3 on 2023-01-08 19:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_messages', '0002_remove_post_username_delete_comment_delete_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('data_send',), 'verbose_name': ('Сообщение',), 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.RemoveField(
            model_name='message',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='message',
            name='data_send',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
