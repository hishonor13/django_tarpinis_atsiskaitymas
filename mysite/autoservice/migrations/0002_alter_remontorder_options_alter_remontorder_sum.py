# Generated by Django 4.0.3 on 2022-03-24 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='remontorder',
            options={'ordering': ['car'], 'verbose_name': 'Repair order', 'verbose_name_plural': 'Repair orders'},
        ),
        migrations.AlterField(
            model_name='remontorder',
            name='sum',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Sum'),
        ),
    ]