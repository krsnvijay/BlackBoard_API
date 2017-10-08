# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 05:59
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_id', models.CharField(editable=False, help_text='Enter Class ID eg.CSE-2-F', max_length=30, primary_key=True, serialize=False)),
                ('location', models.CharField(choices=[('ADMIN', (('ADMIN-101', '101'), ('ADMIN-102', '102'), ('ADMIN-103', '103'))), ('B.M.S', (('B.M.S-101', '101'), ('B.M.S-102', '102'), ('B.M.S-103', '103'))), ('BLOCK-III', (('BLOCK-III-101', '101'), ('BLOCK-III-102', '102'), ('BLOCK-III-103', '103')))], help_text='Choose Class Location', max_length=30)),
                ('dept', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('IT', 'IT'), ('EEE', 'EEE'), ('CIVIL', 'CIVIL'), ('MECH', 'MECH')], help_text='Choose Department of the Class', max_length=5)),
                ('year', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], help_text='Choose Year Of The Class', max_length=1)),
                ('section', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], help_text='Choose Section Of The Class', max_length=1)),
            ],
            options={
                'verbose_name_plural': 'classes',
                'ordering': ['-class_id'],
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('faculty_id', models.CharField(help_text="Enter Faculty's College ID Number", max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text="Enter Faculty's Name", max_length=30)),
                ('email', models.EmailField(help_text="Enter Faculty's Email", max_length=50)),
                ('password', models.CharField(default=123456, help_text="Enter Faculty's Password", max_length=30)),
                ('phone', models.CharField(help_text="Enter Faculty's Phone", max_length=10)),
                ('dept', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('IT', 'IT'), ('EEE', 'EEE'), ('CIVIL', 'CIVIL'), ('MECH', 'MECH')], help_text="Choose Faculty's Dept", max_length=5)),
                ('faculty_type', models.CharField(choices=[('DEAN', 'DEAN'), ('HOD', 'HOD'), ('PROFESSOR', 'PROFESSOR')], help_text="Choose Faculty's Designation", max_length=100)),
                ('incharge_of', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='of_class', to='app.Class')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'faculties',
                'ordering': ['-faculty_id'],
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subj_code', models.CharField(help_text='Enter Subjcode', max_length=10)),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], help_text='Choose The Day', max_length=10)),
                ('hour', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], help_text='Choose Section Of The Class', max_length=1)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_schedule', to='app.Class')),
                ('faculty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faculty_schedule', to='app.Faculty')),
            ],
            options={
                'verbose_name_plural': 'schedules',
                'ordering': ['-faculty_id'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='class',
            unique_together=set([('class_id', 'location', 'dept', 'year', 'section')]),
        ),
        migrations.AlterUniqueTogether(
            name='schedule',
            unique_together=set([('class_id', 'subj_code', 'day', 'hour')]),
        ),
    ]
