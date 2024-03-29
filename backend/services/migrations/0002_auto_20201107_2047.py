# Generated by Django 2.1.15 on 2020-11-07 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventdetail',
            name='content',
        ),
        migrations.AddField(
            model_name='event',
            name='content',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='notices',
            name='end_date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='notices',
            name='is_temp',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='notices',
            name='start_date',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
