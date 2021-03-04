# Generated by Django 2.2.7 on 2020-01-08 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0014_auto_20200108_1749'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='latest_history',
            new_name='latest_execution',
        ),
        migrations.AlterField(
            model_name='adhocexecution',
            name='adhoc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='execution', to='ops.AdHoc'),
        ),
        migrations.AlterField(
            model_name='adhocexecution',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='execution', to='ops.Task'),
        ),
        migrations.AlterModelTable(
            name='adhocexecution',
            table='ops_adhoc_execution',
        ),
    ]
