# Generated by Django 3.0.4 on 2020-04-02 20:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_commentpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentpost',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
