# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateTimeField(verbose_name='дата и время (UTC) получения данных о MODIS')),
                ('confidence', models.DecimalField(verbose_name='достоверность (0-100%)', decimal_places=0, max_digits=3)),
                ('frp', models.DecimalField(verbose_name='мощность пожара', decimal_places=1, max_digits=5)),
                ('brightness21', models.DecimalField(verbose_name='температура по каналу 21/22 (в Кельвинах)', decimal_places=1, max_digits=4)),
                ('brightness31', models.DecimalField(verbose_name='температура по каналу 31 (в Кельвинах)', decimal_places=1, max_digits=4)),
                ('scan', models.DecimalField(verbose_name='размер пиксела в направлении сканирования', decimal_places=1, max_digits=2)),
                ('track', models.DecimalField(verbose_name='размер пиксела в направлении траектории', decimal_places=1, max_digits=2)),
                ('version', models.DecimalField(verbose_name='версия', decimal_places=1, max_digits=2)),
                ('geometry', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'verbose_name': 'MODIS данные о пожаре',
                'verbose_name_plural': 'MODIS данные о пожарах',
            },
        ),
        migrations.CreateModel(
            name='Satellite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('satellite', models.CharField(verbose_name='спутник', max_length=5, unique=True)),
                ('short_satellite_name', models.CharField(verbose_name='спутник сокращенно', max_length=1, unique=True)),
            ],
            options={
                'verbose_name': 'Спутник',
                'verbose_name_plural': 'Спутники',
            },
        ),
        migrations.AddField(
            model_name='fire',
            name='satellite',
            field=models.ForeignKey(to='fires.Satellite'),
        ),
    ]
