# Generated by Django 4.2.1 on 2023-05-05 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voting',
            name='voting_user',
        ),
    ]
