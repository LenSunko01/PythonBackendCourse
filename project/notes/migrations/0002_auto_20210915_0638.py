# Generated by Django 3.2.7 on 2021-09-15 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='note',
            name='note_name',
            field=models.CharField(default='SOME NAME', max_length=20),
        ),
        migrations.AddField(
            model_name='note',
            name='note_tag',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='note',
            name='note_text',
            field=models.CharField(default='SOME TEXT', max_length=200),
        ),
    ]