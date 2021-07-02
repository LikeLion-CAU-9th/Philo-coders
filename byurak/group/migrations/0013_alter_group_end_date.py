# Generated by Django 3.2.3 on 2021-07-02 04:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0012_alter_group_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='end_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 3, 4, 42, 23, 68018, tzinfo=utc), null=True, verbose_name='그룹 마침일'),
        ),
    ]
