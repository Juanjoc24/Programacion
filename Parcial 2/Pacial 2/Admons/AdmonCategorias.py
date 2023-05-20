
from Conex.conexionparcial import Conexionpar
from Modelos.Categorias import Categorias

class AdmonCateg:
    
    def __init__(self):
        self.con=Conexionpar()
        self.miConexion=self.con.conectar()
        print("objeto tipo Administracion categorias creado y listo")
        
        self.menu()
        
    def menu(self):
        opcion=-1
        while opcion != 0:
            print("=========OPCIONES========")
            print("0: Salir")
            print("1: Nueva categoria")
            print("2: Ver todas las categorias")
            print("3: Buscar categoria")
            print("4: Eliminar categoria")
            print("5: Modificar categoria")
            
            opcion=int(input("digite opcion:"))
            if opcion ==0:
                self.con.desconectar()
                print("Se cierra conexion bye :)")
            elif opcion==1:
                self.nuevaCateg()
            elif opcion==2:
                self.verTodos()
            elif opcion ==3:
                self.buscarCateg()
            elif opcion==4:
                self.eliminarCateg()
            elif opcion==5:
                self.modificarCateg()
                
    def verTodos (self):
        cant= 0
        try:
            mycursor=self.miConexion.cursor()
            mycursor.callproc("allCateg")
            
            for result in mycursor.stored_results():
                
                for(idCategoria,Nombre) in result:
                    laCateg=Categorias(idCategoria,Nombre)
                    print(laCateg.toString())
                    cant= cant+1
            if cant==0:
                print ("No hay categorias registradas")
            
            mycursor.close()
        
        except Exception as miError:
            print ("Fallo ejecutando el procedimiento")
            print(miError)
            
    def existeIdCateg(self, IdCategoria):
         try:
             mycursor = self.miConexion.cursor ()
             query = "SELECT count(*) FROM categorias WHERE IdCategoria = %s;"
             mycursor. execute (query, [IdCategoria]) 
             resultados=mycursor.fetchall()
             for registro in resultados:
                 if registro[0] == 1 :
                    return True
                 return False
         except Exception as miError :
             print ('Fallo ejecutando el procedimiento')
             print(miError)
            
    def nuevaCateg(self) :
        idCategNew = int(input('Digite el id de la nueva categoria:' )) 
        if self.existeIdCateg(idCategNew) == True :
            print( "La categoria ya existe no se puede repetir" )
        else :
            nomNew = input( 'Digite el nombre de la categoria:')
            try:
                  mycursor = self.miConexion.cursor()
                  mycursor.callproc ('newCateg',[idCategNew,nomNew])#orden proceso
                  self.miConexion.commit()
                  
                  print("La categoria ha sido creada.!!")
                  mycursor.close()
            except Exception as miError :
                     print('Fallo ejecutando el procedimiento')
                     print(miError)
                     
                     
    def eliminarCateg(self):
        idCategDel= int(input("Digite el id de la categoria a eliminar:"))
        if self.existeIdCateg(idCategDel) == False :
            print ("La categoria no existe, no se puede eliminar") 
        else:
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delCateg', [ idCategDel ] )
                self.miConexion.commit()
                print ("la categoria ha sido eliminada..!!")
                mycursor.close()
            except Exception as miError :
                print( 'Fallo ejecutando el procedimiento' )
                print( miError)
                
    def modificarCateg(self):
        idCategOld = int(input('Digite id actual:'))
        if self.existeIdCateg(idCategOld) == False :
            print ("La categoria no existe")
        else :
            idCategNew = int(input("Digite nuevo id de la Categoria: "))
            if idCategNew != idCategOld and self.existeIdCateg(idCategNew) == True:
                print("Ya existe una categoria con ese ID, No se puede modificar")
            else:
                nomNew = input( 'Digite el nombre de la categoria:')
                try:
                    mycursor = self.miConexion.cursor()
                    mycursor.callproc('modCat',[idCategNew,nomNew,idCategOld]) #orden proceso
                    self.miConexion.commit()
                    print ("La categoria ha sido modificada..!!")
                    mycursor.close ()
                except Exception as miError:
                    print("Fallo ejecutando")
                    print(miError)
                    
             
                
                 
                 
    def  buscarCateg(self):
         idCategSearch =int(input('Digite el id de la categoria:'))
         
         if self.existeIdCateg(idCategSearch) == False :
            print ("La categoria no existe")
         else :
             try:
                 mycursor = self.miConexion.cursor()
                 mycursor. callproc('getCateg', [idCategSearch])
                 for result in mycursor.stored_results():
                     for (IdCategoria,Nombre) in result:#como la tabla
                         laCategoria = Categorias(IdCategoria,Nombre)
                         print (laCategoria.toString())
                 mycursor.close()
             except Exception as miError :
                print ('Fallo ejecutando el procedimiento')
                print (miError)

