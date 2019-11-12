# Generated by Django 2.2.7 on 2019-11-10 17:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotline', '0009_auto_20191110_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='postal_code',
            field=models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(message="Postal code must be entered in the format: '99999'.", regex='^\\d{5}$')]),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tickets', to='hotline.Customer'),
        ),
    ]
