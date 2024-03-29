# Generated by Django 5.0.2 on 2024-03-15 09:53

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0006_alter_lectureaddress_address_detail'),
        ('member', '0003_member_admin_type'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_status',
        ),
        migrations.AddField(
            model_name='order',
            name='member',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='member.member'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('order_status', models.IntegerField(choices=[(0, '진행중'), (-1, '삭제'), (1, '결제완료')], default=0)),
                ('date', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('kit', models.CharField(default='offline', max_length=100)),
                ('quantity', models.IntegerField(default=1)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lecture.lecture')),
            ],
            options={
                'db_table': 'tbl_order_detail',
                'ordering': ['-id'],
            },
        ),
    ]
