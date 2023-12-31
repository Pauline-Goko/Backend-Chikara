# Generated by Django 4.2.5 on 2023-09-26 05:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0009_alter_user_date_created_alter_user_date_updated"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="date_created",
            field=models.DateTimeField(
                null=True,
                verbose_name=datetime.datetime(
                    2023, 9, 26, 5, 52, 31, 352203, tzinfo=datetime.timezone.utc
                ),
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="date_updated",
            field=models.DateTimeField(
                null=True,
                verbose_name=datetime.datetime(
                    2023, 9, 26, 5, 52, 31, 352218, tzinfo=datetime.timezone.utc
                ),
            ),
        ),
    ]
