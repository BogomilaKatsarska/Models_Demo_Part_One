# Generated by Django 3.2.16 on 2022-10-26 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_auto_20221026_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='level',
            field=models.CharField(choices=[('Senior', 'Senior'), ('Junior', 'Junior'), ('Regular', 'Regular')], max_length=50, verbose_name='Seniority Level'),
        ),
    ]