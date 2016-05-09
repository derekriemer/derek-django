# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipOfTheDay', '0003_tip_weight'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tip',
            options={'ordering': ['weight', 'pk']},
        ),
        migrations.AlterField(
            model_name='tip',
            name='weight',
            field=models.PositiveSmallIntegerField(help_text=b'the weight of the field. Tinkering with this causes this tip to appear earlier in the list. lowering the weight floats it to the top, while adding weight makes it sink down in the list.'),
        ),
    ]
