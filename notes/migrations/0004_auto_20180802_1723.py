# Generated by Django 2.0.7 on 2018-08-02 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_note_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
