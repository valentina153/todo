# Generated by Django 3.2 on 2021-05-16 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDoApp', '0002_auto_20210516_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo1',
            name='datumObaveze',
            field=models.DateField(blank=True, null=True),
        ),
    ]