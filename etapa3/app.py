import mysql.connector

class Registros:

    def __init__(self, host, user, password, database):

        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS registros (
            codigo INT AUTO_INCREMENT PRIMARY KEY, checkin VARCHAR(35) NOT NULL, checkout VARCHAR(35) NOT NULL, tipoHabitacion VARCHAR(20) NOT NULL, cantidadAdultos INT NOT NULL, cantidadMenores INT, cantidadHabitaciones INT NOT NULL, email VARCHAR(40));''')
        self.conn.commit()

    # Agregar una cotización (create)
    def agregar_cotizacion(self, checkin, checkout, tipoHabitacion, cantidadAdultos, cantidadMenores, cantidadHabitaciones, email):
        
        sql = "INSERT INTO registros (checkin, checkout, tipoHabitacion, cantidadAdultos, cantidadMenores, cantidadHabitaciones, email) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores = (checkin, checkout, tipoHabitacion, cantidadAdultos, cantidadMenores, cantidadHabitaciones, email)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.lastrowid
    
    def modificar_cotizacion(self, codigo, nuevo_checkin, nuevo_checkout, nuevo_tipoHabitacion, nueva_cantidadAdultos, nueva_cantidadMenores, nueva_cantidadHabitaciones, nuevo_email):
        sql = "UPDATE registros SET checkin = %s, checkout = %s, tipoHabitacion = %s, cantidadAdultos = %s, cantidadMenores = %s, cantidadHabitaciones = %s, email = %s WHERE codigo = %s"
        valores = (nuevo_checkin, nuevo_checkout, nuevo_tipoHabitacion, nueva_cantidadAdultos, nueva_cantidadMenores, nueva_cantidadHabitaciones, nuevo_email, codigo)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def consultar_cotizacion(self, codigo):
        # Consultamos una cotización a partir de su codigo
        self.cursor.execute(f"SELECT * FROM registros WHERE codigo = {codigo}")
        return self.cursor.fetchone()
    
    def mostrar_cotizacion(self, codigo):
        # Mostramos los datos de una cotización a partir de su código
        cotizacion = self.consultar_cotizacion(codigo)
        if cotizacion:
            print("-"*50)
            print(f'Código.....................: {cotizacion["codigo"]}')
            print(f'Check-in...................: {cotizacion["checkin"]}')
            print(f'Check-out..................: {cotizacion["checkout"]}')
            print(f'Tipo de habitacion.........: {cotizacion["tipoHabitacion"]}')
            print(f'Cantidad de adultos........: {cotizacion["cantidadAdultos"]}')
            print(f'Cantidad de menores........: {cotizacion["cantidadMenores"]}')
            print(f'Cantidad de habitaciones...: {cotizacion["cantidadHabitaciones"]}')
            print(f'e-mail.....................: {cotizacion["email"]}')
            print("-"*50)
        else:
            print("Cotización no encontrada.")
        
    def listar_cotizaciones(self):
        self.cursor.execute("SELECT * FROM registros")
        cotizaciones = self.cursor.fetchall()
        return cotizaciones

    def eliminar_cotizacion(self, codigo):
        # Eliminamos una cotización de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM registros WHERE codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0


# Programa principal
registro = Registros(host='localhost', user='root', password='', database='hotelapp')

# # Agregar cotización a la tabla
# registro.agregar_cotizacion('2024-06-17', '2024-06-21', 'Family', 2, 3, 2, 'germancaradec@gmail.com')
# registro.agregar_cotizacion('2024-06-21', '2024-06-29', 'Deluxe', 2, 0, 1, 'robertorodriguez@gmail.com')
# registro.agregar_cotizacion('2024-07-01', '2024-07-25', 'Standard', 2, 5, 2, 'cristinaperez@gmail.com')

# # Consultamos una cotización y la mostramos
# cod_cot = int(input("Ingrese el código de la cotizacion: "))
# cotizacion = registro.consultar_cotizacion(cod_cot)
# if cotizacion:
#     print(f"Cotización encontrada: {cotizacion['codigo']} - {cotizacion['checkin']} - {cotizacion['checkout']}")
# else:
#     print(f'Cotización {cod_cot} no encontrada.')

# # Modificar y consultar cotización
# registro.mostrar_cotizacion(2)
# registro.modificar_cotizacion(2, '2024-07-01', '2024-07-25', 'Standard', 2, 10, 2, 'cristinaperez@gmail.com')
# registro.mostrar_cotizacion(2)

# # Listar cotización
# cotizaciones = registro.listar_cotizaciones()
# for cotizacion in cotizaciones:
#     print(cotizacion)

# # Eliminamos la cotización 3
# registro.eliminar_cotizacion(3)
# cotizaciones = registro.listar_cotizaciones()
# for cotizacion in cotizaciones:
#     print(cotizacion)



