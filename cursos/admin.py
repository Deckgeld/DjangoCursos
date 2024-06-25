from django.contrib import admin
from .models import Cursos
from .models import Actividad

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id', 'nombre', 'categoria','autor', 'precio', 'likes', 'created')
    search_fields = ('created','nombre')
    date_hierarchy = 'created'
    list_filter = ('categoria','autor')

admin.site.register(Cursos, AdministrarModelo)

##############

class AdministrarActividad(admin.ModelAdmin):
    list_display = ('id', 'desc')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')

admin.site.register(Actividad, AdministrarActividad)
