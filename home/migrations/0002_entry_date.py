# Generated by Django 5.0 on 2024-01-07 00:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
