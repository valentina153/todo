# Generated by Django 3.2 on 2021-05-16 11:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('toDoApp', '0003_alter_todo1_datumobaveze'),
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naslov', models.CharField(max_length=100)),
                ('opis', models.TextField(blank=True)),
                ('važno', models.BooleanField(default=False)),
                ('datumZavrsetka', models.DateTimeField(blank=True, null=True)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='todo1',
        ),
    ]
