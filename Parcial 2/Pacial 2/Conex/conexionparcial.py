

import mysql.connector
from mysql.connector import Error


class Conexionpar:
    # métodos
    def __init__(self):
        print('Objeto tipo Conexion creado y listo para usarse..!!')
    def conectar(self):
        try:
            self.connect = mysql.connector.connect(
                host="localhost",
                user="root",
                password= "3213444031jj",
                database="parcialcentrosmayores")
            if self.connect.is_connected():
                print("Conexion lista para usarse ...!!")
                return self.connect
        except Error as error:
            print('Error al intentar abrir la conexión..')
            print(error)

 

    def desconectar(self):
        if self.connect.is_connected():
            self.connect.close()
            print("Conexión cerrada ..!!")

    

