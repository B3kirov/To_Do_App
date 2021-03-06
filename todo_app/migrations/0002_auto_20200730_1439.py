# Generated by Django 3.0.8 on 2020-07-30 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='todos',
            name='finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='todos',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
