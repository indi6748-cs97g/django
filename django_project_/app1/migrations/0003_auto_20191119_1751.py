# Generated by Django 2.2.7 on 2019-11-19 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20191119_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calate',
            name='a',
            field=models.FloatField(max_length=10),
        ),
        migrations.AlterField(
            model_name='calate',
            name='result',
            field=models.FloatField(max_length=10),
        ),
    ]