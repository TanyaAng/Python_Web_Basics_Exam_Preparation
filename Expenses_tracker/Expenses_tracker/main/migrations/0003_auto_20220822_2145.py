# Generated by Django 3.2.15 on 2022-08-22 18:45

import Expenses_tracker.main.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220822_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), Expenses_tracker.main.validators.only_letters_validator]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), Expenses_tracker.main.validators.only_letters_validator]),
        ),
    ]