# Generated by Django 5.0.2 on 2024-03-06 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selleaf', '0002_date_lecture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='time',
            field=models.CharField(max_length=100),
        ),
    ]
