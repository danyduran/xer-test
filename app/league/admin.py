from django.contrib import admin
from league.models import Player, Team

# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "city", "goals")


admin.site.register(Team, TeamAdmin)
admin.site.register(Player)
