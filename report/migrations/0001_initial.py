# Generated by Django 5.0.2 on 2024-03-05 09:31

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('report_category_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'tbl_report_category',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('report_name', models.CharField(max_length=255)),
                ('report_status', models.BooleanField(default=True)),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='member.member')),
                ('report_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='report.reportcategory')),
            ],
            options={
                'db_table': 'tbl_report',
                'ordering': ['-id'],
            },
        ),
    ]
