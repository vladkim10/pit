# Generated by Django 2.0.2 on 2018-04-06 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pit', '0025_auto_20180406_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_type',
            field=models.CharField(default='', max_length=100),
        ),
    ]
