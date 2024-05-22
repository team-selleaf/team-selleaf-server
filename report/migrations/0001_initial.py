# Generated by Django 5.0.2 on 2024-05-22 17:04

import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("knowhow", "0001_initial"),
        ("lecture", "0001_initial"),
        ("member", "0001_initial"),
        ("post", "0001_initial"),
        ("trade", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="KnowhowReplyReport",
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
                ("report_content", models.CharField(max_length=50)),
                ("report_status", models.BooleanField(default=True)),
                (
                    "knowhow_reply",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="knowhow.knowhowreply",
                    ),
                ),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="member.member"
                    ),
                ),
            ],
            options={
                "db_table": "tbl_knowhow_reply_report",
                "ordering": ["-id"],
            },
            managers=[
                ("object", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="KnowhowReport",
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
                ("report_content", models.CharField(max_length=50)),
                ("report_status", models.BooleanField(default=True)),
                (
                    "knowhow",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="knowhow.knowhow",
                    ),
                ),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="member.member"
                    ),
                ),
            ],
            options={
                "db_table": "tbl_knowhow_report",
                "ordering": ["-id"],
            },
            managers=[
                ("object", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="LectureReport",
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
                ("report_content", models.CharField(max_length=50)),
                ("report_status", models.BooleanField(default=True)),
                (
                    "lecture",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="lecture.lecture",
                    ),
                ),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="member.member"
                    ),
                ),
            ],
            options={
                "db_table": "tbl_lecture_report",
                "ordering": ["-id"],
            },
            managers=[
                ("object", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="PostReplyReport",
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
                ("report_content", models.CharField(max_length=50)),
                ("report_status", models.BooleanField(default=True)),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="member.member"
                    ),
                ),
                (
                    "post_reply",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="post.postreply"
                    ),
                ),
            ],
            options={
                "db_table": "tbl_post_reply_report",
                "ordering": ["-id"],
            },
            managers=[
                ("object", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="PostReport",
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
                ("report_content", models.CharField(max_length=50)),
                ("report_status", models.BooleanField(default=True)),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="member.member"
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="post.post"
                    ),
                ),
            ],
            options={
                "db_table": "tbl_post_report",
                "ordering": ["-id"],
            },
            managers=[
                ("object", django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name="TradeReport",
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
                ("report_content", models.CharField(max_length=50)),
                ("report_status", models.BooleanField(default=True)),
                (
                    "member",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="member.member"
                    ),
                ),
                (
                    "trade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="trade.trade"
                    ),
                ),
            ],
            options={
                "db_table": "tbl_trade_report",
                "ordering": ["-id"],
            },
            managers=[
                ("object", django.db.models.manager.Manager()),
            ],
        ),
    ]
