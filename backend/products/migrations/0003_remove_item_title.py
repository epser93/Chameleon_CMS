# Generated by Django 2.1.15 on 2020-10-30 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_category_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='title',
        ),
    ]
