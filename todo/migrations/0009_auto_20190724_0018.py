# Generated by Django 2.2.3 on 2019-07-23 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_post_achivement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='achivement',
            new_name='achievement',
        ),
    ]
