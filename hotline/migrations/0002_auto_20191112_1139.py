# Generated by Django 2.2.7 on 2019-11-12 10:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotline', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='postal_code',
            field=models.CharField(blank=True, max_length=5, null=True, validators=[django.core.validators.RegexValidator(message="Postal code must be entered in the format: '99999'.", regex='^\\d{5}$')]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='street',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='technician',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='hotline.Person'),
        ),
    ]
