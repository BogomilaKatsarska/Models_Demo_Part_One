# Generated by Django 3.2.16 on 2022-10-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_employee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.IntegerField(default=-1),
        ),
    ]
