# Generated by Django 3.0.2 on 2020-01-31 01:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forex_data', '0006_auto_20200130_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 31, 1, 31, 57, 207676, tzinfo=utc)),
        ),
    ]
