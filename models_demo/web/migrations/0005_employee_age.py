# Generated by Django 3.2.16 on 2022-10-26 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_employee_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='age',
            field=models.IntegerField(default=19),
            preserve_default=False,
        ),
    ]
