# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0004_naturalperson'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nombre', models.CharField(null=True, max_length=10, blank=True)),
                ('apellidos', models.TextField(max_length=60)),
                ('dni', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Karina',
                'verbose_name_plural': 'Karinas',
            },
        ),
    ]
