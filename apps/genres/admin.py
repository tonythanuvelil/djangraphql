from django.contrib import admin
from .models import Genre


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'created_at', 'is_active',)
    search_fields = ('name', 'category',)


admin.site.register(Genre, GenreAdmin)
