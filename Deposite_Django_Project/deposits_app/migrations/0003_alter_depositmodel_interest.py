# Generated by Django 3.2.2 on 2021-05-11 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposits_app', '0002_rename_deposit_depositmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depositmodel',
            name='interest',
            field=models.FloatField(),
        ),
    ]
