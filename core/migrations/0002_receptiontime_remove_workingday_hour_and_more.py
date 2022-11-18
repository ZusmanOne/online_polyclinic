# Generated by Django 4.1.3 on 2022-11-13 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceptionTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reception', models.TimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='workingday',
            name='hour',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='time_table',
        ),
        migrations.RenameModel(
            old_name='WorkingHour',
            new_name='TimesTable',
        ),
        migrations.DeleteModel(
            name='TimeTable',
        ),
        migrations.DeleteModel(
            name='WorkingDay',
        ),
        migrations.AddField(
            model_name='receptiontime',
            name='time_table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reception_time', to='core.timestable'),
        ),
    ]