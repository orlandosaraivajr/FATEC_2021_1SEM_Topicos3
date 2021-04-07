from django.shortcuts import render

def natal(request):
    contexto = {'natal':False,
                'carnaval':False}
    return render(request, 'natal.html', contexto)