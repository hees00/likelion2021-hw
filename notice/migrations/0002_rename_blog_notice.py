# Generated by Django 3.2.3 on 2021-05-15 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='Notice',
        ),
    ]