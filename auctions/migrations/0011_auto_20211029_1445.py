# Generated by Django 3.1.4 on 2021-10-29 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auto_20211014_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='bidTime',
        ),
        migrations.AlterField(
            model_name='bid',
            name='ammount',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='listing',
            name='starting_bid',
            field=models.PositiveIntegerField(),
        ),
    ]
