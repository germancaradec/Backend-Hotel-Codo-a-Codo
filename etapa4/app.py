#--------------------------------------------------------------------
# Instalar con pip install Flask
from flask import Flask, request, jsonify

# Instalar con pip install flask-cors
from flask_cors import CORS

# Instalar con pip install mysql-connector-python
import mysql.connector

# Si es necesario, pip install Werkzeug
import mysql.connector.errorcode
from werkzeug.utils import secure_filename

# No es necesario instalar, es parte del sistema standard de Python
import os
import time
#--------------------------------------------------------------------

app = Flask(__name__)
CORS(app)  # Esto habilitará CORS para todas las rutas

class Registros:
    # Constuctor de la clase
    def __init__(self, host, user, password, database):

        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()
        # Intentamos seleccionar la base de datos
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            #Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err
            
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS registros (
            codigo INT AUTO_INCREMENT PRIMARY KEY, checkin VARCHAR(35) NOT NULL, checkout VARCHAR(35) NOT NULL, tipoHabitacion VARCHAR(20) NOT NULL, cantidadAdultos INT NOT NULL, cantidadMenores INT, cantidadHabitaciones INT NOT NULL, email VARCHAR(40));''')
        self.conn.commit()

        # Cerrar el cursor inicial y abrir uno nuevo con diccionario = true
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)

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
    

#---------------------------------------------------------------------------
# Programa principal
#---------------------------------------------------------------------------
# Crear una instancia de la clase catalogo
registro = Registros(host='localhost', user='root', password='', database='hotelapp')

@app.route("/cotizaciones", methods=["GET"])
def listar_cotizaciones():
    cotizaciones = registro.listar_cotizaciones()
    return jsonify(cotizaciones)

@app.route("/cotizaciones/<int:codigo>", methods=["GET"])
def mostrar_cotizacion(codigo):
    cotizacion = registro.consultar_cotizacion(codigo)
    if cotizacion:
        return jsonify(cotizacion)
    else:
        return "Cotización no encontrada", 404

if __name__ == "__main__":
    app.run(debug=True)