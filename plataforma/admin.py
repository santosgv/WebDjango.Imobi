
from django.contrib import admin
from .models import DiasVisita, Horario, Imovei, Cidade, Imagem, Visitas

@admin.register(Imovei)
class ImoveiAdmin(admin.ModelAdmin):
    list_display = ('rua', 'valor', 'quartos', 'tamanho', 'cidade', 'tipo')
    list_editable = ('valor', 'tipo')
    list_filter = ('cidade', 'tipo','quartos')


class VisitasAdmin(admin.ModelAdmin):
    list_display = ('usuario')
    list_editable = ('status')
    list_filter = ()
    
admin.site.register(DiasVisita)
admin.site.register(Horario)
admin.site.register(Imagem)
admin.site.register(Cidade)
admin.site.register(Visitas)
