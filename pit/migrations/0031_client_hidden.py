# Generated by Django 2.0.2 on 2018-05-22 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pit', '0030_auto_20180520_0214'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='hidden',
            field=models.BooleanField(default=True),
        ),
    ]
