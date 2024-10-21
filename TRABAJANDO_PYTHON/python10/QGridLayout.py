import sys, sqlite3
from PySide6.QtWidgets import QCalendarWidget,QMessageBox,QComboBox, QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Qt, QDate

def obtener_conexion():
    nra = "C:\\LENGUAJE_PROGRAMACION\\TRABAJANDO_PYTHON\\python10\\persona.sqlite3"
    conexion = None
    try:
       conexion = sqlite3.connect(nra)
    except sqlite3.Error as error:
       conexion = None
    return conexion

def insertar(nombre,apellido,sexo):
    conexion = obtener_conexion()
    if conexion != None:
       QMessageBox.information(None,"OK","CONEXION")
       try:
         cursor = conexion.cursor()
         query = "INSERT INTO Persona (nombre,apellido,sexo) VALUES(?,?,?);"
         registro_t = (nombre,apellido,sexo)
         cursor.execute(query,registro_t)
         conexion.commit()
         QMessageBox.information(None,"OK","INSERT")
       except Exception as e:
         QMessageBox.critical(None,"ERROR","INSERT")
    else:
       QMessageBox.critical(None,"ERROR","CONEXION")

def obtener_datos():
    nombre = txtNombre.text()
    apellido = txtApellido.text()
    sexo = cboSexo.currentText()
    bandera = False
    if sexo == 'Seleccione':
       QMessageBox.critical(None,"ERROR","DEBE SELECCIONAR SU SEXO")
    elif sexo == 'Hombre':
       sexo = 'H'; bandera = True
    else:
       sexo = 'M'; bandera = True
    
    if bandera == True:
       insertar(nombre,apellido,sexo)
       QMessageBox.information(None,"OK","DATOS")

def mostrarFechaSeleccionada(fecha):
    print(fecha)
    fecha_str = "{:02d}/{:02d}/{:04d}".format(fecha.day(), fecha.month(), fecha.year())
    txtNacimiento.setText(fecha_str)  

# 0. CONSTRUIR UNA APLICACION

app = QApplication(sys.argv) #<------------

# 1. CREAR LA VENTANA PRINCIPAL

ventana_principal = QMainWindow()

# 2. CREAR UN PANEL QWIDGET

panel = QWidget()

# 3. CREAR UN ADMINISTRADOR(LAYOUT) DEL PANEL

layoutGrid = QGridLayout()

# 4. CREAR COMPONENTES Y GESTINARLOS CON EL ADMINSTRADOR

lblNombre = QLabel("Nombre?")
txtNombre = QLineEdit()

layoutGrid.addWidget(lblNombre,0,0)
layoutGrid.addWidget(txtNombre,0,1)

lblApellido = QLabel("Apellido?")
txtApellido = QLineEdit()

layoutGrid.addWidget(lblApellido,1,0)
layoutGrid.addWidget(txtApellido,1,1)

calendario = QCalendarWidget()
calendario.setGridVisible(True)
calendario.setGeometry(10, 10, 460, 250)
calendario.clicked[QDate].connect(mostrarFechaSeleccionada) #1
layoutGrid.addWidget(calendario,4,1)

txtNacimiento = QLineEdit()
layoutGrid.addWidget(txtNacimiento,5,1)

lblNacimiento = QLabel("Selecciones Fecha Nacimiento")
layoutGrid.addWidget(lblNacimiento,6,1)



cboSexo = QComboBox()
cboSexo.addItem("Seleccione")
cboSexo.addItem("Hombre")
cboSexo.addItem("Mujer")

layoutGrid.addWidget(cboSexo,2,1)

btnEnviar = QPushButton("Enviar")
btnEnviar.clicked.connect(obtener_datos)

layoutGrid.addWidget(btnEnviar,3,1)

# 5. ASIGNAR EL ADMINISTRADOR AL PANEL

panel.setLayout(layoutGrid)

# 6. PONER EL PANEL A LA VENTANA PRINCIPAL

ventana_principal.setCentralWidget(panel)

# 7. MOSTRAR VENTANA PRINCIPAL

ventana_principal.show()

# 8. EJECUTAR APLICACION

sys.exit(app.exec())        #<------------








