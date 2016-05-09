# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_achievments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Achievments',
        ),
    ]
