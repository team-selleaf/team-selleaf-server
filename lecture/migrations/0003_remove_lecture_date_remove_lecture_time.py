# Generated by Django 5.0.2 on 2024-03-06 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0002_lecturescrap_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='date',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='time',
        ),
    ]
