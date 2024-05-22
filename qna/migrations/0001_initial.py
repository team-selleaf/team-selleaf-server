# Generated by Django 5.0.2 on 2024-05-22 16:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="QnA",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                (
                    "updated_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("qna_title", models.CharField(max_length=255)),
                ("qna_content", models.CharField(max_length=255)),
                ("qna_status", models.BooleanField(default=True)),
            ],
            options={
                "db_table": "tbl_qna",
                "ordering": ["-id"],
            },
        ),
    ]
