from django.http import HttpResponse

def natal(request):
    return HttpResponse("<center><h1>Não é natal.</h1></center>")