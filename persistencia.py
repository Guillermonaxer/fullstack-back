"""Este fichero guardo el nombre y apellido en un txt"""

def guardar_pedido(nombre, apellidos):
    """funcion que abre y escribe en un fichero"""
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write(nombre+""+apellidos+"\n")
#yo habría puesto:file.write(nombre+" "+apellidos+"\n") para separar 
#el nombre de los apellidos, pero me he limitado a copiar lo que mandastéis.
    file.close()
