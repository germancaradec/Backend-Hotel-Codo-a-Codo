#Proyecto final CRUD

class Registros:
# Definimos una lista de diccionarios para almacenar las solicitudes de cotizaciones.
    cotizaciones = []

    # Agregar una cotización (create)
    def agregar_cotizacion(self, codigo, checkin, checkout, tipoHabitacion, cantidadAdultos, cantidadMenores, cantidadHabitaciones, email):
        
        if self.consultar_cotizacion(codigo):
            return False
        
        nueva_cotizacion = { # construimos un diccionario de datos (pares clave-valor)
            "codigo": codigo,
            "checkin": checkin , 
            "checkout": checkout , 
            "tipoHabitacion": tipoHabitacion,
            "cantidadAdultos": cantidadAdultos , 
            "cantidadMenores": cantidadMenores , 
            "cantidadHabitaciones": cantidadHabitaciones , 
            "email": email
        }
        self.cotizaciones.append(nueva_cotizacion)
        return True # La cotizacion fue agregada.

    def consultar_cotizacion(self, codigo):
        for cotizacion in self.cotizaciones:
            if cotizacion['codigo'] == codigo:
                return cotizacion
        return False
    


# Programa principal. 

registro1 = Registros()

registro1.agregar_cotizacion(1, '2024-06-17T00:00:00.000Z', '2024-06-21T00:00:00.000Z', 'Family', 2, 3, 2, 'germancaradec@gmail.com')
registro1.agregar_cotizacion(2, '2024-06-21T00:00:00.000Z', '2024-06-29T00:00:00.000Z', 'Deluxe', 2, 0, 1, 'robertorodriguez@gmail.com')
registro1.agregar_cotizacion(3, '2024-07-01T00:00:00.000Z', '2024-07-25T00:00:00.000Z', 'Standard', 2, 1, 2, 'cristinaperez@gmail.com')
registro1.agregar_cotizacion(2, '2024-07-01T00:00:00.000Z', '2024-07-25T00:00:00.000Z', 'Standard', 2, 5, 2, 'cristinaperez@gmail.com')

for cotizacion in Registros.cotizaciones:
    print(cotizacion)
    print()





#     # Listar productos (read)

#     def listar_productos(self):
#         print("-"*50)
#         for producto in self.productos:
#             print(f'Código.......: {producto["codigo"]}')
#             print(f'Descripción..: {producto["descripcion"]}')
#             print(f'Cantidad.....: {producto["cantidad"]}')
#             print(f'Precio.......: {producto["precio"]}')
#             print(f'Imagen.......: {producto["imagen"]}')
#             print(f'Proveedor....: {producto["proveedor"]}')
#             print("-"*50)

#     # Modificar un producto (update)
#     def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
#         for producto in self.productos:
#             if producto['codigo'] == codigo:
#                 producto['descripcion'] = nueva_descripcion
#                 producto['cantidad'] = nueva_cantidad
#                 producto['precio'] = nuevo_precio
#                 producto['imagen'] = nueva_imagen
#                 producto['proveedor'] = nuevo_proveedor
#                 return True
#         return False    

#     # Eliminar un producto
#     def eliminar_producto(self, codigo):
#         for producto in self.productos:
#             if producto['codigo'] == codigo:
#                 self.productos.remove(producto)
#                 return True
#         False    

#     # Mostrar un producto
#     def mostrar_producto(self, codigo):
#         producto = self.consultar_producto(codigo)
#         if producto:
#             print("-"*50)
#             print(f'Código.......: {producto["codigo"]}')
#             print(f'Descripción..: {producto["descripcion"]}')
#             print(f'Cantidad.....: {producto["cantidad"]}')
#             print(f'Precio.......: {producto["precio"]}')
#             print(f'Imagen.......: {producto["imagen"]}')
#             print(f'Proveedor....: {producto["proveedor"]}')
#             print("-"*50)



# print("Listando los productos...")
# catalogo.listar_productos()

# print("Modificando un producto...")
# catalogo.modificar_producto(2, 'Mouse PS2 c/ruedita', 3, 25000, 'mouse_viejo.jpg', 101)
# catalogo.listar_productos()

# print("Eliminando el producto 1...")
# catalogo.eliminar_producto(1)
# catalogo.listar_productos()

# print("Mostrando los datos del producto 3")
# catalogo.mostrar_producto(3)









# # for producto in productos:
# #     print(producto)
# #     print()


# # Eliminar un producto
# eliminar_producto(4)
# listar_poroductos()
