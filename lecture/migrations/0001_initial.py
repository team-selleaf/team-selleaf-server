# Generated by Django 5.0.2 on 2024-03-05 17:26

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '__first__'),
        ('selleaf', '__first__'),
        ('teacher', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='LectureCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('lecture_category_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tbl_lecture_category',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('lecture_price', models.BigIntegerField(default=0)),
                ('lecture_headcount', models.IntegerField(default=0)),
                ('lecture_title', models.CharField(max_length=100)),
                ('lecture_content', models.CharField(max_length=225)),
                ('lecture_status', models.BooleanField(default=False)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='selleaf.date')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teacher.teacher')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='selleaf.time')),
                ('lecture_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lecture.lecturecategory')),
            ],
            options={
                'db_table': 'tbl_lecture',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('kit_name', models.CharField(max_length=100)),
                ('kit_content', models.CharField(max_length=225)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lecture.lecture')),
            ],
            options={
                'db_table': 'tbl_kit',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='LecturePlaceFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('file_url', models.ImageField(upload_to='file/%Y/%m/%d')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lecture.lecture')),
            ],
            options={
                'db_table': 'tbl_lecture_place_file',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='LecturePlant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('plant_name', models.CharField(max_length=50)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lecture.lecture')),
            ],
            options={
                'db_table': 'tbl_lecture_plant',
            },
        ),
        migrations.CreateModel(
            name='LectureProductFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('file_url', models.ImageField(upload_to='file/%Y/%m/%d')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lecture.lecture')),
            ],
            options={
                'db_table': 'tbl_lecture_product_file',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='LectureReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('review_title', models.CharField(max_length=100)),
                ('review_content', models.CharField(max_length=225)),
                ('review_rating', models.IntegerField(default=0)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lecture.lecture')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='member.member')),
            ],
            options={
                'db_table': 'tbl_lecture_review',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='LectureScrap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lecture.lecture')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='member.member')),
            ],
            options={
                'db_table': 'tbl_lecture_scrap',
            },
        ),
    ]
