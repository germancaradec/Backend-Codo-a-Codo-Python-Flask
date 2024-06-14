#Proyecto final CRUD

# Definimos una lista de diccionarios para almacenar los productos.
productos = []

#Agregar un producto (create)
def agregar_producto(codigo, descripcion, cantidad, precio, imagen, proveedor):
    
    nuevo_producto = { # construimos un diccionario de datos (pares clave-valor)
        'codigo': codigo,
        'descripcion': descripcion,
        'cantidad': cantidad,
        'precio': precio,
        'imagen': imagen,
        'proveedor': proveedor
    }
    productos.append(nuevo_producto)
    return True # El producto fue agregado.

# Programa principal. 

# Agregar productos. 
agregar_producto(1, 'Teclado USB 101 teclas', 10, 4500, 'teclado.jpg', 101)
agregar_producto(2, 'Mouse USB 3 botones', 5, 2500, 'mouse.jpg', 102)
agregar_producto(3, 'Monitor LCD 22 pulgadas', 15, 52500, 'monitor22.jpg', 103)
agregar_producto(4, 'Monitor LCD 27 pulgadas', 25, 78500, 'monitor27.jpg', 104)
agregar_producto(5, 'Pad mouse', 5, 500, 'padmouse.jpg', 105)
agregar_producto(3, 'Parlantes USB', 4, 2500, 'parlantes.jpg', 105)

for producto in productos:
    print(producto)
    print()