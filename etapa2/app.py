#Proyecto final CRUD

class Catalogo:
# Definimos una lista de diccionarios para almacenar los productos.
    productos = []

    # Agregar un producto (create)
    def agregar_producto(self, codigo, descripcion, cantidad, precio, imagen, proveedor):
        
        if self.consultar_producto(codigo):
            return False
        
        nuevo_producto = { # construimos un diccionario de datos (pares clave-valor)
            'codigo': codigo,
            'descripcion': descripcion,
            'cantidad': cantidad,
            'precio': precio,
            'imagen': imagen,
            'proveedor': proveedor
        }
        self.productos.append(nuevo_producto)
        return True # El producto fue agregado.

    def consultar_producto(self, codigo):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                return producto
        return False

    # Listar productos (read)

    def listar_productos(self):
        print("-"*50)
        for producto in self.productos:
            print(f'Código.......: {producto["codigo"]}')
            print(f'Descripción..: {producto["descripcion"]}')
            print(f'Cantidad.....: {producto["cantidad"]}')
            print(f'Precio.......: {producto["precio"]}')
            print(f'Imagen.......: {producto["imagen"]}')
            print(f'Proveedor....: {producto["proveedor"]}')
            print("-"*50)

    # Modificar un producto (update)
    def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                producto['descripcion'] = nueva_descripcion
                producto['cantidad'] = nueva_cantidad
                producto['precio'] = nuevo_precio
                producto['imagen'] = nueva_imagen
                producto['proveedor'] = nuevo_proveedor
                return True
        return False    

    # Eliminar un producto
    def eliminar_producto(self, codigo):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                self.productos.remove(producto)
                return True
        False    

    # Mostrar un producto
    def mostrar_producto(self, codigo):
        producto = self.consultar_producto(codigo)
        if producto:
            print("-"*50)
            print(f'Código.......: {producto["codigo"]}')
            print(f'Descripción..: {producto["descripcion"]}')
            print(f'Cantidad.....: {producto["cantidad"]}')
            print(f'Precio.......: {producto["precio"]}')
            print(f'Imagen.......: {producto["imagen"]}')
            print(f'Proveedor....: {producto["proveedor"]}')
            print("-"*50)


# Programa principal. 

catalogo = Catalogo()

catalogo.agregar_producto(1, 'Teclado USB 101 teclas', 10, 4500, 'teclado.jpg', 101)
catalogo.agregar_producto(2, 'Mouse USB 3 botones', 5, 2500, 'mouse.jpg', 102)
catalogo.agregar_producto(3, 'Monitor LCD 22 pulgadas', 15, 52500, 'monitor22.jpg', 103)
catalogo.agregar_producto(4, 'Monitor LCD 27 pulgadas', 25, 78500, 'monitor27.jpg', 104)
catalogo.agregar_producto(5, 'Pad mouse', 5, 500, 'padmouse.jpg', 105)

print("Listando los productos...")
catalogo.listar_productos()

print("Modificando un producto...")
catalogo.modificar_producto(2, 'Mouse PS2 c/ruedita', 3, 25000, 'mouse_viejo.jpg', 101)
catalogo.listar_productos()

print("Eliminando el producto 1...")
catalogo.eliminar_producto(1)
catalogo.listar_productos()

print("Mostrando los datos del producto 3")
catalogo.mostrar_producto(3)









# # for producto in productos:
# #     print(producto)
# #     print()


# # Eliminar un producto
# eliminar_producto(4)
# listar_poroductos()
