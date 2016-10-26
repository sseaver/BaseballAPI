# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 21:07
from __future__ import unicode_literals
import csv
from django.db import migrations


def add_info(apps, schema_editor):
    Master = apps.get_model("app", "Master")
    Batting = apps.get_model("app", "Batting")
    Pitching = apps.get_model("app", "Pitching")
    Fielding = apps.get_model("app", "Fielding")

    with open('core/Master.csv') as open_file:
        reader = csv.reader(open_file)
        for row in reader:
            Master.objects.create(playerID=row[0], birthYear=row[1], birthMonth=row[2],
                                  birthDay=row[3], birthCountry=row[4], birthState=row[5],
                                  birthCity=row[6], deathYear=row[7], deathMonth=row[8],
                                  deathDay=row[9], deathCountry=row[10], deathState=row[11],
                                  deathCity=row[12], nameFirst=row[13], nameLast=row[14],
                                  nameGiven=row[15], weight=row[16], height=row[17],
                                  bats=row[18], throws=row[19], debut=row[20], finalGame=row[21],
                                  retroID=row[22], bbrefID=row[23])

            raise Exception("BOOMSHAKALAKA!")

    with open("core/Batting.csv") as open_file:
        reader = csv.reader(open_file)
        for row in reader:
            master = Master.objects.get(playerID=row[0])
            Batting.objects.create(playerID=master, yearID=row[1], stint=row[2],
                                   teamID=row[3], lgID=row[4], G=row[5], AB=row[6],
                                   R=row[7], H=row[8], doubles=row[9], triples=row[10],
                                   HR=row[11], RBI=row[12], SB=row[13], CS=row[14],
                                   BB=row[15], SO=row[16], IBB=row[17], HBP=row[18],
                                   SH=row[19], SF=row[20], GIDP=row[21])

            raise Exception("BOOMSHAKALAKA!")

    with open("core/Pitching.csv") as open_file:
        reader = csv.reader(open_file)
        for row in reader:
            master = Master.objects.get(playerID=row[0])
            Pitching.objects.create(playerID=master, yearID=row[1], stint=row[2],
                                    teamID=row[3], lgID=row[4], W=row[5], L=row[6],
                                    G=row[7], GS=row[8], CG=row[9], SHO=row[10],
                                    SV=row[11], IPouts=row[12], H=row[13], ER=row[14],
                                    HR=row[15], BB=row[16], SO=row[17], BAOpp=row[18],
                                    ERA=row[19], IBB=row[20], WP=row[21], HBP=row[22],
                                    BK=row[23], BFP=row[24], GF=row[25], R=row[26],
                                    SH=row[27], SF=row[28], GIDP=row[29])

            raise Exception("BOOMSHAKALAKA!")

    with open("core/Fielding.csv") as open_file:
        reader = csv.reader(open_file)
        for row in reader:
            master = Master.objects.get(playerID=row[0])
            Fielding.objects.create(playerID=master, yearID=row[1], stint=row[2],
                                    teamID=row[3], lgID=row[4], POS=row[5], G=row[6],
                                    GS=row[7], InnOuts=row[8], PO=row[9], A=row[10],
                                    E=row[11], DP=row[12], PB=row[13], WP=row[14],
                                    SB=row[15], CS=row[16], ZR=row[17])

            raise Exception("BOOMSHAKALAKA!")


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20161026_1909'),
    ]

    operations = [
    ]