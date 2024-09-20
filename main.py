from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog

from presentation.program import Ui_MainWindow
from presentation.dialog import Ui_Dialog

from business.cuilLogic import cuilCalculator
from business.exportLogic import exportFile

import os
import os.path

class MyMain(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMain, self).__init__(parent)
        self.setupUi(self)

        self.genero = None
        self.dni = None
        self.cuil = None

        self.cmbGenero.addItem('Masculino', 'M')
        self.cmbGenero.addItem('Femenino', 'F')

        self.btnGenerar.clicked.connect(self.generar)
        
        self.actionExportar.setStatusTip("Exportar los datos en un archivo")
        self.actionExportar.triggered.connect(self.ejecutar)

    
    
    def generar(self):
        self.genero = self.cmbGenero.currentData()
        self.dni = self.leDni.text()
        mycuil = cuilCalculator(self.dni, self.genero)
        try:
            mycuil.validate()
            self.cuil = mycuil.calculate()
            self.txtCuil.setText(self.cuil)
        except Exception as e:
            self.txtCuil.setText(e.args[0])

    def ejecutar(self):
        dialog = MyDialog()
        dialog.exec()
         
        ruta = dialog.data['ruta']
        data = {'genero': self.genero, 'dni': self.dni, 'cuil': self.cuil}
        result = exportFile().export(ruta, data)
        if result:
            self.statusbar.showMessage("Archivo exportado correctamente", 5000)
        else:
            self.statusbar.showMessage("Ocurrio un problema al exportar", 5000)


        
class MyDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.setupUi(self)

        self.data = {}
        self.ruta = os.getcwd()
        self.btnAceptar.clicked.connect(self.aceptar)
        self.btnCancelar.clicked.connect(lambda: self.close())

        self.btnNueva.clicked.connect(self.nueva)
        self.btnDescargas.clicked.connect(self.descargas)
        self.btnDocumentos.clicked.connect(self.documentos)
        self.btnEscritorio.clicked.connect(self.escritorio)

    def aceptar(self):
        self.data.setdefault('ruta', self.txtRuta.text())
        self.close()
    
    def nueva(self):
        ruta = exportFile().getRoute('newdir')
        self.txtRuta.setText(ruta)
    
    def descargas(self):
        ruta = exportFile().getRoute('downloads')
        self.txtRuta.setText(ruta)

    def documentos(self):
        ruta = exportFile().getRoute('documents')
        self.txtRuta.setText(ruta)

    def escritorio(self):
        ruta = exportFile().getRoute('desktop')
        self.txtRuta.setText(ruta)


# Inicializar la aplicacion
app = QApplication([])
window = MyMain()
window.show()
app.exec()