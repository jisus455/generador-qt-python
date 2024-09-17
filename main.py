from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog

from presentation.program import Ui_MainWindow
from presentation.dialog import Ui_Dialog

from business.cuilLogic import cuilCalculator
from business.exportLogic import exportFile

class MyMain(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMain, self).__init__(parent)
        self.setupUi(self)

        self.cmbGenero.addItem('Masculino', 'M')
        self.cmbGenero.addItem('Femenino', 'F')

        self.btnGenerar.clicked.connect(self.generar)
        self.actionExportar.triggered.connect(self.ejecutar)
    
    
    def generar(self):
        genero = self.cmbGenero.currentData()
        dni = self.leDni.text()
        mycuil = cuilCalculator(dni, genero)
        try:
            mycuil.validate()
            resultado = mycuil.calculate()
            self.txtCuil.setText(resultado)
        except Exception as e:
            self.txtCuil.setText(e.args[0])

    def ejecutar(self):
        dialog = MyDialog()
        dialog.exec()

        
class MyDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.setupUi(self)

        self.btnExportar.clicked.connect(self.exportar)

    def exportar(self):
        file = exportFile('M', '12345678', '999')
        file.export()
        


# Inicializar la aplicacion
app = QApplication([])
window = MyMain()
window.show()
app.exec()