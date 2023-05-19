
class Proyecto:
    #constructor
    def __init__(self, codigoNew, nombreNew, presupNew, fechaNew, codigoLidNew):
        #atributos
        self.codigo=codigoNew
        self.nombre=nombreNew
        self.presup=presupNew
        self.fecha=fechaNew
        self.codigoLid=codigoLidNew
        
    #analizadores  
    def getCodigo(self):
        return self.codigo
    def getNombre(self):
        return self.nombre
    def getFecha(self):
        return self.fecha
    def getPresup(self):
        return self.presup
    def getCodigoLid(self):
        return self.codigoLid
    
   
    #modificadores
    def setCodigo(self, codigoNew):
        self.codigo=codigoNew  
    def setNombre(self, nombreNew):
        self.nombre=nombreNew
    def setPresup(self, presupNew):
        self.presup=presupNew
    def setFecha(self,fechaNew):
        self.fecha=fechaNew
    def setCodigoLid(self,codigoLidNew):
        self.codigoLid=codigoLidNew
      
        
    def toString (self):
        return ("Codigo=",self.codigo,"nombre=", self.nombre,"Fecha inicio=",self.fecha,"Presupuesto", self.presup,
                "Codigo Lider", self.codigoLid)
