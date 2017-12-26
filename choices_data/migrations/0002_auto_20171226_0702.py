# Generated by Django 2.0 on 2017-12-26 07:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('choices_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject_choices',
            options={'ordering': ['-subject_code'], 'verbose_name_plural': 'Subject Choices'},
        ),
        migrations.AlterField(
            model_name='dept_choices',
            name='dept_code',
            field=models.CharField(help_text='Enter Dept (EEE,CSE..)', max_length=10, primary_key=True,
                                   serialize=False),
        ),
        migrations.AlterField(
            model_name='faculty_choices',
            name='faculty_type',
            field=models.CharField(help_text='Enter Faculty Type (HOD,DEAN,Asst.Prof)', max_length=30, primary_key=True,
                                   serialize=False),
        ),
        migrations.AlterField(
            model_name='room_choices',
            name='room_name',
            field=models.CharField(help_text='Enter room Name (101,201)', max_length=30, primary_key=True,
                                   serialize=False),
        ),
        migrations.AlterField(
            model_name='subject_choices',
            name='subject_code',
            field=models.CharField(help_text='Enter Subject Code (15IT301)', max_length=30, primary_key=True,
                                   serialize=False),
        ),
    ]