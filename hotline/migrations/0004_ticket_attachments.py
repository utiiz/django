# Generated by Django 2.2.7 on 2019-12-23 15:07

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotline', '0003_auto_20191114_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='attachments',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1024), blank=True, null=True, size=None),
        ),
    ]