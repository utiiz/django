# Generated by Django 2.2.7 on 2019-11-10 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotline', '0005_remove_person_tickets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='user',
        ),
        migrations.AddField(
            model_name='ticket',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_ticket_set', to='hotline.Person'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='technician',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='technician_ticket_set', to='hotline.Person'),
        ),
    ]
