from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt6.QtGui import QIcon

from presentation.program import Ui_MainWindow
from presentation.dialog import Ui_Dialog

from business.cuilLogic import cuilCalculator
from business.exportLogic import exportFile

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
        self.actionExportar.triggered.connect(self.ejecutar)
        self.actionExportar.setStatusTip("Exportar los datos en un archivo")


    def generar(self):
        self.genero = self.cmbGenero.currentData()
        self.dni = self.txtDni.text()
        if self.genero and self.dni:
            mycuil = cuilCalculator(self.dni, self.genero)
            try:
                mycuil.validate()
                self.cuil = mycuil.calculate()
                self.txtCuil.setText(self.cuil)
                self.statusbar.showMessage("Cuil generado correctamente", 5000)
            except Exception as e:
                QMessageBox().critical(self, 'Atencion', str(e.args[0]))
        else:
            QMessageBox().information(self, 'Atencion', 'Debe completar todos los campos')


    def ejecutar(self):
        if not self.cuil:
            QMessageBox().warning(self, 'Atencion', 'No hay datos para exportar')
        else:
            dialog = MyDialog()
            result = dialog.exec()
        
            if result == 0:
                self.statusbar.showMessage("Operacion exportar cancelada", 5000)
            
            if result == 1:
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

        self.btnNueva.setIcon(QIcon('./assets/icon/carpeta.png'))
        self.btnDescargas.setIcon(QIcon('./assets/icon/carpeta.png'))
        self.btnDocumentos.setIcon(QIcon('./assets/icon/carpeta.png'))
        self.btnEscritorio.setIcon(QIcon('./assets/icon/carpeta.png'))

        self.data = {}
        self.btnAceptar.clicked.connect(self.aceptar)
        self.btnCancelar.clicked.connect(lambda: self.close())

        self.btnNueva.clicked.connect(self.nueva)
        self.btnDescargas.clicked.connect(self.descargas)
        self.btnDocumentos.clicked.connect(self.documentos)
        self.btnEscritorio.clicked.connect(self.escritorio)

    def aceptar(self):
        if self.txtRuta.text():
            self.data.setdefault('ruta', self.txtRuta.text())
            self.done(1)

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