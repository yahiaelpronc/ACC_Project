# Generated by Django 4.0.5 on 2022-07-21 05:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0014_alter_messages_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animalName', models.CharField(max_length=30, unique=True)),
                ('ownerUsername', models.CharField(max_length=30)),
                ('weight', models.IntegerField()),
                ('b_date', models.DateField(max_length=20)),
                ('gender', models.CharField(choices=[('m', 'm'), ('f', 'f')], max_length=30)),
                ('species', models.CharField(blank=True, choices=[('immature', 'immature'), ('mature&married', 'mature&married'), ('pregnant ', 'pregnant'), ('lactating', 'lactating')], max_length=30, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='messages',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 21, 7, 10, 40, 299650)),
        ),
    ]