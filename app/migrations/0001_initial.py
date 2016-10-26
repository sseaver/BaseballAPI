# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerID', models.CharField(max_length=10)),
                ('yearID', models.IntegerField()),
                ('stint', models.IntegerField()),
                ('teamID', models.CharField(max_length=5)),
                ('lgID', models.CharField(max_length=5)),
                ('G', models.IntegerField()),
                ('AB', models.IntegerField()),
                ('R', models.IntegerField()),
                ('H', models.IntegerField()),
                ('doubles', models.IntegerField()),
                ('triples', models.IntegerField()),
                ('HR', models.IntegerField()),
                ('RBI', models.IntegerField()),
                ('SB', models.IntegerField()),
                ('CS', models.IntegerField()),
                ('BB', models.IntegerField()),
                ('SO', models.IntegerField()),
                ('IBB', models.IntegerField()),
                ('HBP', models.IntegerField()),
                ('SH', models.IntegerField()),
                ('SF', models.IntegerField()),
                ('GIDP', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Fielding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerID', models.CharField(max_length=10)),
                ('yearID', models.IntegerField()),
                ('stint', models.IntegerField()),
                ('teamID', models.CharField(max_length=10)),
                ('lgID', models.CharField(max_length=10)),
                ('POS', models.IntegerField()),
                ('G', models.IntegerField()),
                ('GS', models.IntegerField()),
                ('InnOuts', models.IntegerField()),
                ('PO', models.IntegerField()),
                ('A', models.IntegerField()),
                ('E', models.IntegerField()),
                ('DP', models.IntegerField()),
                ('PB', models.IntegerField()),
                ('WP', models.IntegerField()),
                ('SB', models.IntegerField()),
                ('CS', models.IntegerField()),
                ('ZR', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerID', models.CharField(max_length=10)),
                ('birthYear', models.IntegerField()),
                ('birthMonth', models.IntegerField()),
                ('birthDay', models.IntegerField()),
                ('birthCountry', models.CharField(max_length=50)),
                ('birthState', models.CharField(max_length=5)),
                ('birthCity', models.CharField(max_length=50)),
                ('deathYear', models.IntegerField()),
                ('deathMonth', models.IntegerField()),
                ('deathDay', models.IntegerField()),
                ('deathCountry', models.CharField(max_length=50)),
                ('deathState', models.CharField(max_length=5)),
                ('deathCity', models.CharField(max_length=50)),
                ('nameFirst', models.CharField(max_length=50)),
                ('nameLast', models.CharField(max_length=50)),
                ('nameGiven', models.CharField(max_length=50)),
                ('weight', models.IntegerField()),
                ('height', models.IntegerField()),
                ('bats', models.CharField(max_length=5)),
                ('throws', models.CharField(max_length=5)),
                ('debut', models.CharField(max_length=50)),
                ('finalGame', models.CharField(max_length=50)),
                ('retroID', models.CharField(max_length=10)),
                ('bbrefID', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Pitching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerID', models.CharField(max_length=10)),
                ('yearID', models.IntegerField()),
                ('stint', models.IntegerField()),
                ('teamID', models.CharField(max_length=10)),
                ('lgID', models.CharField(max_length=10)),
                ('W', models.IntegerField()),
                ('L', models.IntegerField()),
                ('G', models.IntegerField()),
                ('GS', models.IntegerField()),
                ('CG', models.IntegerField()),
                ('SHO', models.IntegerField()),
                ('SV', models.IntegerField()),
                ('IPouts', models.IntegerField()),
                ('H', models.IntegerField()),
                ('ER', models.IntegerField()),
                ('HR', models.IntegerField()),
                ('BB', models.IntegerField()),
                ('SO', models.IntegerField()),
                ('BAOpp', models.IntegerField()),
                ('ERA', models.IntegerField()),
                ('IBB', models.IntegerField()),
                ('WP', models.IntegerField()),
                ('HBP', models.IntegerField()),
                ('BK', models.IntegerField()),
                ('BFP', models.IntegerField()),
                ('GF', models.IntegerField()),
                ('R', models.IntegerField()),
                ('SH', models.IntegerField()),
                ('SF', models.IntegerField()),
                ('GIDP', models.IntegerField()),
            ],
        ),
    ]
