# Generated by Django 2.2 on 2021-09-21 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goat_app', '0013_goatdb_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='bet',
        ),
        migrations.RemoveField(
            model_name='user',
            name='vote',
        ),
    ]