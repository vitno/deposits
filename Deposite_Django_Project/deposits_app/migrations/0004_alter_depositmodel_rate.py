# Generated by Django 3.2.2 on 2021-05-11 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposits_app', '0003_alter_depositmodel_interest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depositmodel',
            name='rate',
            field=models.FloatField(),
        ),
    ]
