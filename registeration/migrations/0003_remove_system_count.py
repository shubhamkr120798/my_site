# Generated by Django 2.2.11 on 2020-03-28 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registeration', '0002_auto_20200328_0725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='system',
            name='count',
        ),
    ]