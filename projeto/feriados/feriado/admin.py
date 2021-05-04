from django.contrib import admin
from .models import FeriadoModel
from datetime import datetime

class FeriadoModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'dia', 'mes','modificado_em', 'criado_este_mes')
    date_hierarchy = 'modificado_em'
    search_fields = ('nome', 'dia', 'mes')
    list_filter = ('modificado_em','dia','mes')
    
    def criado_este_mes(self, obj):
        hoje = datetime.today()
        return obj.modificado_em.month == hoje.month

    criado_este_mes.short_description = "Modificado este mês"
    criado_este_mes.boolean = True

admin.site.register(FeriadoModel, FeriadoModelAdmin)
# admin.site.register(FeriadoModel)