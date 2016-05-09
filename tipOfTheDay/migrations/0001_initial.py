# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'The title of the tip. Keep it short.', max_length=30)),
                ('level', models.PositiveSmallIntegerField(help_text=b'This is how familiar with windows the user should be when seeing this tip. Please note that this is <em> Not </em> how familiar the user is with NVDA.', choices=[(1, b'beginner'), (2, b'intermediate'), (4, b'advanced'), (3, b'beginner and intermediate'), (6, b'intermediate and advanced'), (7, b'Beginner, Intermediate, and Advanced')])),
                ('text', models.TextField(help_text=b'Write the tip here.')),
            ],
        ),
    ]
