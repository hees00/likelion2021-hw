# Generated by Django 3.1.7 on 2021-05-23 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_rename_blog_notice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='studentID',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='writer',
        ),
        migrations.AlterField(
            model_name='notice',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
