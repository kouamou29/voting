# Generated by Django 4.2.1 on 2023-05-08 06:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_mility_party'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voting',
            name='date_create',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='voting',
            name='number_voting',
            field=models.IntegerField(default=0),
        ),
    ]
