# Generated by Django 3.2.16 on 2022-10-26 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_nullblankdemo'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_full_time',
            field=models.BooleanField(null=True),
        ),
    ]
