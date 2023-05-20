

from Conex.conexionparcial import Conexionpar
from Modelos.Inscripciones import Inscripciones

class AdmonInscrip:
    
    def __init__(self):
        self.con=Conexionpar()
        self.miConexion=self.con.conectar()
        print("objeto tipo Administracion inscripcion creado y listo")
        
        self.menu()
        
    def menu(self):
        opcion=-1
        while opcion != 0:
            print("=========OPCIONES========")
            print("0: Salir")
            print("1: Nueva inscripcion")
            print("2: Ver todas las inscripciones") 
            print("3: Buscar iscripcion")
            print("4: Eliminar inscripcion")
            print("5: Modificar inscripcion")
            
            opcion=int(input("digite opcion:"))
            if opcion ==0:
                self.con.desconectar()
                print("Se cierra conexion bye :)")
            elif opcion==1:
                self.nuevaInscrip()
            elif opcion==2:
                self.verTodos()
            elif opcion ==3:
                self.buscarInscrip()
            elif opcion==4:
                self.eliminarInscrip()
            elif opcion==5:
                self.modificarInscrip()
                
    def verTodos (self):
        cant= 0
        try:
            mycursor=self.miConexion.cursor()
            mycursor.callproc("allInscrip")
            
            for result in mycursor.stored_results():
                
                for(idAdulto,idActividad,Calificacion) in result:
                    laInscrip=Inscripciones(idAdulto,idActividad,Calificacion)
                    print(laInscrip.toString())
                    cant= cant+1
            if cant==0:
                print ("No hay inscripciones registradas")
            
            mycursor.close()
        
        except Exception as miError:
            print ("Fallo ejecutando el procedimiento")
            print(miError)
            
    def existeIdAdul(self, idAdulto):
         try:
             mycursor = self.miConexion.cursor ()
             query = "SELECT count(*) FROM inscripciones WHERE IdAdulto = %s;"
             mycursor. execute (query, [idAdulto]) 
             resultados=mycursor.fetchall()
             for registro in resultados:
                 if registro[0] == 1 :
                    return True
                 return False
         except Exception as miError :
             print ('Fallo ejecutando el procedimiento')
             print(miError)
 
    def existeIdAct(self, idActividad):
         try:
             mycursor = self.miConexion.cursor ()
             query = "SELECT count(*) FROM inscripciones WHERE IdActividad = %s;"
             mycursor. execute (query, [idActividad]) 
             resultados=mycursor.fetchall()
             for registro in resultados:
                 if registro[0] == 1 :
                    return True
                 return False
         except Exception as miError :
             print ('Fallo ejecutando el procedimiento')
             print(miError)  
    
    def validarCal(self, Calificacion):
         try:
             mycursor = self.miConexion.cursor ()
             query = "SELECT count(*) FROM inscripciones WHERE Calificacion > 0 and Caificacion < 11;"
             mycursor. execute (query, [Calificacion]) 
             resultados=mycursor.fetchall()
             for registro in resultados:
                 if registro[0] == 1 :
                    return True
                 return False
         except Exception as miError :
             print ('Fallo ejecutando el procedimiento')
             print(miError)        
 
    
    def nuevaInscrip(self) :
        idAdulNew= int(input('Digite el id del nuevo adulto:' )) 
        idActNew= int(input('Digite el id de la nueva Actividad:' ))
        if self.existeIdAdul(idAdulNew) and self.existeIdAct(idActNew)  == True :
            print( "La Incripcion ya existe no se puede repetir" )
        else :
            calNew =int( input( 'Digite lacalificacion de la acividad:'))
            if self.validarCal(calNew)== False :
                print("La calificacion no es valida")
            else:
                
                try:
                      mycursor = self.miConexion.cursor()
                      mycursor.callproc ('newInscri',[idAdulNew,idActNew,calNew])#orden proceso
                      self.miConexion.commit()
                      
                      print("La inscripcion ha sido creada.!!")
                      mycursor.close()
                except Exception as miError :
                         print('Fallo ejecutando el procedimiento')
                         print(miError)
                
            
            
                     
                     
    def eliminarInscrip(self):
        idAdulDel=int( input("Digite el id del adult a eliminar:"))
        idActDel=int(input("Ingrese id de acividad a eliminar"))
        if self.existeIdAdul(idAdulDel) and self.existeIdAct(idActDel)== True :
            print ("La inscripcion no existe, no se puede eliminar") 
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delInscrip', [ idAdulDel,idActDel ] )
                self.miConexion.commit()
                print ("la inscripcio ha sido eliminada..!!")
                mycursor.close()
            except Exception as miError :
                print( 'Fallo ejecutando el procedimiento' )
                print( miError)
                
    def modificarInscrip(self):
        idAdulOld = int(input('Digite id adulto actual:'))
        idActOld = int(input('Digite id acividad actual:'))
        if self.existeIdAdul(idAdulOld) and self.existeIdAct(idActOld)== True :
            print ("La inscripcion no existe")
        else :
            idAdulNew = int(input("Digite nuevo id del Adulto: "))
            idActNew = int(input("Digite nuevo id de la actividad:"))
            if idAdulNew != idAdulOld and idActNew != idActOld and self.existeIdAdul(idAdulNew) and self.existeIdAct(idActNew) == True:
                print("Ya existe una   con esos ID, No se puede modificar")
            else:
                calNew =int( input( 'Digite la calificacion de la actividad:'))
                if self.validarCal(calNew)== False :
                    print("Ingrese calificacion Valida")
                else:
                    try:
                        mycursor = self.miConexion.cursor()
                        mycursor.callproc('modInscrip',[idAdulNew,idActNew,calNew,idAdulOld,idActOld]) #orden proceso
                        self.miConexion.commit()
                        print ("La inscripcion ha sido modificada..!!")
                        mycursor.close ()
                    except Exception as miError:
                        print("Fallo ejecutando")
                        print(miError)
                    
                
                    
             
                
                 
                 
    def  buscarInscrip(self):
         idAdulSearch = input('Digite el id del adulto:')
         idActSearch = input('Digite el id de la activdad:')
         if self.existeIdAdul(idAdulSearch) and self.existeIdAct(idActSearch) == False :
            print ("La inscripcion no existe")
         else :
             try:
                 mycursor = self.miConexion.cursor()
                 mycursor. callproc('getInscrip', [idAdulSearch,idActSearch])
                 for result in mycursor.stored_results():
                     for (IdAdulto,IdActividad,Calificacion) in result:#como la tabla
                         laInscripcion = Inscripciones(IdAdulto,IdActividad,Calificacion)
                         print (laInscripcion.toString())
                 mycursor.close()
             except Exception as miError :
                print ('Fallo ejecutando el procedimiento')
                print (miError)

