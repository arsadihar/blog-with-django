# Generated by Django 3.1.5 on 2021-01-18 15:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210118_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
