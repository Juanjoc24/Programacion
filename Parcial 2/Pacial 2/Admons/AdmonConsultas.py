
from Conex.conexionparcial import Conexionpar

class AdmonConsul:
    
    def __init__(self):
        self.con=Conexionpar()
        self.miConexion=self.con.conectar()
        print("objeto tipo Administracion consultas creado y listo")
        self.menu()
    
    def menu(self):
        opcion=-1
        while opcion != 0:
            print("=========OPCIONES========")
            print("0: Salir")
            print("1: Consulta 1")
            print("2: Consulta 2")
            print("3: Consulta 3")
            print("4: Consulta 4")
            print("5: Consulta 5")
            
            opcion=int(input("digite opcion:"))
            if opcion ==0:
                self.con.desconectar()
                print("Se cierra conexion bye :)")
            elif opcion==1:
                self.verAlgo1()
            elif opcion==2:
                self.verAlgo2()
            elif opcion ==3:
                self.verAlgo3()
            elif opcion==4:
                self.verAlgo4()
            elif opcion==5:
                self.verAlgo5()    
        
    def  verAlgo1(self):
        try:
            mycursor=self.miConexion.cursor()
            query="SELECT centros.Nombre AS CENTRO, adultos.Nombre as NOMBRE , adultos.Apellido AS APELLIDO FROM adultos inner join centros on adultos.Centro = centros.Nombre order by centros.Nombre and adultos.Apellido;"   
            mycursor.execute(query)
            resultados=mycursor.fetchall()
            for registro in resultados:
                print(registro [0], registro [1], registro [2])
        except Exception as miError:
            print("Fallo ejecutando el procedimiento")
            print(miError)
            
    def  verAlgo2(self):
        try:
            mycursor=self.miConexion.cursor()
            query="SELECT categorias.Nombre as Categoria , actividades.Fecha as Fecha, actividades.Nombre as Nombre_actividad, actividades.Descripcion As Descripcion, centros.Direccion as Direccion from (actividades inner join categorias on actividades.iDCategoria= categorias.idCategoria) inner join centros on actividades.Centro=centros.Nombre;"   
            mycursor.execute(query)
            resultados=mycursor.fetchall()
            for registro in resultados:
                print(registro [0], registro [1], registro [2])
        except Exception as miError:
            print("Fallo ejecutando el procedimiento")
            print(miError)        
    
    def  verAlgo3(self):
        try:
            mycursor=self.miConexion.cursor()
            query="SELECT actividades.Nombre AS NOMBRE, adultos.Nombre as Nombre_Participante,  inscripciones.Calificacion as CALIFICACION FROM (inscripciones inner join actividades on inscripciones.IdActividad=actividades.idActividad) inner join adultos on inscripciones.IdAdulto=adultos.idAdulto order by Calificacion;"   
            mycursor.execute(query)
            resultados=mycursor.fetchall()
            for registro in resultados:
                print(registro [0], registro [1], registro [2])
        except Exception as miError:
            print("Fallo ejecutando el procedimiento")  
            print(miError)
     
    def  verAlgo4(self):
        try:
            mycursor=self.miConexion.cursor()
            query="SELECT adultos.Nombre As Nombre, adultos.Apellido As Apellido from (inscripciones inner join actividades on inscripciones.idActividad=actividades.idActividad) inner join adultos on inscripciones.IdAdulto=adultos.idAdulto where actividades.idActividad=2;"  
            mycursor.execute(query)
            resultados=mycursor.fetchall()
            for registro in resultados:
                print(registro [0], registro [1], registro [2])
        except Exception as miError:
            print("Fallo ejecutando el procedimiento")  
            print(miError)        
    
    def  verAlgo5(self):
        try:
            mycursor=self.miConexion.cursor()
            query="SELECT actividades.Fecha AS FECHA,  actividades.Nombre AS NOMBRE, inscripciones.Calificacion AS CALIFICACION FROM (inscripciones inner join actividades on inscripciones.IdActividad=actividades.idActividad) inner join adultos on inscripciones.IdAdulto=adultos.idAdulto where adultos.idAdulto=4444;"   
            mycursor.execute(query)
            resultados=mycursor.fetchall()
            for registro in resultados:
                print(registro [0], registro [1], registro [2])
        except Exception as miError:
            print("Fallo ejecutando el procedimiento")
            print(miError)   
            
            
   


    
