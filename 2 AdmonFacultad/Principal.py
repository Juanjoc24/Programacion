import sys
from PyQt6.QtWidgets import QMainWindow,QApplication

from Admon.AdmonFuentes import AdmonFuentes
from Diseno.DPrincipal import Ui_MainWindow
from Admon.AdmonProyectos import AdmonProyectos

class Principal (QMainWindow):
	
    def __init__(self):
        super(Principal,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.BFuente.clicked.connect(self.fuente)
        self.ui.BTerminar.clicked.connect(self.terminar)
        self.ui.BProyecto.clicked.connect(self.proyectos)
    def fuente(self):
        print("Se llama a Fuente")
        self.ventanaFuente = AdmonFuentes () #Dispara fuente
        self.ventanaFuente.show ()
    
    def proyectos(self):
        print("Se llama a proyectos")
        self.ventanaProyectos=AdmonProyectos()
        self.ventanaProyectos.show()
    
    def terminar(self):
        self.close()



if __name__ == '__main__':
	app =QApplication([])
	ventanaPrincipal = Principal()
	ventanaPrincipal.show()
	sys.exit(app.exec())


