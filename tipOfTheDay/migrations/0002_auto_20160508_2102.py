# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipOfTheDay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='title',
            field=models.CharField(help_text=b'The title of the tip. Keep it short.', max_length=255),
        ),
    ]
