# Generated by Django 4.1.3 on 2022-11-13 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_timestable_reception_alter_receptiontime_reception_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timestable',
            name='reception',
        ),
    ]
