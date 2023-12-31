# Generated by Django 4.2.5 on 2023-09-28 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='number_plate',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='chassis_number',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_model',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='engine_type',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
