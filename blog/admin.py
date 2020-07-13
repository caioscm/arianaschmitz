from django.contrib import admin
from .models import BlogPost

class ListandoPostagem(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'assuntos', 'data_modificacao', 'publicada', 'destaque')
    list_display_links = ('id', 'titulo')
    search_fields = ('nome',)
    list_per_page = 8
    list_editable = ('publicada', 'destaque')

admin.site.register(BlogPost, ListandoPostagem)