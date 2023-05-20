
class Centros:
    #constructor
    def __init__(self, NombreNew,direcNew,telNew):
        #atributos
        self.Nombre=NombreNew   
        self.direccion=direcNew
        self.telefono=telNew
        
        
    #analizadores
    def getNombre(self):
        return self.Nombre
    def getDireccion(self):
        return self.direccion
    def getTelefono(self):
        return self.telefono
    

    
    def toString (self):
        return("Nombre centro:",self.Nombre,"Direccion:",self.direccion,
               "Telefono:",self.telefono)
        