
class Actividades:
    #constructor
    def __init__(self, idActivNew,nomNew,descripNew,fechaNew,idCatNew,centrNew):
        #atributos
        self.idActiv=idActivNew   
        self.nom=nomNew
        self.descrip=descripNew
        self.fecha=fechaNew
        self.idCat=idCatNew
        self.centr=centrNew
        
        
    #analizadores
    def getIdAct(self):
        return self.idActiv
    def getNombre(self):
        return self.nom
    def getDescrip(self):
        return self.descrip
    def getFecha(self):
        return self.fecha
    def getIdCat(self):
        return self.idCat
    def getCentr(self):
        return self.centr
    

    
    def toString (self):
        return("ID Actividad:",self.idActiv,"Nombre:",self.nom,
               "Descripcion:",self.descrip,"Fecha:",self.fecha,
               "ID Categoria:",self.idCat,"Centro:",self.centr)

