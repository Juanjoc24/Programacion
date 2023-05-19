
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication,QMessageBox,QTableWidgetItem

from Modelo.Proyectos import Proyecto
from Conex.Conexion import Conexion
from Diseno.DProyectos import Ui_MainWindow


class AdmonProyectos(QMainWindow):
    
    def __init__(self):
        super(AdmonProyectos,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.objConexion=Conexion()
        self.miConexion=self.objConexion.conectar()
        print("Objeto tipo AdmonProyectos creado y listo para usarse!!!")
        
        self.ui.PBTodasProy.clicked.connect(self.verTodas)
        self.ui.PBSalirProy.clicked.connect(self.cerrarConexion)
        self.ui.PBBuscar.clicked.connect(self.buscarProyecto)
        self.ui.PBModificarProy.clicked.connect(self.modProyecto)
        self.ui.PBNuevoProy.clicked.connect(self.agregaFuente)
        self.ui.PBEliminarProy.clicked.connect(self.eliminaProyecto)
        
        
        
        
        
    def cerrarConexion(self):
        self.close()    
        
        
    def verTodas(self):
        cant=0
        try:
            mycursor=self.miConexion.cursor()
            mycursor.callproc('allProyectos')
            
            a=self.ui.TWTabla.rowCount()
            for rep in range(a):
                self.ui.TWTabla.removeRow(0)
            
            for result in mycursor.stored_results():
                for(codigo,nombre,presup,fecha, codigoLid)in result:
                    self.ui.TWTabla.insertRow(cant)
                    
                    celdaCodigo=QTableWidgetItem(str(codigo))
                    celdaNombre=QTableWidgetItem(nombre)
                    celdaPresup=QTableWidgetItem(str(presup))
                    celdaFecha=QTableWidgetItem(str(fecha))
                    celdaLider=QTableWidgetItem(str(codigoLid))
                    
                    self.ui.TWTabla.setItem(cant,0,celdaCodigo)
                    self.ui.TWTabla.setItem(cant,1,celdaNombre)
                    self.ui.TWTabla.setItem(cant,2,celdaPresup)
                    self.ui.TWTabla.setItem(cant,3,celdaFecha)
                    self.ui.TWTabla.setItem(cant,4,celdaLider)
                    
                    cant=cant+1
                    
            if cant==0:
                QMessageBox.warning(self,"Alerta consulta","No hay proyectos registradas")
                
            mycursor.close()
            
        except Exception as ex:
            QMessageBox.warning(self,"Consulta Fallida","Fallo ejecutando el procedimiento de consulta de proyectos")
            
            print(ex)
                
    def buscarProyecto(self):
        idProyectoSearch = self.ui.SBCodigoBuscar.value()
        
        
        a=self.ui.TWTabla.rowCount()
        for rep in range(a):
            self.ui.TWTabla.removeRow(0)
        
        if self.existeIdProyecto(idProyectoSearch) == False :
            QMessageBox.information(self,"Busqueda fallida","El proyecto no existe, no se puede buscar")
        else :
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('getProyecto', [idProyectoSearch])
                self.miConexion.commit()
                for result in mycursor.stored_results ():
                    for (codigo,nombre,presup,fecha, codigoLid) in result :
                        self.ui.TWTabla.insertRow(0)
                        
                        
                        celdaCodigo=QTableWidgetItem(str(codigo))
                        celdaNombre=QTableWidgetItem(nombre)
                        celdaPresup=QTableWidgetItem(str(presup))
                        celdaFecha=QTableWidgetItem(str(fecha))
                        celdaLider=QTableWidgetItem(str(codigoLid))
                        
                        self.ui.TWTabla.setItem(0,0,celdaCodigo)
                        self.ui.TWTabla.setItem(0,1,celdaNombre)
                        self.ui.TWTabla.setItem(0,2,celdaPresup)
                        self.ui.TWTabla.setItem(0,3,celdaFecha)
                        self.ui.TWTabla.setItem(0,4,celdaLider)
    
    
                mycursor.close()
    
            except Exception as miError :
                print('Fallo ejecutando el procedimiento')
                print(miError)
                
                
                
                
    def modProyecto(self):
        idProyectoOld=self.ui.SBCodigoMod.value()
        if self.existeIdProyecto (idProyectoOld) == False :
            QMessageBox.information(self,"Modificacion fallida","El proyecto no existe, no se puede modificar")
        else:
            idProyectoNew=self.ui.SBCodigoModNew.value()
            fechainicioModNew=self.ui.DEFechaMod.text()
            if idProyectoNew != idProyectoOld and self.existeIdProyecto(idProyectoNew)== True:
                QMessageBox.information(self,"Error","Ya existe un proyecto con este id , no se puede modificar")
            else:
                nombreModNew=self.ui.LENombreMod.text()
                if nombreModNew=="":
                    QMessageBox.warning(self, "Error", "No agrego nombre")
                    
                presupuestoModNew=self.ui.LEPresupuestoMod.text()
                if presupuestoModNew=="":
                    QMessageBox.warning(self, "Error", "No agrego presupuesto")
            
                
                liderModNew=self.ui.SBLiderMod.value()
                if liderModNew=="":
                    QMessageBox.warning(self,"Error","No agrego codigo del lider ")
                    
                else:
                    try:
                        mycursor = self.miConexion.cursor()
                        mycursor.callproc('modProyecto', [idProyectoNew, nombreModNew,presupuestoModNew, fechainicioModNew, liderModNew  ,idProyectoOld])
                        self.miConexion.commit()
                        QMessageBox.information(self,"Modificacion exitosa","El proyecto fue modificado!!")
                    except Exception as miError :
                        print('Fallo ejecutando el procedimiento')
                        print(miError)    
                
    def eliminaProyecto(self):
        idProyectoDel =self.ui.SBCodigoEliminar.value()
        if self.existeIdProyecto ( idProyectoDel ) == False :
            QMessageBox.information(self,"Eliminacion fallida","El proyecto no existe, no se puede eliminar")
            
        else :
            try:
                mycursor = self.miConexion.cursor()
                mycursor.callproc('delProyecto' , [ idProyectoDel ] )
                self.miConexion.commit()
                QMessageBox.information(self, "Eliminacion exitosa",'La fuente ha sido eliminada..!!')

                mycursor.close()
            except Exception as miError :
                QMessageBox.information(self,"Eliminacion Fallida",'Fallo ejecutando el procedimiento')
                
                print(miError)           
               
               
               

                     
                
                
    


    def agregaFuente(self):
        idProyectoNew=self.ui.SBCodigoNew.value()
        fechainicioNew=self.ui.DEFechaNew.text()
        
        if self.existeIdProyecto(idProyectoNew)==True:
            QMessageBox.warning(self, "Error", "Ya existe este id no se puede agregar fuente")
        
        else:
            nombreNew=self.ui.LENombreNew.text()
            if nombreNew=="":
                QMessageBox.warning(self, "Error", "No agrego nombre")
                
                
            presupuestoNew=self.ui.LEPresupuestoNew.text()
            if presupuestoNew=="":
                QMessageBox.warning(self, "Error", "No agrego presupuesto")
        
            
            liderNew=self.ui.SBLiderNew.value()
            if liderNew=="":
                QMessageBox.warning(self,"Error","No agrego codigo del lider ")
            else:
                try:
                    mycursor = self.miConexion.cursor()
                    mycursor.callproc('newProyecto', [idProyectoNew, nombreNew,presupuestoNew, fechainicioNew, liderNew])
                    self.miConexion.commit()
                    QMessageBox.information(self," Agregado exitosamente","El proyecto fue agregada!!")
                except Exception as miError :
                    QMessageBox.warning(self,"Error",'Fallo ejecutando el procedimiento')
                    print(miError)
                    
                    
    def existeIdProyecto (self,idProyecto):
        try :
            mycursor = self.miConexion.cursor ()
            query = "SELECT count(*) FROM PROYECTOS WHERE idProyecto = %s"
            mycursor.execute(query, [idProyecto])      
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
    ventanaAdmonProyectos = AdmonProyectos()
    ventanaAdmonProyectos.show()
    sys.exit(app.exec())        
    

    



        
        
        



    