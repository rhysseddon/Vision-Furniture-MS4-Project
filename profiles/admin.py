from django.contrib import admin
from .models import Favorites


class FavoritesAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'favorites',
        )


admin.site.register(Favorites)
