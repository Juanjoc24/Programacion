import mysql.connector
from mysql.connector import Error


class Conexion:
    # métodos
    def __init__(self):
        print('Objeto tipo Conexion creado y listo para usarse..!!')

    def conectar(self):
        try:
            self.conect = mysql.connector.connect(
                host="localhost",
                user="root",
                password="3213444031jj",
                database="proyecto_facultad")
            if self.conect.is_connected():
                print("Conexion lista para usarse ...!!")
                return self.conect
        except Error as error:
            print('Error al intentar abrir la conexión..')
            print(error)

    def desconectar(self):
        if self.conect.is_connected():
            self.conect.close()
            print("Conexión cerrada ..!!")

