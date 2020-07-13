from django.contrib import admin


from .models import Receitas, Mensagens

class ReceitasAdmin(admin.ModelAdmin):

	list_display = ['name', 'slug', 'update_at']

admin.site.register(Receitas, ReceitasAdmin)