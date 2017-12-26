# Generated by Django 2.0 on 2017-12-26 09:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('choices_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room_choices',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room_choices',
            name='room_name',
            field=models.CharField(help_text='Enter room Name (101,201)', max_length=30),
        ),
    ]
