# Generated by Django 3.1.7 on 2021-04-07 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210407_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='stockResults',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='stockResults',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.PROTECT, to='app.stocklist'),
        ),
    ]
