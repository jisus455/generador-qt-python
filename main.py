from PyQt6.QtWidgets import QApplication, QMainWindow
from presentation.program import Ui_MainWindow
from business.cuilLogic import cuilCalculator

class MyMain(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMain, self).__init__(parent)
        self.setupUi(self)

        self.cmbGenero.addItem('Masculino', 'M')
        self.cmbGenero.addItem('Femenino', 'F')
        self.btnGenerar.clicked.connect(self.generar)
    
    
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


# Inicializar la aplicacion
app = QApplication([])
window = MyMain()
window.show()
app.exec()