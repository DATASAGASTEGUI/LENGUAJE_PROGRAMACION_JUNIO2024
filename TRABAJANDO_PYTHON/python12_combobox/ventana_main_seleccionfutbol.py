import sys,os,sqlite3
from PySide6.QtWidgets import (
    QVBoxLayout, QWidget,
    QApplication, QMainWindow, QComboBox, QLabel, QPushButton,
    QHBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem
)
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt
from herencia_seleccionfutbol import Futbolista, Entrenador, Masajista

def obtener_lista_seleccionfutbol_objeto():
    seleccionfutbol_lo = []
    conexion = obtener_conexion()
    if conexion != None:
       cursor = conexion.cursor()
       try:
          query_seleccionfutbol = "SELECT * FROM SeleccionFutbol" 
          cursor.execute(query_seleccionfutbol)
          seleccionfutbol_lt = cursor.fetchall()
          for seleccionfutbol_t in seleccionfutbol_lt:
              id_seleccionfutbol, nombre, apellidos, edad = seleccionfutbol_t

              cursor.execute('SELECT * FROM Futbolista WHERE id_futbolista = ?',(id_seleccionfutbol,))
              resultado_t = cursor.fetchone()
              if resultado_t:
                 id_futbolista, dorsal, demarcacion = resultado_t
                 seleccionfutbol_o = Futbolista(id_futbolista, nombre, apellidos, edad, dorsal, demarcacion)
                 seleccionfutbol_lo.append(seleccionfutbol_o)

              cursor.execute('SELECT * FROM Entrenador WHERE id_entrenador = ?',(id_seleccionfutbol,))
              resultado_t = cursor.fetchone()
              if resultado_t:
                 id_entrenador, id_federacion = resultado_t
                 seleccionfutbol_o = Entrenador(id_entrenador, nombre, apellidos, edad, id_federacion)
                 seleccionfutbol_lo.append(seleccionfutbol_o)

              cursor.execute('SELECT * FROM Masajista WHERE id_masajista = ?',(id_seleccionfutbol,))
              resultado_t = cursor.fetchone()
              if resultado_t:
                 id_masajista, titulacion, anio_experiencia = resultado_t
                 seleccionfutbol_o = Masajista(id_masajista, nombre, apellidos, edad, titulacion, anio_experiencia)
                 seleccionfutbol_lo.append(seleccionfutbol_o)
          print("OK: LISTA SELECCION FUTBOL")
          return seleccionfutbol_lo             
       except Exception as e:
          print("ERROR: SELECT ", e)
          return None
    else:
        print("ERROR: CONEXION")

def construir_tabla(cabecera,n,objeto):
        tblMostrar.setColumnCount(n)
        tblMostrar.setRowCount(0)
        tblMostrar.setHorizontalHeaderLabels(cabecera)
        tblMostrar.horizontalHeader().setStyleSheet("color: black; background-color: white;")
        tblMostrar.verticalHeader().setStyleSheet("color: black; background-color: white;")
        tblMostrar.horizontalHeader().setFont(QFont("Courier New", 18, QFont.Bold)) 
        tblMostrar.setFont(QFont("Courier New", 14)) 
        tblMostrar.insertRow(0) 
        tblMostrar.setItem(0, 0, QTableWidgetItem(objeto.id_seleccionfutbol)) 
        tblMostrar.setItem(0, 1, QTableWidgetItem(objeto.nombre))
        tblMostrar.setItem(0, 2, QTableWidgetItem(objeto.apellidos))
        tblMostrar.setItem(0, 3, QTableWidgetItem(str(objeto.edad)))
        if isinstance(objeto, Futbolista):
           tblMostrar.setItem(0, 4, QTableWidgetItem(objeto.dorsal))
           tblMostrar.setItem(0, 5, QTableWidgetItem(str(objeto.demarcacion)))
           tblMostrar.setItem(0, 6, QTableWidgetItem("FUTBOLISTA"))
        if isinstance(objeto, Masajista):
           tblMostrar.setItem(0, 4, QTableWidgetItem(objeto.titulacion))
           tblMostrar.setItem(0, 5, QTableWidgetItem(str(objeto.anio_experiencia)))
           tblMostrar.setItem(0, 6, QTableWidgetItem("MASAJISTA"))
        if isinstance(objeto, Entrenador):
           tblMostrar.setItem(0, 4, QTableWidgetItem(objeto.id_federacion))
           tblMostrar.setItem(0, 5, QTableWidgetItem("ENTRENADOR"))

def salir():
    sys.exit()

def cambiar_item():
    idSeleccionFutbol = cboIdSeleccionFutbol.currentText()
    if idSeleccionFutbol == "SELECCIONAR":
       reiniciar()
       return
    
    seleccionfutbol_lo = obtener_lista_seleccionfutbol_objeto()
    for objeto in seleccionfutbol_lo:
        if objeto.id_seleccionfutbol == idSeleccionFutbol:
            nombre = objeto.nombre
            apellidos = objeto.apellidos
            edad = objeto.edad
            if isinstance(objeto, Futbolista):
               dorsal = objeto.dorsal
               demarcacion = objeto.demarcacion
               '''
               lblInformacion.setText("Futbolista" + " " + nombre + " " + apellidos + " " + 
                                      str(edad) + " " + str(dorsal) + " " + demarcacion + " ")
                                      ''' 
               construir_tabla(["NOMBRE","APELLIDOS","EDAD","DORSAL","DEMARCACION","TIPO"],6,objeto)
            if isinstance(objeto, Entrenador):
               idFederacion = objeto.id_federacion
               '''
               lblInformacion.setText("Entrenador" + " " + nombre + " " + apellidos + " " + 
                                      str(edad) + " " + idFederacion)
                                      '''
               construir_tabla(["NOMBRE","APELLIDOS","EDAD","IDFEDERACION","TIPO"],5,objeto)
            if isinstance(objeto, Masajista):
               anio_experiencia = objeto.anio_experiencia
               titulacion = objeto.titulacion
               '''
               lblInformacion.setText("Masajista" + " " + nombre + " " + apellidos + " " + 
                                      str(edad) + " " + str(anio_experiencia) + " " + titulacion)
                                      '''
               construir_tabla(["NOMBRE","APELLIDOS","EDAD","TITULACION","EXPERIENCIA","TIPO"],6,objeto)

def obtener_conexion():
    nra = ("C:\\LENGUAJE_PROGRAMACION\\TRABAJANDO_PYTHON\\"
           "python12_combobox\\seleccionfutbol.sqlite3")
    conexion = None
    try:
       conexion = sqlite3.connect(nra)
    except sqlite3.Error as error:
       conexion = None
    return conexion

def carcargar_combobox():
    conexion = obtener_conexion()
    if conexion != None:
       QMessageBox.information(None, "INFORMACION", "CONEXION")
       try:
           cursor = conexion.cursor()
           query = "SELECT id_seleccionfutbol FROM SeleccionFutbol;" 
           cursor.execute(query) 
           idseleccionfutbol_lt = cursor.fetchall()
           cboIdSeleccionFutbol.addItem("SELECCIONAR")
           for idseleccionfutbol_t in idseleccionfutbol_lt:
               id_seleccionfutbol, = idseleccionfutbol_t
               cboIdSeleccionFutbol.addItem(id_seleccionfutbol)

       except Exception as e:
          print(e)
          QMessageBox.critical(None, "ERROR", "QUERY") 

    else:
       QMessageBox.critical(None, "ERROR", "CONEXION")

def reiniciar():
    #lblInformacion.setText("INFORMACION MIEMBRO SELECCION FUTBOL")
    tblMostrar.setColumnCount(0)
    tblMostrar.setRowCount(0)
    cboIdSeleccionFutbol.setCurrentIndex(0)

def salir():
    sys.exit()

# 0. CONSTRUIR UNA APLICACION

app = QApplication(sys.argv) 

# 1. CREAR LA VENTANA PRINCIPAL

ventana_principal = QMainWindow()
ventana_principal. setFixedSize(500, 250)
ventana_principal.setWindowTitle("SELECCION FUTBOL")

# Cambiar el icono de la ventanapython9_ventana_menu_mihaita/cross1.png con una ruta absoluta que se crea a partir de una relativa
ruta_relativa = "python12_combobox/cross1.png"
ruta_absoluta = os.path.abspath(ruta_relativa)
print(ruta_absoluta) # F:\CURSOS\TRABAJANDO\PROJECTS___PYTHON\PYTHON_TEXTO\PYTHON\PYTHON_0033\cross1.png
ventana_principal.setWindowIcon(QIcon(ruta_absoluta))

# 2. CREAR UN PANEL PRINCIPAL

panel_principal = QWidget()

# 3. CREAR UN ADMINISTRADOR PRINCIPAL

layout_principal = QVBoxLayout()

# 4. CREAR COMPONENTES Y AÑADIMOS ADMINSTRADOR PRINCIPAL



#lblInformacion = QLabel("INFORMACION MIEMBRO SELECCION FUTBOL")
#lblInformacion.setFont(QFont("Courier New", 8))
tblMostrar = QTableWidget()



cboIdSeleccionFutbol = QComboBox()
cboIdSeleccionFutbol.setFont(QFont("Courier New", 8))
cboIdSeleccionFutbol.currentIndexChanged.connect(cambiar_item)

carcargar_combobox()

btoReiniciar = QPushButton()
btoReiniciar.setText("REINICIAR")
btoReiniciar.setFont(QFont("Courier New", 8))
btoReiniciar.clicked.connect(reiniciar)

btoSalir = QPushButton()
btoSalir.setText("SALIR")
btoSalir.setFont(QFont("Courier New", 8))
btoSalir.clicked.connect(salir)

layout_botones = QHBoxLayout()

layout_botones.addWidget(btoReiniciar)
layout_botones.addWidget(btoSalir)

#layout_principal.addWidget(lblInformacion)
layout_principal.addWidget(tblMostrar)
layout_principal.addWidget(cboIdSeleccionFutbol)
layout_principal.addLayout(layout_botones)

# 5. PONER ADMINISTRADOR PRINCIPAL

panel_principal.setLayout(layout_principal)

# 6. PONER EL PANEL A LA VENTANA PRINCIPAL

ventana_principal.setCentralWidget(panel_principal)

# 7. MOSTRAR VENTANA PRINCIPAL

ventana_principal.show()

# 8. EJECUTAR APLICACION

sys.exit(app.exec())    













