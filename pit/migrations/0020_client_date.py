# Generated by Django 2.0.2 on 2018-04-05 11:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pit', '0019_auto_20180403_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]