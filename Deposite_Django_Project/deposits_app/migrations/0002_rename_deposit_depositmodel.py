# Generated by Django 3.2.2 on 2021-05-11 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deposits_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Deposit',
            new_name='DepositModel',
        ),
    ]
