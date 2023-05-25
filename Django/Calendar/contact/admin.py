from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', # Cria colunas de informações
    ordering = '-id', # Cria ordem crescente/decrescente
    list_filter = ('created_date',) # Criar filtro
    search_fields = ('id', 'first_name', 'last_name') # Barra de pesquisa
    list_per_page = 30 # Valores por Paginas
    list_max_show_all = 5000 # Maximo de valores por Paginas
    # list_editable = 'first_name', 'last_name', # Edita valores antes de selecionar
    list_display_links = 'id', 'phone',
    
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name', # Cria colunas de informações
    ordering = '-id', # Cria ordem crescente/decrescente
