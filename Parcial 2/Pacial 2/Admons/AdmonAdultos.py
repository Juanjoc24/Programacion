
from Conex.conexionparcial import Conexionpar
from Modelos.Adultos import Adultos

class AdmonAdul:
    
    def __init__(self):
        self.con=Conexionpar()
        self.miConexion=self.con.conectar()
        print("objeto tipo Administracion aultos creado y listo")
        
        self.menu()
        
    def menu(self):
        opcion=-1
        while opcion != 0:
            print("=========OPCIONES========")
            print("0: Salir")
            print("1: Nuevo adulto")
            print("2: Ver todas los adultos")
            print("3: Buscar adultos")
            print("4: Eliminar adultos")
            print("5: Modificar adultos")
            
            opcion=int(input("digite opcion:"))
            if opcion ==0:
                self.con.desconectar()
                print("Se cierra conexion bye :)")
            elif opcion==1:
                self.nuevoAdul()
            elif opcion==2:
                self.verTodos()
            elif opcion ==3:
                self.buscarAdul()
            elif opcion==4:
                self.eliminarAdul()
            elif opcion==5:
                self.modificarAdul()
                
    def verTodos (self):
        cant= 0
        try:
            mycursor=self.miConexion.cursor()
            mycursor.callproc("allAdult")
            
            for result in mycursor.stored_results():
                
                for(idAdulto,Nombre,Apellido,Nacimiento,Peso,Altura,Contacto,Centro) in result:
                    elAdulto=Adultos(idAdulto,Nombre,Apellido,Nacimiento,Peso,Altura,Contacto,Centro) 
                    print(elAdulto.toString())
                    cant= cant+1
            if cant==0:
                print ("No hay adultos registrados")
            
            mycursor.close()
        
        except Exception as miError:
            print ("Fallo ejecutando el procedimiento")
            print(miError)
            
    def existeIdAdul(self, IdAdulto):
         try:
             mycursor = self.miConexion.cursor ()
             query = "SELECT count(*) FROM adultos WHERE IdAdulto = %s;"
             mycursor. execute (query, [IdAdulto]) 
             resultados=mycursor.fetchall()
             for registro in resultados:
                 if registro[0] == 1 :
                    return True
                 return False
         except Exception as miError :
             print ('Fallo ejecutando el procedimiento')
             print(miError)
            

    def nuevoAdul(self) :
        idAdulNew = int(input('Digite el id del nuevo adulto:' )) 
        if self.existeIdAdul(idAdulNew) == True :
            print( "El aduloya ya existe no se puede repetir" )
        else :
            nomNew=input("escriba el nombre del adulto:")  
            apellNew = input( 'Digite el apellido del adulto:')
            naciNew = input("Agrege fecha(AAAA-MM-DD) de nacimiento:")
            pesoNew=input("Ingrese peso del adulto: ")
            altNew= input("Ingrese altura del adulto:")
            contacNew= input("Ingrese contacto del adulto:")
            centroNew= input("Ingrese cenro a donde va el adulto:")
            try:
                  mycursor = self.miConexion.cursor()
                  mycursor.callproc ('newAdult',[idAdulNew,nomNew,apellNew,naciNew,pesoNew,altNew,contacNew,centroNew])
                  self.miConexion.commit()
                  
                  print("El adulto ha sido creada.!!")
                  mycursor.close()
            except Exception as miError :
                     print('Fallo ejecutando el procedimiento')
                     print(miError)
                     
                     
    def eliminarAdul(self):
        idAdulDel = input("Digite el id del adulto a eliminar:")
        if self.existeIdAdul(idAdulDel) == False :
            print ("El adulto no existe, no se puede eliminar") 
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delAdult', [ idAdulDel ] )
                self.miConexion.commit()
                print ("el adulto ha sido eliminada..!!")
                mycursor.close()
            except Exception as miError :
                print( 'Fallo ejecutando el procedimiento' )
                print( miError)
                
    def modificarAdul(self):
        idAdulOld = input('Digite id actual:')
        if self.existeIdAdul(idAdulOld) == False :
            print ("el adulto no existe")
        else :
            idAdulNew = input("Digite nuevo id del adulto: ")
            if idAdulNew != idAdulOld and self.existeIdAdul(idAdulNew) == True:
                print("Ya existe un adulto con ese ID, No se puede modificar")
            else:
                nomNew=input("escriba el nombre del adulto")  
                apellNew = input( 'Digite el apellido del adulto:')
                naciNew = input("Agrege fecha(AAAA-MM-DD) de nacimiento:")
                pesoNew=input("Ingrese peso del adulto: ")
                altNew= input("Ingrese altura del adulto")
                contacNew= input("Ingrese contacto del adulto")
                centroNew= input("Ingrese centro a donde va el adulto")
                try:
                    mycursor = self.miConexion.cursor()
                    mycursor.callproc('modAdult', [idAdulNew,nomNew,apellNew,naciNew,pesoNew,altNew,contacNew,centroNew,idAdulOld]) 
                    self.miConexion.commit()
                    print ("El adulto ha sido modificada..!!")
                    mycursor.close ()
                except Exception as miError:
                    print("Fallo ejecutando")
                    print(miError)
                    
             
                
                 
                 
    def  buscarAdul(self):
         idAdulSearch = input('Digite el id del adulto:')
         
         if self.existeIdAdul(idAdulSearch) == False :
            print ("El adulto no existe")
         else :
             try:
                 mycursor = self.miConexion.cursor()
                 mycursor. callproc('getAdult', [idAdulSearch])
                 for result in mycursor.stored_results():
                     for (IdAdulto,Nombre,Apellido,Nacimiento,Peso,Altura,Contacto,Centro) in result:
                         elAdulto = Adultos(IdAdulto,Nombre,Apellido,Nacimiento,Peso,Altura,Contacto,Centro)
                         print (elAdulto.toString())
                 mycursor.close()
             except Exception as miError :
                print ('Fallo ejecutando el procedimiento')
                print (miError)
                                