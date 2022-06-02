
"""APP backend"""
from flask import Flask, request, redirect
import persistencia

app = Flask(__name__)


@app.route("/pizza", methods=['POST'])
def hello():
    """Esta es la funcion de nuestro backend"""

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
