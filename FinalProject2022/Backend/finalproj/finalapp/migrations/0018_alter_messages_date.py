<<<<<<< HEAD
# Generated by Django 3.2.14 on 2022-07-21 13:27
=======
# Generated by Django 4.0.6 on 2022-07-21 10:53
>>>>>>> 6474e54db4d9b2ac29d43dcaaab25386621dfc76

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0017_alter_messages_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='date',
<<<<<<< HEAD
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 21, 15, 27, 17, 128500)),
=======
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 21, 12, 53, 46, 439188)),
>>>>>>> 6474e54db4d9b2ac29d43dcaaab25386621dfc76
        ),
    ]
