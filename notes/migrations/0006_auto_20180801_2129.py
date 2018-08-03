# Generated by Django 2.0.7 on 2018-08-01 21:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_personalnote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='note',
            name='last_modified',
        ),
        migrations.RemoveField(
            model_name='note',
            name='url',
        ),
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
