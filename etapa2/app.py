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
    
    # Consultar si ya hay una cotizacion con ese código
    def consultar_cotizacion(self, codigo):
        for cotizacion in self.cotizaciones:
            if cotizacion['codigo'] == codigo:
                return cotizacion
        return False
    
    # Listar cotizaciones (read)
    def listar_cotizaciones(self):
        print("-"*50)
        for cotizacion in self.cotizaciones:
            print(f'Código.....................: {cotizacion["codigo"]}')
            print(f'Check-in...................: {cotizacion["checkin"]}')
            print(f'Check-out..................: {cotizacion["checkout"]}')
            print(f'Tipo de habitacion.........: {cotizacion["tipoHabitacion"]}')
            print(f'Cantidad de adultos........: {cotizacion["cantidadAdultos"]}')
            print(f'Cantidad de menores........: {cotizacion["cantidadMenores"]}')
            print(f'Cantidad de habitaciones...: {cotizacion["cantidadHabitaciones"]}')
            print(f'e-mail.....................: {cotizacion["email"]}')
            print("-"*50)

    # Modificar una cotizacion (update)
    def modificar_cotizacion(self, codigo, nuevo_checkin, nuevo_checkout, nuevo_tipoHabitacion, nueva_cantidadAdultos, nueva_cantidadMenores, nueva_cantidadHabitaciones, nuevo_email):
        for cotizacion in self.cotizaciones:
            if cotizacion['codigo'] == codigo:
                cotizacion['checkin'] = nuevo_checkin
                cotizacion['checkout'] = nuevo_checkout
                cotizacion['tipoHabitacion'] = nuevo_tipoHabitacion
                cotizacion['cantidadAdultos'] = nueva_cantidadAdultos
                cotizacion['cantidadMenores'] = nueva_cantidadMenores
                cotizacion['cantidadHabitaciones'] = nueva_cantidadHabitaciones
                cotizacion['email'] = nuevo_email
                return True
        return False    



# Programa principal. 

registro1 = Registros()

print("Agregando cotizaciones...")
print()

registro1.agregar_cotizacion(1, '2024-06-17T00:00:00.000Z', '2024-06-21T00:00:00.000Z', 'Family', 2, 3, 2, 'germancaradec@gmail.com')
registro1.agregar_cotizacion(2, '2024-06-21T00:00:00.000Z', '2024-06-29T00:00:00.000Z', 'Deluxe', 2, 0, 1, 'robertorodriguez@gmail.com')
registro1.agregar_cotizacion(3, '2024-07-01T00:00:00.000Z', '2024-07-25T00:00:00.000Z', 'Standard', 2, 1, 2, 'cristinaperez@gmail.com')
registro1.agregar_cotizacion(2, '2024-07-01T00:00:00.000Z', '2024-07-25T00:00:00.000Z', 'Standard', 2, 5, 2, 'cristinaperez@gmail.com')

print("Iterando cotizaciones...")
print()

for cotizacion in Registros.cotizaciones:
    print(cotizacion)
    print()

print("Listando las cotizaciones...")
registro1.listar_cotizaciones()

print("Modificando una cotizacion...")
registro1.modificar_cotizacion(2, '2024-07-01T00:00:00.000Z', '2024-07-25T00:00:00.000Z', 'Standard', 2, 5, 2, 'cristinaperez@gmail.com')
registro1.listar_cotizaciones()





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
