# Generated by Django 3.0.5 on 2020-04-30 17:51

from django.db import migrations, models


class Migration(migrations.Migration):



    operations = [
        migrations.AddField(
            model_name='pagelink',
            name='items',
            field=models.ManyToManyField(to='book.Item'),
        ),
    ]
