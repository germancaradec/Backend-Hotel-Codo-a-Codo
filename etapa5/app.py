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

class CotizacionesGR:
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
            
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS cotizaciones (
            codigo INT AUTO_INCREMENT PRIMARY KEY, checkin DATE NOT NULL, checkout DATE NOT NULL, tipoHabitacion VARCHAR(20) NOT NULL, cantidadAdultos INT NOT NULL, cantidadMenores INT NOT NULL, cantidadHabitaciones INT NOT NULL, email VARCHAR(40) , asignada VARCHAR(2)  DEFAULT 'NO' );''')
        self.conn.commit()

        # Cerrar el cursor inicial y abrir uno nuevo con diccionario = true
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)

    def agregar_cotizacion(self, checkin, checkout, tipoHabitacion, cantidadAdultos, cantidadMenores, cantidadHabitaciones, email):
        
        sql = "INSERT INTO cotizaciones (checkin, checkout, tipoHabitacion, cantidadAdultos, cantidadMenores, cantidadHabitaciones, email) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores = (checkin, checkout, tipoHabitacion, cantidadAdultos, cantidadMenores, cantidadHabitaciones, email)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.lastrowid
    
    def modificar_cotizacion(self, codigo, nuevo_checkin, nuevo_checkout, nuevo_tipoHabitacion, nueva_cantidadAdultos, nueva_cantidadMenores, nueva_cantidadHabitaciones, nuevo_email, nuevo_asignada):
        sql = "UPDATE cotizaciones SET checkin = %s, checkout = %s, tipoHabitacion = %s, cantidadAdultos = %s, cantidadMenores = %s, cantidadHabitaciones = %s, email = %s , asignada = %s WHERE codigo = %s"
        valores = (nuevo_checkin, nuevo_checkout, nuevo_tipoHabitacion, nueva_cantidadAdultos, nueva_cantidadMenores, nueva_cantidadHabitaciones, nuevo_email,nuevo_asignada, codigo)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def consultar_cotizacion(self, codigo):
        # Consultamos una cotización a partir de su codigo
        self.cursor.execute(f"SELECT * FROM cotizaciones WHERE codigo = {codigo} ")
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
        self.cursor.execute("SELECT * FROM cotizaciones order by asignada ,checkin desc, checkout desc")
        cotizaciones = self.cursor.fetchall()
        return cotizaciones

    def eliminar_cotizacion(self, codigo):
        # Eliminamos una cotización de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM cotizaciones WHERE codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0
    
class ConsultasGR:
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
            
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS consultas (
                        codigo INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(30) NOT NULL, ape VARCHAR(20) NOT NULL, correo VARCHAR(20), tel INT, consulta VARCHAR(500) NOT NULL, `check` BOOLEAN DEFAULT FALSE);''')
        self.conn.commit()

        # Cerrar el cursor inicial y abrir uno nuevo con diccionario = true
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)

        # Agregar una cotización (create)
    
        # Agregar una consulta (create)
    def agregar_consulta(self, nom, ape, correo, tel, consulta, check):
        
        sql = "INSERT INTO consultas (nom, ape, correo, tel, consulta, `check`) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (nom, ape, correo, tel, consulta, check)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.lastrowid
    
    def modificar_consulta(self, codigo, nuevo_nom, nuevo_ape, nuevo_correo, nuevo_tel, nuevo_consulta, nuevo_check):
        sql = "UPDATE consultas SET nom = %s, ape = %s, correo = %s, tel = %s, consulta = %s, `check` = %s WHERE codigo = %s"
        valores = (nuevo_nom, nuevo_ape, nuevo_correo, nuevo_tel, nuevo_consulta, nuevo_check, codigo)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def consultar_consulta(self, codigo):
        # Consultamos una cotización a partir de su codigo
        self.cursor.execute(f"SELECT * FROM consultas WHERE codigo = {codigo} ")
        return self.cursor.fetchone()
    
    def mostrar_consultas(self, codigo):
        # Mostramos los datos de una cotización a partir de su código
        consulta = self.consultar_consulta(codigo)
        if consulta:
            print("-"*50)
            print(f'Nombre.....................: {consulta["nom"]}')
            print(f'Apellido...................: {consulta["ape"]}')
            print(f'Correo..................: {consulta["correo"]}')
            print(f'Telefono.........: {consulta["tel"]}')
            print(f'Consulta........: {consulta["consulta"]}')
            print(f'check........: {consulta["check"]}')

            print("-"*50)
        else:
            print("Consulta no encontrada.")
        
    def listar_consultas(self):
        self.cursor.execute("SELECT * FROM consultas order by codigo ")
        consultas = self.cursor.fetchall()
        return consultas

    def eliminar_consulta(self, codigo):
        # Eliminamos una cotización de la tabla a partir de su código
        self.cursor.execute(f"DELETE FROM consultas WHERE codigo = {codigo}")
        self.conn.commit()
        return self.cursor.rowcount > 0
    




#---------------------------------------------------------------------------
# Programa principal
#---------------------------------------------------------------------------



# Crear una instancia de la clase cotizaciones
cotizacionesGR = CotizacionesGR(host='achuar.mysql.pythonanywhere-services.com', user='achuar', password='hotelapp', database='achuar$hotelapp')

@app.route("/cotizaciones", methods=["GET"])
def listar_cotizaciones():
    cotizaciones = cotizacionesGR.listar_cotizaciones()
    return jsonify(cotizaciones)

@app.route("/cotizaciones/<int:codigo>", methods=["GET"])
def mostrar_cotizacion(codigo):
    cotizacion = cotizacionesGR.consultar_cotizacion(codigo)

    if cotizacion:
        return jsonify(cotizacion)
    else:
        return "Cotización no encontrada", 404

@app.route("/cotizaciones", methods=["POST"])
def agregar_cotizacion():
    # linea = 100
    #Recojo los datos del form
    checkin = request.form['checkin']
    checkout = request.form['checkout']
    # linea = 110
    tipoHabitacion = request.form['tipoHabitacion']
    cantidadAdultos = request.form['cantidadAdultos']
    cantidadMenores = request.form['cantidadMenores']  
    # linea = 120
    cantidadHabitaciones = request.form['cantidadHabitaciones']  
    email = request.form['email']  

    # # Genero el nombre de la imagen
    # nombre_imagen = secure_filename(imagen.filename)
    # nombre_base, extension = os.path.splitext(nombre_imagen) 
    # nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}" 

    nueva_cotizacion = cotizacionesGR.agregar_cotizacion(checkin, checkout, tipoHabitacion, cantidadAdultos, cantidadMenores, cantidadHabitaciones, email)
    if nueva_cotizacion:    
        # imagen.save(os.path.join(ruta_destino, nombre_imagen))
        return jsonify({"mensaje": "Cotizacion agregada correctamente.", "cotizacion": nueva_cotizacion, "checkin": checkin, "checkout": checkout}), 201
    else:
        return jsonify({"mensaje": "Error al agregar la cotizacion."}), 500, {"Access-Control-Allow-Origin": "localhost"}

@app.route("/cotizaciones/<int:codigo>", methods=["PUT"])
def modificar_cotizacion(codigo):
    #Se recuperan los nuevos datos del formulario
    checkin = request.form.get("checkin")
    checkout = request.form.get("checkout")
    tipoHabitacion = request.form.get("tipoHabitacion")
    cantidadAdultos = request.form.get("cantidadAdultos")
    cantidadMenores = request.form.get("cantidadMenores")
    cantidadHabitaciones = request.form.get("cantidadHabitaciones")
    email = request.form.get("email")
    asignada = request.form.get("asignada")
    
    # # Verifica si se proporcionó una nueva imagen
    # if 'imagen' in request.files:
    #     imagen = request.files['imagen']
    #     # Procesamiento de la imagen
    #     nombre_imagen = secure_filename(imagen.filename) 
    #     nombre_base, extension = os.path.splitext(nombre_imagen) 
    #     nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}" 

    #     # Guardar la imagen en el servidor
    #     imagen.save(os.path.join(ruta_destino, nombre_imagen))
        
        # # Busco el cotizacion guardado
        # cotizacion = catalogo.consultar_cotizacion(codigo)
        # if cotizacion: # Si existe el cotizacion...
        #     imagen_vieja = cotizacion["imagen_url"]
        #     # Armo la ruta a la imagen
        #     ruta_imagen = os.path.join(ruta_destino, imagen_vieja)

        #     # Y si existe la borro.
        #     if os.path.exists(ruta_imagen):
        #         os.remove(ruta_imagen)
    # else:     
    #     cotizacion = catalogo.consultar_cotizacion(codigo)
    #     if cotizacion:
    #         nombre_imagen = cotizacion["imagen_url"]


    # Se llama al método modificar_cotizacion pasando el codigo del cotizacion y los nuevos datos.
    if cotizacionesGR.modificar_cotizacion(codigo, checkin, checkout, tipoHabitacion, cantidadAdultos, cantidadMenores, cantidadHabitaciones, email, asignada):
        return jsonify({"mensaje": "Cotizacion modificada"}), 200
    else:
        return jsonify({"mensaje": "Cotizacion no encontrada"}), 403

@app.route("/cotizaciones/<int:codigo>", methods=["DELETE"])
def eliminar_cotizacion(codigo):
    # Primero, obtiene la información del cotizacion para encontrar la imagen
    cotizacion = cotizacionesGR.consultar_cotizacion(codigo)
    if cotizacion:
        # # Eliminar la imagen asociada si existe
        # ruta_imagen = os.path.join(ruta_destino, cotizacion['imagen_url'])
        # if os.path.exists(ruta_imagen):
        #     os.remove(ruta_imagen)

        # Luego, elimina el cotizacion del catálogo
        if cotizacionesGR.eliminar_cotizacion(codigo):
            return jsonify({"mensaje": "Cotizacion eliminada"}), 200
        else:
            return jsonify({"mensaje": "Error al eliminar la cotizacion"}), 500
    else:
        return jsonify({"mensaje": "Cotizacion no encontrada"}), 404




# Crear una instancia de la clase consultas
# consultasGR = ConsultasGR(host='localhost', user='root', password='', database='hotelapp')
consultasGR = ConsultasGR(host='achuar.mysql.pythonanywhere-services.com', user='achuar', password='hotelapp', database='achuar$hotelapp')


@app.route("/consultas", methods=["GET"])
def listar_consultas():
    consultas = consultasGR.listar_consultas()
    return jsonify(consultas)

@app.route("/consultas/<int:codigo>", methods=["GET"])
def mostrar_consultas(codigo):
    consulta = consultasGR.consultar_consulta(codigo)

    if consulta:
        return jsonify(consulta)
    else:
        return "Consulta no encontrada", 404
    
@app.route("/consultas", methods=["POST"])
def agregar_consulta():
    #Recojo los datos del form
    nom = request.form['nom']
    ape = request.form['ape']
    correo = request.form['correo']
    tel = request.form['tel']
    consulta = request.form['consulta']  

    check = 'check' in request.form and request.form['check'] == 'on' 
    
    nueva_consulta = consultasGR.agregar_consulta(nom, ape, correo, tel, consulta, check)
    if nueva_consulta:    
        return jsonify({"mensaje": "Consulta agregada correctamente.", "consulta": nueva_consulta, "nom": nom, "ape": ape}), 201
    else:
        return jsonify({"mensaje": "Error al agregar la consulta."}), 500, {"Access-Control-Allow-Origin": "localhost"}

@app.route("/consultas/<int:codigo>", methods=["PUT"])
def modificar_consulta(codigo):
    #Se recuperan los nuevos datos del formulario
    nom = request.form['nom']
    ape = request.form['ape']
    correo = request.form['correo']
    tel = request.form['tel']
    consulta = request.form['consulta'] 
    # Manejo del checkbox
    check = 'check' in request.form and request.form['check'] == 'on'  
    
    # Se llama al método modificar_cotizacion pasando el codigo del cotizacion y los nuevos datos.
    if consultasGR.modificar_consulta(codigo, nom, ape, correo, tel, consulta, check):
        return jsonify({"mensaje": "Consulta modificada"}), 200
    else:
        return jsonify({"mensaje": "Consulta no encontrada"}), 403

@app.route("/consultas/<int:codigo>", methods=["DELETE"])
def eliminar_consulta(codigo):
    # Primero, obtiene la información del cotizacion para encontrar la imagen
    consulta = consultasGR.consultar_consulta(codigo)
    if consulta:
        # Luego, elimina el cotizacion del catálogo
        if consultasGR.eliminar_consulta(codigo):
            return jsonify({"mensaje": "Consulta eliminada"}), 200
        else:
            return jsonify({"mensaje": "Error al eliminar la consulta"}), 500
    else:
        return jsonify({"mensaje": "Consulta no encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True)