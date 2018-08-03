from django.db import migrations, models

class Migration(migrations.Migration):
  dependencies = [
    {'notes','0003_auto_20180731_2313'}
  ]

  operations = [
    migrations.AlterField(
      model_name='note',
      name='url',
      field=models.URLField(),
    ),
  ]
