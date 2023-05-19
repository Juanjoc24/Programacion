class Fuente:

    #Constructor
    def __init__(self,idFuenteNew,nombreNew,contactoNew):
        self.idFuente=idFuenteNew
        self.nombre=nombreNew
        self.contacto=contactoNew

    #Modificadores
    def setIdFuente(self,idFuenteNew):
        self.idFuente=idFuenteNew

    def setNombre(self,nombreNew):
        self.nombre=nombreNew

    def setContacto(self,contactoNew):
        self.contacto=contactoNew

    #Analizadores
    def getIdFuente(self):
        return self.idFuente

    def getNombre(self):
        return self.nombre

    def getContacto(self):
        return self.contacto

    
    #toString
    def toString(self):
        return "Fuente ID =", self.idFuente, "Nombre = ", self.nombre,"Contacto =" , self.contacto