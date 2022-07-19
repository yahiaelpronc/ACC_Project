# Generated by Django 4.0.5 on 2022-07-19 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0006_locations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='work_hours_end_period',
            field=models.CharField(choices=[('am', 'am'), ('pm', 'pm')], max_length=2),
        ),
        migrations.AlterField(
            model_name='locations',
            name='work_hours_start_period',
            field=models.CharField(choices=[('am', 'am'), ('pm', 'pm')], max_length=2),
        ),
    ]