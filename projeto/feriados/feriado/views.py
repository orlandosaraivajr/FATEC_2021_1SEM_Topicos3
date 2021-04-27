from django.shortcuts import render
from feriado.models import FeriadoModel
from datetime import date

def feriado(request):
    verifica_feriado = False
    nome_feriado = ''
    hoje = date.today()
    feriados = FeriadoModel.objects.all()
    for feriado in feriados:
        if feriado.dia == hoje.day:
            if feriado.mes == hoje.month:
                verifica_feriado = True
                nome_feriado = feriado.nome
    contexto = {'feriado':verifica_feriado,
                'nome_feriado':nome_feriado}
    return render(request, 'mostra_feriado.html', contexto)