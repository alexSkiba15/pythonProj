# Generated by Django 2.2.7 on 2019-11-14 21:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
