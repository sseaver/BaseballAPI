# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 19:09
from __future__ import unicode_literals
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batting',
            name='playerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Master'),
        ),
        migrations.AlterField(
            model_name='fielding',
            name='playerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Master'),
        ),
        migrations.AlterField(
            model_name='pitching',
            name='playerID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Master'),
        ),
    ]