# Generated by Django 5.0.2 on 2024-03-10 20:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_postlike_status_postreplylike_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcategory',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='post.post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postscrap',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
