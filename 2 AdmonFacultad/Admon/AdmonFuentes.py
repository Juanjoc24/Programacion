
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication,QMessageBox,QTableWidgetItem

from Modelo.Fuente import Fuente
from Conex.Conexion import Conexion
from Diseno.DFuentes import Ui_MainWindow


class AdmonFuentes(QMainWindow):

    def __init__(self):
        super(AdmonFuentes,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.objConexion=Conexion()
        
        
        self.miConexion = self.objConexion.conectar ()
        print('Objeto tipo AdmonFuentes creado y listo para usarse..!!')
        
        self.ui.PBTodas.clicked.connect(self.verTodas)
        self.ui.PBEliminar.clicked.connect(self.eliminaFuente)
        self.ui.PBSalir.clicked.connect(self.cerrarConexion)
        self.ui.PBBuscar.clicked.connect(self.buscarFuente)
        self.ui.PBModificar.clicked.connect(self.modFuente)
        self.ui.PBNuevo.clicked.connect(self.agregaFuente)
        
    def cerrarConexion(self):
        self.close()
        



    def verTodas(self):
        cant = 0
        try :
            mycursor = self.miConexion.cursor ()
            mycursor.callproc ( 'allFuentes')
            
            #Limpiar la TAbla
            a=self.ui.TWTabla.rowCount()
            for rep in range(a):
                self.ui.TWTabla.removeRow(0)

    
            for result in mycursor.stored_results ():
                for (idFuente, nombre, contacto) in result :
                    self.ui.TWTabla.insertRow(cant)
                    
                    
                    celdaCodigo=QTableWidgetItem(str(idFuente))
                    celdaNombre=QTableWidgetItem(nombre)
                    celdaContacto=QTableWidgetItem(contacto)
                    
                    self.ui.TWTabla.setItem(cant,0,celdaCodigo)
                    self.ui.TWTabla.setItem(cant,1,celdaNombre)
                    self.ui.TWTabla.setItem(cant,2,celdaContacto)
                    
                    cant = cant + 1
            if cant == 0 :
                QMessageBox.information(self,"Alerta en consulta","No hay fuentes registradas::!!")
                
            mycursor.close()
        except Exception as ex:
            QMessageBox.information(self, "Consulta Fallida"," No hay fuebtes registradas")
            print(ex)

    def buscarFuente(self):
        idFuenteSearch = self.ui.SBCodigoBuscar.value()
        
        a=self.ui.TWTabla.rowCount()
        for rep in range(a):
            self.ui.TWTabla.removeRow(0)
        
        if self.existeIdFuente(idFuenteSearch) == False :
            QMessageBox.information(self,"Busqueda fallida","La fuente no existe, no se puede buscar")
        else :
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getFuente', [idFuenteSearch])
                self.miConexion.commit()
                for result in mycursor.stored_results ():
                    for (idFuente, nombre, contacto) in result :
                        self.ui.TWTabla.insertRow(0)
                        
                        
                        celdaCodigo=QTableWidgetItem(str(idFuente))
                        celdaNombre=QTableWidgetItem(nombre)
                        celdaContacto=QTableWidgetItem(contacto)
                        
                        self.ui.TWTabla.setItem(0, 0,celdaCodigo)
                        self.ui.TWTabla.setItem(0, 1,celdaNombre)
                        self.ui.TWTabla.setItem(0, 2,celdaContacto)
    
    
                mycursor.close()
    
            except Exception as miError :
                print('Fallo ejecutando el procedimiento')
                print(miError)





    def modFuente(self):
        idFuenteOld=self.ui.SBCodigoMod.value()
        if self.existeIdFuente ( idFuenteOld) == False :
            QMessageBox.information(self,"Modificacion fallida","La fuente no existe, no se puede modificar")
        else:
            idFuenteNew=self.ui.SBCodigoModNew.value()
            if idFuenteNew != idFuenteOld and self.existeIdFuente(idFuenteNew)== True:
                QMessageBox.information(self,"Error","Ya existe una fuente con este id , no se puede modificar")
            else:
                nombreModNew=self.ui.LENombreMod.text()
                if nombreModNew=="":
                    QMessageBox.warning(self, "Error", "No agrego nombre")
                    
                contactoModNew=self.ui.LEContacMod.text()
                if contactoModNew=="":
                    QMessageBox.warning(self, "Error", "No agrego contacto")
                else:
                    try:
                        mycursor = self.miConexion.cursor()
                        mycursor.callproc('modFuente', [idFuenteNew, nombreModNew,contactoModNew,idFuenteOld])
                        self.miConexion.commit()
                        QMessageBox.information(self,"Modificacion exitosa","La fuente fue modificada!!")
                    except Exception as miError :
                        print('Fallo ejecutando el procedimiento')
                        print(miError)
                    
                
                
    def agregaFuente(self):
        idFuenteNew=self.ui.SBCodigoNew.value()
        
        if self.existeIdFuente(idFuenteNew)==True:
            QMessageBox.warning(self, "Error", "Ya existe este id no se puede agregar fuente")
        
        else:
            nombreNew=self.ui.LENombreNew.text()
            if nombreNew=="":
                QMessageBox.warning(self, "Error", "No agrego nombre")
                
                
            contactoNew=self.ui.LEContacNew.text()
            if contactoNew=="":
                QMessageBox.warning(self, "Error", "No agrego contacto")
            else:
                try:
                    mycursor = self.miConexion.cursor()
                    mycursor.callproc('newFuente', [idFuenteNew, nombreNew,contactoNew])
                    self.miConexion.commit()
                    QMessageBox.information(self," Agregado exitosamente","La fuente fue agregada!!")
                except Exception as miError :
                    print('Fallo ejecutando el procedimiento')
                    print(miError)
                    
            
            



    def eliminaFuente(self):

        idFuenteDel =self.ui.SBCodigoEliminar.value()
        if self.existeIdFuente ( idFuenteDel ) == False :
            QMessageBox.information(self,"Eliminacion fallida","La fuente no existe, no se puede eliminar")
            
        else :
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delFuente' , [ idFuenteDel ] )
                self.miConexion.commit()
                QMessageBox.information(self, "Eliminacion exitosa",'La fuente ha sido eliminada..!!')

                mycursor.close()
            except Exception as miError :
                QMessageBox.information(self,"Eliminacion Fallida",'Fallo ejecutando el procedimiento')
                
                print(miError)

    def existeIdFuente (self,idFuente):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM FUENTES WHERE idFuente = %s"
            mycursor.execute(query, [idFuente])      
            resultados=mycursor.fetchall()
            for registro in resultados:
                if  registro[0] == 1 :
                    return True
                return False
        except Exception as miError:
            print('Fallo ejecutando el procedimiento')
            print(miError)
          

if __name__ == '__main__':
    app =QApplication([])
    ventanaAdmonFuentes = AdmonFuentes()
    ventanaAdmonFuentes.show()
    sys.exit(app.exec())
    
	           

