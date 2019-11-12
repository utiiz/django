# Generated by Django 2.2.7 on 2019-11-12 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotline', '0003_auto_20191112_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='hotline.Customer'),
        ),
        migrations.AlterField(
            model_name='person',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='hotline.Profile'),
        ),
    ]
