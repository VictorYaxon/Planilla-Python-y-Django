# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-06 02:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20161103_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planillagenerar',
            name='bonificacion',
        ),
        migrations.RemoveField(
            model_name='planillagenerar',
            name='empleado',
        ),
        migrations.RemoveField(
            model_name='planillagenerar',
            name='retencion',
        ),
        migrations.RemoveField(
            model_name='planillagenerar',
            name='salario',
        ),
        migrations.DeleteModel(
            name='PlanillaGenerar',
        ),
    ]
