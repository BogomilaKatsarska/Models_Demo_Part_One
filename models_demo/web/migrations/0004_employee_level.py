# Generated by Django 3.2.16 on 2022-10-26 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_employee_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='level',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
