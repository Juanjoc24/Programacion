
from Conex.conexionparcial import Conexionpar
from Modelos.Centros import Centros

class AdmonCentr:
    
    def __init__(self):
        self.con=Conexionpar()
        self.miConexion=self.con.conectar()
        print("objeto tipo Administracion Centros creado y listo")
        
        self.menu()
        
    def menu(self):
        opcion=-1
        while opcion != 0:
            print("=========OPCIONES========")
            print("0: Salir")
            print("1: Nuevo Centro")
            print("2: Ver todos los centros")
            print("3: Buscar Centro")
            print("4: Eliminar centro")
            print("5: Modificar centro")
            
            opcion=int(input("digite opcion:"))
            if opcion ==0:
                self.con.desconectar()
                print("Se cierra conexion bye :)")
            elif opcion==1:
                self.nuevoCentro()
            elif opcion==2:
                self.verTodos()
            elif opcion ==3:
                self.buscarCentro()
            elif opcion==4:
                self.eliminarCentro()
            elif opcion==5:
                self.modificarCentro()
                
    def verTodos (self):
        cant= 0
        try:
            mycursor=self.miConexion.cursor()
            mycursor.callproc("allCentros")
            
            for result in mycursor.stored_results():
                
                for(Nombre,Direccion,Telefono) in result:
                    elCentro=Centros(Nombre, Direccion, Telefono)
                    print(elCentro.toString())
                    cant= cant+1
            if cant==0:
                print ("No hay centros registradas")
            
            mycursor.close()
        
        except Exception as miError:
            print ("Fallo ejecutando el procedimiento")
            print(miError)
            
    def existeNombre (self, Nombre):
         try:
             mycursor = self.miConexion.cursor ()
             query = "SELECT count(*) FROM centros WHERE Nombre = %s ;"
             mycursor. execute (query, [Nombre]) 
             resultados=mycursor.fetchall()
             for registro in resultados:
                 if registro[0] == 1 :
                    return True
                 return False
         except Exception as miError :
             print ('Fallo ejecutando el procedimiento')
             print(miError)
            

    def nuevoCentro ( self) :
        nomNew = input('Digite el nombre del nuevo centro: ' ) 
        if self.existeNombre ( nomNew) == True :
            print( "El centro ya existe no se puede repetir" )
        else :
              direcNew = input ( 'Digite la direccion del centro:')
              telNew = input("Digite el numero del centro:")
              try:
                  mycursor = self.miConexion.cursor()
                  
                  mycursor.callproc ( 'newCentros', [ nomNew, direcNew , telNew] )
                  self.miConexion.commit()
                  
                  print("El centro ha sido creado..!!")
                  mycursor.close()
              except Exception as miError :
                     print('Fallo ejecutando el procedimiento')
                     print(miError)
                     
                     
    def eliminarCentro(self):
        nomDel = input("Digite el nombre del centro a eliminar: ")
        if self.existeNombre (nomDel ) == False :
            print ("El centro no existe, no se puede eliminar") 
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delCentros', [ nomDel ] )
                self.miConexion.commit()
                print ("El centro ha sido eliminado..!!")
                mycursor.close()
            except Exception as miError :
                print( 'Fallo ejecutando el procedimiento' )
                print( miError)
                
    def modificarCentro(self):
        nomOld = input('Digite nombre actual: ')
        if self.existeNombre(nomOld) == False :
            print ("El centro no existe")
        else :
            nomNew = input("Digite nuevo nombre del centro: ")
            if nomNew != nomOld and self.existeNombre(nomNew) == True:
                print("Ya existe un centro con ese nombre , No se puede modificar")
            else:
                direcNew = input ("Digite la nueva direccion del centro: ")
                telNew = input ("Digite el nuevo telefono del centro: ")
                try:
                    mycursor = self.miConexion.cursor()
                    mycursor.callproc('modCentros', [nomNew, direcNew, telNew, nomOld]) 
                    self.miConexion.commit()
                    print ("El centro ha sido modificado..!!")
                    mycursor.close ()
                except Exception as miError:
                    print("Fallo ejecutando")
                    print(miError)
                    
             
                
                 
                 
    def  buscarCentro(self):
         nomSearch = input ('Digite el nombre del centro:')
         if self.existeNombre (nomSearch) == False :
            print ("El centro no existe")
         else :
             try:
                 mycursor = self.miConexion.cursor()
                 mycursor. callproc('getCentros', [nomSearch])
                 for result in mycursor.stored_results():
                     for (Nombre, Direccion, Telefono) in result:
                        elCentro = Centros(Nombre,Direccion,Telefono)
                        print (elCentro.toString())
                 mycursor.close()
             except Exception as miError :
                print ('Fallo ejecutando el procedimiento')
                print (miError)

                    
                 
             
             
         

           
                
            

              
                  
      
                
                
            
        