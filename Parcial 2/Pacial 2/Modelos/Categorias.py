
class Categorias:
    #constructor
    def __init__(self, idCategNew,nomNew):
        #atributos  
        self.idCateg=idCategNew
        self.nom=nomNew
        
    
        
        
    #analizadores
    def getIdCateg(self):
        return self.idCat
    def getNombre(self):
        return self.nom
    

    
    def toString (self):
        return("ID Categoria:",self.idCateg,
               "Nombre:",self.nom)


