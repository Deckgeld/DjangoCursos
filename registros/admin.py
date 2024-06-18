from django.contrib import admin
from .models import Cursos

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'nombre', 'categoria','autor', 'precio', 'likes')
    search_fields = ('id','nombre','categoria', 'autor')
    date_hierarchy = 'created'
    list_filter = ('categoria','autor')

admin.site.register(Cursos, AdministrarModelo)

