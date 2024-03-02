# Generated by Django 5.0.2 on 2024-03-01 22:33

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lecture', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('cart_status', models.IntegerField(choices=[(0, '결제중'), (1, '결제완료'), (-1, '결제취소'), (-2, '삭제')], default=0)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='member.member')),
            ],
            options={
                'db_table': 'tbl_cart',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='CartDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('quantity', models.IntegerField(default=0)),
                ('cart_detail_status', models.IntegerField(choices=[(0, '게시중'), (-1, '상품 삭제'), (1, '결제 완료')], default=0)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cart.cart')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lecture.lecture')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]