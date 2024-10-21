import sys,os
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox, QLabel, QWidget, QPushButton
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.personalizarVentana()
        self.personalizarComponentes()

    def personalizarVentana(self):
        self.setWindowTitle("VENTANA PYQT5")  # Título para la ventana
        self.setFixedSize(480, 330)  # Tamaño de la ventana ancho y altura
        self.setStyleSheet("background-color: lightgray;")  # Color de fondo para la ventana

        # Cambiar el icono de la ventanapython9_ventana_menu_mihaita/cross1.png con una ruta absoluta que se crea a partir de una relativa
        ruta_relativa = "python12_combobox/cross1.png"
        ruta_absoluta = os.path.abspath(ruta_relativa)
        print(ruta_absoluta) # F:\CURSOS\TRABAJANDO\PROJECTS___PYTHON\PYTHON_TEXTO\PYTHON\PYTHON_0033\cross1.png
        self.setWindowIcon(QIcon(ruta_absoluta))

        self.pnlPrincipal = QWidget() # Crear un contenedor
        self.setCentralWidget(self.pnlPrincipal) # Establecer el contenedor como principal para nuestra ventana
      

    def personalizarComponentes(self):
        self.lblTitulo = QLabel("SELECCIONAR UNA CIUDAD DE UN COMBOBOX", self.pnlPrincipal)
        self.lblTitulo.setFont(QFont("Courier New", 9))
        self.lblTitulo.setAlignment(Qt.AlignCenter)
        self.lblTitulo.setGeometry(0, 0, 480, 20)
        self.lblTitulo.setStyleSheet("background-color: black; color: yellow;")
        
        self.lblCiudad = QLabel("SELECCIONE CIUDAD", self.pnlPrincipal)
        self.lblCiudad.setFont(QFont("Courier New", 9))
        self.lblCiudad.setAlignment(Qt.AlignCenter)
        self.lblCiudad.setGeometry(0, 80, 480, 20)

        self.cboCiudad = QComboBox(self.pnlPrincipal)
        self.cboCiudad.setFont(QFont("Courier New", 8))
        self.cboCiudad.setGeometry(157, 160, 165, 20)
        self.cboCiudad.addItem("SELECCIONE CIUDAD")
        self.cboCiudad.addItem("BARCELONA")
        self.cboCiudad.addItem("BILBAO")
        self.cboCiudad.addItem("MADRID")
        self.cboCiudad.addItem("SEVILLA")
        self.cboCiudad.addItem("ZARAGOZA")
        self.cboCiudad.currentIndexChanged.connect(self.itemSeleccionado)

        self.btoReiniciar = QPushButton(self.pnlPrincipal)
        self.btoReiniciar.setText("REINICIAR")
        self.btoReiniciar.setGeometry(150, 240, 80, 20)
        self.btoReiniciar.setFont(QFont("Courier New", 8))
        self.btoReiniciar.clicked.connect(self.reiniciar)

        self.btoSalir = QPushButton(self.pnlPrincipal)
        self.btoSalir.setText("SALIR")
        self.btoSalir.setGeometry(250, 240, 80, 20)
        self.btoSalir.setFont(QFont("Courier New", 8))
        self.btoSalir.clicked.connect(self.salir)
    
    def reiniciar(self):
        self.cboCiudad.setCurrentIndex(0)

    def salir(self):
        sys.exit()

    def itemSeleccionado(self, index):
        ciudad = self.cboCiudad.currentText()
        if ciudad == "MADRID":
            self.lblCiudad.setText("MADRID ES CAPITAL DEL REYNO DE ESPAÑA")
        elif ciudad == "BARCELONA":
            self.lblCiudad.setText("BARCELONA ES CAPITAL DE LA CA DE CATALUÑA")
        elif ciudad == "SEVILLA":
            self.lblCiudad.setText("SEVILLA ES CAPITAL DE LA CA DE ANDALUCIA")
        elif ciudad == "BILBAO":
            self.lblCiudad.setText("BILBAO ES CAPITAL DE LA CA DEL PAIS VASCO")
        elif ciudad == "ZARAGOZA":
            self.lblCiudad.setText("ZARAGOZA ES CAPITAL DE LA CA DE ARAGON")
        else:
            self.lblCiudad.setText("SELECCIONE CIUDAD")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())