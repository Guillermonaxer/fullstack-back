
from flask import Flask, request, redirect, Response
import persistencia

app = Flask(__name__)


@app.route("/pizza", methods=['POST'])
@app.route("/checksize", methods=['POST'])
def checksize():
    """
    Comprueba disponibilidad de un tamaño de pizza.
    """
    nombre = request.form.get("tamaño")
    if nombre == 'S':
       mensaje = 'No disponible'
    if nombre != 'S' and nombre != 'selecciona':
      mensaje = 'Disponible'
    if nombre == 'selecciona':
      mensaje = 'Error:Debes seleccionar un tamaño'

    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})
   


def hello():
    """
    Guardo pedido y redirecciono a solicita_pedido.
    """
    nombre = request.form.get("nombre")
    apellidos = request.form.get("apellidos")
    print(nombre)
    print(apellidos)
    # guardo nombre y apellidos en un txt(no me quedaba claro si era necesario o no)
    with open("pedidos.txt", "w", encoding="utf-8") as file:
        file.write("")
        file.close()
    persistencia.guardar_pedido(nombre, apellidos)
    return redirect("http://localhost/master/solicita_pedido.html", code=302)
