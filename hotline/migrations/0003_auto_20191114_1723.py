# Generated by Django 2.2.7 on 2019-11-14 16:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotline', '0002_auto_20191113_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='customers',
        ),
        migrations.AddField(
            model_name='customer',
            name='persons',
            field=models.ManyToManyField(related_name='customers', to='hotline.Person'),
        ),
        migrations.AlterField(
            model_name='person',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
