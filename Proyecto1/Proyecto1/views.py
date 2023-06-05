from django.http import HttpResponse


def saludo(request): #Primera vista
    return HttpResponse("Hola mundo, esta es la primera página con Django")