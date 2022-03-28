# Generated by Django 4.0.3 on 2022-03-28 17:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0005_comment_name_alter_comment_for_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repairorder',
            name='due_back',
            field=models.DateField(blank=True, db_index=True, default=datetime.date(2022, 4, 4), null=True, verbose_name='Due back'),
        ),
    ]
