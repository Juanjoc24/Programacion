class Inscripciones:
    #constructor
    def __init__(self, idAdulNew,idActNew,calNew):
        #atributos  
        self.idAdul=idAdulNew
        self.idAct=idActNew
        self.cal=calNew
        
    
        
        
    #analizadores
    def getIdAdul(self):
        return self.idAdul
    def getIdAct(self):
        return self.idAct
    def getCal(self):
        return self.cal
    

    
    def toString (self):
        return("ID Adulto:",self.idAdul,
               "id actividad",self.idAct,
               "calificacion:", self.cal)
