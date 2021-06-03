# Generated by Django 3.2.3 on 2021-06-02 12:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', models.CharField(blank=True, max_length=255, null=True)),
                ('mento_users', models.CharField(blank=True, max_length=255, null=True)),
                ('mentee_users', models.CharField(blank=True, max_length=255, null=True)),
                ('limited_user_numbers', models.IntegerField(blank=True, default=1, null=True)),
                ('status', models.CharField(choices=[('complete', 'COMPLETE'), ('recruitment', 'RECRUITMENT'), ('overdue', 'OVERDUE')], default='recruitment', help_text='그룹 상태', max_length=31)),
                ('start_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='그룹 시작일')),
                ('end_date', models.DateTimeField(blank=True, default=datetime.datetime(2021, 6, 3, 12, 18, 17, 450150, tzinfo=utc), null=True, verbose_name='그룹 시작일')),
                ('keyword', models.CharField(blank=True, max_length=63, null=True)),
                ('short_description', models.CharField(blank=True, max_length=255, null=True)),
                ('representive', models.ForeignKey(help_text='유저', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupNotice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=127, null=True)),
                ('body', models.TextField(help_text='그룹 공지 글')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('group', models.ForeignKey(help_text='그룹', on_delete=django.db.models.deletion.CASCADE, to='group.group')),
                ('user', models.ForeignKey(help_text='유저', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupCommunityPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=127, null=True)),
                ('body', models.TextField(help_text='그룹 공지 글')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('group', models.ForeignKey(help_text='그룹', on_delete=django.db.models.deletion.CASCADE, to='group.group')),
                ('user', models.ForeignKey(help_text='유저', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
