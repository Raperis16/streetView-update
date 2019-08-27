from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'api'
urlpatterns = [
    path('game', views.ran_game,  name = 'ran_game' ),
    path('save', views.save, name = 'save'),
]

