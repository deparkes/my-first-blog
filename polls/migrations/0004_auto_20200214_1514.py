# Generated by Django 2.2.6 on 2020-02-14 15:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20200214_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='vote_datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 15, 14, 41, 923489, tzinfo=utc), verbose_name='time voted'),
        ),
    ]