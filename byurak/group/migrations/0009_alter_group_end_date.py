# Generated by Django 3.2.3 on 2021-06-28 11:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0008_alter_group_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 29, 11, 6, 34, 995885, tzinfo=utc), null=True, verbose_name='그룹 마침일'),
        ),
    ]