import persistencia

with open("pedidos.txt", "w", encoding="utf-8") as file:
    file.write("")
    file.close()

    pedidos = [{"nombre": "Pedro", "apellidos": "Gil de Diego"},
               {"nombre": "Michael", "apellidos": "Jordan"}]

for n in pedidos:

    persistencia.guardar_pedido(n['nombre'], n['apellidos'])
