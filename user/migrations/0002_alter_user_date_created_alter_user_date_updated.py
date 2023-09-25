# Generated by Django 4.2.5 on 2023-09-25 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="date_created",
            field=models.DateTimeField(
                null=True,
                verbose_name=datetime.datetime(
                    2023, 9, 25, 14, 33, 51, 940157, tzinfo=datetime.timezone.utc
                ),
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="date_updated",
            field=models.DateTimeField(
                null=True,
                verbose_name=datetime.datetime(
                    2023, 9, 25, 14, 33, 51, 940171, tzinfo=datetime.timezone.utc
                ),
            ),
        ),
    ]
