# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_auto_20150706_2020'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='software_list',
            options={'verbose_name': 'software', 'verbose_name_plural': 'pieces of software'},
        ),
        migrations.RenameField(
            model_name='software_list',
            old_name='discription',
            new_name='description',
        ),
    ]
