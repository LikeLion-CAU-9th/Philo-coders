# Generated by Django 3.2.3 on 2021-06-26 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210625_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('service_provider', 'SERVICE_PROVIDER'), ('default_user', 'default_user')], default='default_user', help_text='유저 타입', max_length=20),
        ),
    ]
