# Generated by Django 4.0.3 on 2022-03-26 15:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0002_alter_car_car_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repairorder',
            name='due_back',
            field=models.DateField(blank=True, db_index=True, default=datetime.date(2022, 4, 2), null=True, verbose_name='Due back'),
        ),
    ]
