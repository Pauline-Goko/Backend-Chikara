# Generated by Django 4.2.1 on 2023-09-23 15:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0005_alter_user_date_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="date_created",
            field=models.DateTimeField(
                null=True,
                verbose_name=datetime.datetime(
                    2023, 9, 23, 15, 23, 9, 153633, tzinfo=datetime.timezone.utc
                ),
            ),
        ),
    ]