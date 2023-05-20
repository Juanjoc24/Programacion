from Conex.conexionparcial import Conexionpar
from Admons.AdmonActividades import AdmonActiv
from Admons.AdmonAdultos import AdmonAdul
from Admons.AdmonCategorias import AdmonCateg
from Admons.AdmonCentros import AdmonCentr
from Admons.AdmonConsultas import AdmonConsul
from Admons.AdmonInscripciones import AdmonInscrip

 

class Entrada:
    #Constuctor
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
            print("1: ACTIVIDADES")
            print("2: ADULTOS")
            print("3: CATEGORIAS")
            print("4: CENTROS")
            print("5: INSCRIPCIONES")
            print("6: CONSULTAS")
            
            opcion=int(input("digite opcion:"))
            if opcion ==0:
                self.con.desconectar()
                print("Se cierra conexion bye :)")
            elif opcion==1:
                AdmonActiv()
            elif opcion==2:
                AdmonAdul()
            elif opcion ==3:
                AdmonCateg()
            elif opcion==4:
                AdmonCentr()
            elif opcion==5:
                AdmonInscrip()
            elif opcion==6:
                AdmonConsul()
Entrada()

 

    
