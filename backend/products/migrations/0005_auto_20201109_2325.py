# Generated by Django 2.1.15 on 2020-11-09 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20201109_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorydescription',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='description', to='products.Category'),
        ),
    ]
