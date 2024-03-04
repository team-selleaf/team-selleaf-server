# Generated by Django 5.0.2 on 2024-03-04 16:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0001_initial'),
        ('lecture', '0002_alter_lectureplacefile_table'),
        ('selleaf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='date',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='selleaf.date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='apply',
            name='kit',
            field=models.ForeignKey(default='offline', on_delete=django.db.models.deletion.PROTECT, to='lecture.kit'),
        ),
        migrations.AddField(
            model_name='apply',
            name='time',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='selleaf.time'),
            preserve_default=False,
        ),
    ]