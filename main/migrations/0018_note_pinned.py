# Generated by Django 3.0.5 on 2021-06-04 17:24

from django.db import migrations, models


class Migration(migrations.Migration):


    operations = [
        migrations.AddField(
            model_name='note',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
    ]
