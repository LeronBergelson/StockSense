# Generated by Django 3.1.7 on 2021-04-07 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StockList',
            fields=[
                ('stock_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('symbol', models.CharField(default='', max_length=6)),
                ('postiveSentimentCount', models.PositiveIntegerField(default=0)),
                ('negativeSentimentCount', models.PositiveIntegerField(default=0)),
                ('value', models.FloatField(default=0.0)),
                ('tweet_id', models.CharField(blank=True, default='', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='WatchList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watchList_id', models.PositiveIntegerField(default=0)),
                ('stockResults', models.ManyToManyField(to='app.StockList')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('watchList', models.ManyToManyField(to='app.WatchList')),
            ],
            options={
                'ordering': ['user'],
            },
        ),
    ]
