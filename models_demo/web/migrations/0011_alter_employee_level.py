# Generated by Django 3.2.16 on 2022-10-26 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_alter_employee_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='level',
            field=models.CharField(choices=[('Senior', 'Senior'), ('Junior', 'Junior'), ('Regular', 'Regular')], max_length=7),
        ),
    ]
