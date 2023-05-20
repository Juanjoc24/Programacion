
class Adultos:
    #constructor
    def __init__(self, idAdulNew,nomNew,apellNew,nacinew,pesoNew,altNew,contacNew,centroNew):
        #atributos
        self.idAdul=idAdulNew   
        self.nom=nomNew
        self.apell=apellNew
        self.naci=nacinew
        self.peso=pesoNew
        self.alt=altNew
        self.contac=contacNew
        self.centro=centroNew
        
        
    #analizadores
    def getIdadul(self):
        return self.idAdul
    def getNombre(self):
        return self.nom
    def getApellido(self):
        return self.apell
    def getNacimiento(self):
        return self.naci
    def getPeso(self):
        return self.peso
    def getAltura(self):
        return self.alt
    def getContacto(self):
        return self.contac
    def getCenro(self):
        return self.centro

    
    def toString (self):
        return("id adulto", self.idAdul, "Nombre",self.nom,"Apellido",self.apell,
               "Nacimiento",self.naci,"Peso",self.peso,"Altura",self.alt,"Conacto",self.contac,
               "Centro",self.centro)
