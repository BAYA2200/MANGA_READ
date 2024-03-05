from django.contrib import admin

# Register your models here.
from anime.models import Anime, Type, Genre

admin.site.register(Anime)
admin.site.register(Type)
admin.site.register(Genre)