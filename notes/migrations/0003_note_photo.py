# Generated by Django 2.1 on 2018-08-02 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_personalnote'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='photo',
            field=models.ImageField(default={None}, upload_to='notes'),
            preserve_default=False,
        ),
    ]