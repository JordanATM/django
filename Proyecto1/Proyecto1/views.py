from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo(request): #Primera vista

    p1 = Persona("Pedro","Pereira")

    # nombre = "Jordán"
    # apellido = "Torrejón"
    ahora = datetime.datetime.now()

    doc_externo = open("Proyecto1/plantillas/mi-plantilla.html")
    plt = Template(doc_externo.read())
    doc_externo.close()

    ctx = Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido, "fecha":ahora})

    documento = plt.render(ctx)
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta la próxima!")

def dame_fecha(request):
    fecha_actual = datetime.datetime.now()
    documento = """
    <html>
    <body>
        <h1>Fecha y hóra actuales %s</h1>
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