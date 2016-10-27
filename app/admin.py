from django.contrib import admin
from app.models import Batting, Fielding, Master, Pitching
# Register your models here.
admin.site.register([Batting, Fielding, Master, Pitching])
