from django.contrib import admin
from .models import place, team_members

# Register your models here.
admin.site.register(place)
admin.site.register(team_members)