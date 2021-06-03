# Generated by Django 3.2.3 on 2021-06-03 07:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='title',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 4, 7, 5, 32, 620532, tzinfo=utc), null=True, verbose_name='그룹 시작일'),
        ),
    ]