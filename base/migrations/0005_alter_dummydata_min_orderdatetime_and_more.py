# Generated by Django 4.1 on 2022-12-21 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_dummydata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dummydata',
            name='min_orderdatetime',
            field=models.DateField(max_length=200),
        ),
        migrations.AlterField(
            model_name='dummydata',
            name='week_ending_mon_sun_dt',
            field=models.DateField(max_length=200),
        ),
    ]
