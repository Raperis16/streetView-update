from django.contrib import admin

# Register your models here.
from .models import Random
from .models import Game

class RandomAdmin(admin.ModelAdmin):
    list_display = ["pk","id", "nos", "lng", "lat"]

class GameAdmin(admin.ModelAdmin):
    list_display = ["id", "id_loc", "Result", "Fake1", "Fake2", "Fake3"]

admin.site.register(Random, RandomAdmin)
admin.site.register(Game, GameAdmin)