# Generated by Django 4.2.1 on 2023-05-05 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_voting_parti_politi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voting',
            old_name='parti_politi',
            new_name='parti',
        ),
    ]
