# Generated by Django 2.0.2 on 2018-03-29 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pit', '0014_auto_20180319_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='hidden',
            field=models.BooleanField(default=True),
        ),
    ]
