# Generated by Django 4.0.6 on 2022-07-17 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myuser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30, null=True)),
                ('mobile', models.CharField(max_length=20, null=True)),
                ('b_date', models.DateField(max_length=20, null=True)),
                ('active_status', models.BooleanField(default=False)),
                ('face_link', models.URLField(null=True)),
                ('active_link', models.URLField(null=True)),
                ('profile_pic', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]