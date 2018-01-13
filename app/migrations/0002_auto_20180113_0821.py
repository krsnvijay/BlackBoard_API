# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-13 02:51
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsibility',
            name='faculties_responsible',
            field=models.ManyToManyField(related_name='responsibilities', to='app.Faculty'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='hour',
            field=models.CharField(help_text='Choose hour Of The Class', max_length=1, validators=[
                django.core.validators.RegexValidator('^[1-8]', 'Only 1-8 are allowed.')]),
        ),
    ]