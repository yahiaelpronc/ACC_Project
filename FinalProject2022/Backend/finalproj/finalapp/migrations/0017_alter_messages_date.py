# Generated by Django 3.2.14 on 2022-07-21 08:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0016_animal_female_state_alter_animal_species_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 21, 10, 31, 54, 71107)),
        ),
    ]
