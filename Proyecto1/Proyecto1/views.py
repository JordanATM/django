from django.http import HttpResponse
import datetime

documento = """
<html>
<body>
    <h1>Hola mundo, esta es la primera página con Django</h1>
</body>
</html>

"""
def saludo(request): #Primera vista
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta la próxima!")

def dame_fecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """
    <html>
    <body>
        <h1>Fecha y hora actuales %s</h1>
    </body>
    </html>
    """ % fecha_actual

    return HttpResponse(documento)

def calcula_edad(request,edad, agno):

    # edadActual = 26
    periodo = agno - 2023
    edadFutura = edad + periodo
    documento = """
    <html>
    <body>
        <h1>En el año %s tendrás %s años</h1>
    </body>
    </html>
    """ % (agno, edadFutura)

    return HttpResponse(documento)