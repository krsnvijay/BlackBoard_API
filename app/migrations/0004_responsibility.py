# Generated by Django 2.0 on 2017-12-26 08:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0003_auto_20171226_0718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responsibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsibility_name', models.CharField(help_text='Enter Responsibility Name', max_length=30)),
                ('faculties_responsible', models.ManyToManyField(to='app.Faculty')),
            ],
            options={
                'verbose_name_plural': 'responsibilties',
                'ordering': ['-responsibility_name'],
            },
        ),
    ]