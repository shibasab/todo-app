# Generated by Django 2.2.3 on 2019-07-12 09:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('detail', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
