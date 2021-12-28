# Generated by Django 3.2.10 on 2021-12-28 20:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20211229_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 28, 20, 9, 30, 296085, tzinfo=utc), verbose_name='Created on'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='image',
            name='updated_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 28, 20, 9, 30, 296085, tzinfo=utc), verbose_name='Updated on'),
        ),
    ]
