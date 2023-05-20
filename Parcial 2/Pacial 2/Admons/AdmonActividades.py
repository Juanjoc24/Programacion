
from Conex.conexionparcial import Conexionpar
from Modelos.Actividades import Actividades

class AdmonActiv:
    
    def __init__(self):
        self.con=Conexionpar()
        self.miConexion=self.con.conectar()
        print("objeto tipo Administracion Actividades creado y listo")
        
        self.menu()
        
    def menu(self):
        opcion=-1
        
        while opcion != 0:
            print("=========OPCIONES========")
            print("0: Salir")
            print("1: Nueva actividad")
            print("2: Ver todas las actividades")
            print("3: Buscar actividad")
            print("4: Eliminar actividad")
            print("5: Modificar actividad")
            
            opcion=int(input("digite opcion:"))
            if opcion ==0:
                self.con.desconectar()
                print("Se cierra conexion bye :)")
            elif opcion==1:
                self.nuevaActiv()
            elif opcion==2:
                self.verTodos()
            elif opcion ==3:
                self.buscarActiv()
            elif opcion==4:
                self.eliminarActiv()
            elif opcion==5:
                self.modificarActiv()
                
    def verTodos (self):
        cant= 0
        try:
            mycursor=self.miConexion.cursor()
            mycursor.callproc("allActiv")
            
            for result in mycursor.stored_results():
                
                for(idActividad,Nombre,Descripcion,Fecha,iDCategoria,Centro) in result:
                    laActiv=Actividades(idActividad,Nombre,Descripcion,Fecha,iDCategoria,Centro)
                    print(laActiv.toString())
                    cant= cant+1
            if cant==0:
                print ("No hay actividades registradas")
            
            mycursor.close()
        
        except Exception as miError:
            print ("Fallo ejecutando el procedimiento")
            print(miError)
            
    def existeIdActiv(self, IdActividad):
         try:
             mycursor = self.miConexion.cursor ()
             query = "SELECT count(*) FROM actividades WHERE idActividad = %s;"
             mycursor. execute (query, [IdActividad]) 
             resultados=mycursor.fetchall()
             for registro in resultados:
                 if registro[0] == 1 :
                    return True
                 return False
         except Exception as miError :
             print ('Fallo ejecutando el procedimiento')
             print(miError)
            

    def nuevaActiv(self) :
        idActivNew = int(input('Digite el id de la nueva actividad:' )) 
        if self.existeIdActiv(idActivNew) == True :
            print( "La actividad ya existe no se puede repetir" )
        else :
            idCatNew=int(input("digite id de la categoria de la actividad"))  
            nomNew = input( 'Digite el nombre de la Actividad:')
            descripNew = input("Agrege la descripcion de la actividad:")
            fechaNew=input("Ingrese la fecha(AAAA-MM-DD) de la actividad: ")
            centrNew= input("Ingrese nombre del centro donde sera la actividad")
            try:
                  mycursor = self.miConexion.cursor()
                  mycursor.callproc ('newAct',[idActivNew,nomNew,descripNew,fechaNew,idCatNew,centrNew])
                  self.miConexion.commit()
                  
                  print("La actividad ha sido creada.!!")
                  mycursor.close()
            except Exception as miError :
                     print('Fallo ejecutando el procedimiento')
                     print(miError)
                     
                     
    def eliminarActiv(self):
        idActivDel = input("Digite el id de la actividad a eliminar:")
        if self.existeIdActiv(idActivDel) == False :
            print ("La Actividad no existe, no se puede eliminar") 
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delAct', [ idActivDel ] )
                self.miConexion.commit()
                print ("LA actividad ha sido eliminada..!!")
                mycursor.close()
            except Exception as miError :
                print( 'Fallo ejecutando el procedimiento' )
                print( miError)
                
    def modificarActiv(self):
        idActivOld = input('Digite id actual:')
        if self.existeIdActiv(idActivOld) == False :
            print ("La actividad no existe")
        else :
            idActivNew = input("Digite nuevo id de la actividad: ")
            if idActivNew != idActivOld and self.existeIdActiv(idActivNew) == True:
                print("Ya existe una actividad con ese ID, No se puede modificar")
            else:
                nomNew =input("Digite el nuevo nombre de la Actividad:")
                descripNew =input("Agrege la nueva descripcion de la actividad:")
                fechaNew=input("Ingrese la nueva fecha(AAAA-MM-DD) de la actividad: ")
                idCatNew=int(input("digite id de la categoria de la actividad:"))         
                centrNew= input("Ingrese nombre del centro donde sera la actividad:")
                try:
                    mycursor = self.miConexion.cursor()
                    mycursor.callproc('modAct', [idActivNew,idCatNew,nomNew, descripNew, fechaNew,centrNew,idActivOld]) 
                    self.miConexion.commit()
                    print ("La actividad ha sido modificada..!!")
                    mycursor.close ()
                except Exception as miError:
                    print("Fallo ejecutando")
                    print(miError)
                    
             
                
                 
                 
    def  buscarActiv(self):
         idActivSearch = input('Digite el id de la actividad:')
         
         if self.existeIdActiv(idActivSearch) == False :
            print ("La actividad no existe")
         else :
             try:
                 mycursor = self.miConexion.cursor()
                 mycursor. callproc('getAct', [idActivSearch])
                 for result in mycursor.stored_results():
                     for (IdActividad,Nombre,Descripcion,Fecha,iDCategoria,Centro) in result:
                         laActividad = Actividades(IdActividad,Nombre,Descripcion,Fecha,iDCategoria,Centro)
                         print (laActividad.toString())
                 mycursor.close()
             except Exception as miError :
                print ('Fallo ejecutando el procedimiento')
                print (miError)
                
                
                
                
                