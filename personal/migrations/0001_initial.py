# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Software_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('discription', models.TextField()),
                ('source_code_download', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_released', models.DateField()),
                ('major_version_number', models.PositiveIntegerField()),
                ('minor_version_number', models.PositiveIntegerField()),
                ('sub_version_number', models.PositiveIntegerField()),
                ('stable_release', models.BinaryField()),
                ('download', models.URLField()),
                ('software', models.ForeignKey(to='personal.Software_list')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
