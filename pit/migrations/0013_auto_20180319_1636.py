# Generated by Django 2.0.2 on 2018-03-19 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pit', '0012_auto_20180319_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='url1',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='dog',
            name='url2',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
