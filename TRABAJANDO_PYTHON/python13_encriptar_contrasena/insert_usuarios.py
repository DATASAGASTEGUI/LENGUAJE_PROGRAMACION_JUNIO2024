import sys, sqlite3, bcrypt
from PySide6.QtWidgets import (
    QFormLayout, QApplication, QMainWindow, 
    QWidget, QGridLayout, QLabel, QLineEdit, QPushButton,
    QComboBox, QMessageBox, QHBoxLayout
)
from PySide6.QtGui import QFont, QIcon

def cambiar_item():
    pass

def create_table():
    crear_tabla()

def insert():
    conexion = obtener_conexion()
    if conexion != None:
       QMessageBox.information(None, "INFORMACION", "CONEXION")
       try:
           cursor = conexion.cursor()
           query = """INSERT INTO Usuario(nombre_usuario,contrasena,rol) 
                      VALUES (?,?,?);"""
           nombre_usuario = txtNombreUsuario.text()
           contrasena = txtContrasena.text()
           rol = cboRol.currentText()
           print(nombre_usuario)
           print(contrasena)
           print(rol)
           cursor.execute(query,(nombre_usuario,encriptar_contrasena(contrasena),rol))
           conexion.commit()
           QMessageBox.information(None, "INFORMACION", "OK INSERT")
       except Exception as e:
           QMessageBox.critical(None, "ERROR", "QUERY INSERT")
    else:
      QMessageBox.critical(None, "ERROR", "CONEXION")

def encriptar_contrasena(contrasena):
    # CONVERTIR LA CONTRASEÑA A BYTES
    contrasena_byte = contrasena.encode()
    contrasena_hashed = bcrypt.hashpw(contrasena_byte, bcrypt.gensalt())
    return contrasena_hashed.decode()

def obtener_conexion():
    nra = ("C:\\LENGUAJE_PROGRAMACION\\TRABAJANDO_PYTHON\\"
           "python13_encriptar_contrasena\\ferreteria.sqlite3")
    conexion = None
    try:
       conexion = sqlite3.connect(nra)
    except sqlite3.Error as error:
       conexion = None
    return conexion

def crear_tabla():
    conexion = obtener_conexion()
    if conexion != None:
       QMessageBox.information(None, "INFORMACION", "CONEXION")
       try:
            cursor = conexion.cursor()
            sql = """CREATE TABLE Usuario (
                     id_usuario  INTEGER PRIMARY KEY AUTOINCREMENT,
                     nombre_usuario      TEXT NOT NULL UNIQUE,
                     contrasena          TEXT NOT NULL,
                     rol                 TEXT NOT NULL CHECK (rol IN ('Administrador', 'Cajero', 'Almacén'))
                                                );"""
            cursor.execute(sql)
            conexion.commit()
            conexion.close()
       except Exception as e:
            QMessageBox.critical(None, "ERROR", "QUERY")
    else:
       QMessageBox.critical(None, "ERROR", "CONEXION") 


# 0. CONSTRUIR UNA APLICACION

app = QApplication(sys.argv) 

# 1. CREAR LA VENTANA PRINCIPAL

ventana_principal = QMainWindow()

# 2. CREAR UN PANEL PRINCIPAL

panel_principal = QWidget()

# 3. CREAR UN ADMINISTRADOR PRINCIPAL DEL PANEL

layout_principal = QFormLayout()

# 4. CREAR COMPONENTES Y GESTINARLOS CON EL ADMINSTRADOR

lblNombreUsuario = QLabel("Nombre Usuario?")
txtNombreUsuario = QLineEdit()

lblContrasena = QLabel("Contrasena?")
txtContrasena = QLineEdit()
txtContrasena.setEchoMode(QLineEdit.Password)

btnTogglePassword = QPushButton("👁️") 
btnTogglePassword.setCheckable(True)  # Hacer que el botón sea conmutador (toggle)
btnTogglePassword.setFixedSize(30, 30)

# Función para alternar la visibilidad
def toggle_password_visibility():
    if btnTogglePassword.isChecked():
        txtContrasena.setEchoMode(QLineEdit.Normal)  # Mostrar texto
        btnTogglePassword.setText("👁️")  # Cambiar ícono
    else:
        txtContrasena.setEchoMode(QLineEdit.Password)  # Ocultar texto
        btnTogglePassword.setText("🙈")  # Cambiar ícono de vuelta

# Conectar la señal del botón a la función
btnTogglePassword.clicked.connect(toggle_password_visibility)

btnTogglePassword.setText("🙈")  # Cambiar ícono de vuelta



cboRol = QComboBox()
cboRol.setFont(QFont("Courier New", 8))
cboRol.addItem('SELECCIONAR ROL')
cboRol.addItem('Administrador')
cboRol.addItem('Cajero')
cboRol.addItem('Almacén')
cboRol.currentIndexChanged.connect(cambiar_item)

btnCreate = QPushButton("CREATE TABLE")
btnCreate.clicked.connect(create_table)

btnInsert = QPushButton("INSERT")
btnInsert.clicked.connect(insert)

# Agregando etiquetas y campos de entrada
layout = QHBoxLayout()
layout.addWidget(lblContrasena)
layout.addWidget(txtContrasena)
layout.addWidget(btnTogglePassword)


layout_principal.addRow(lblNombreUsuario, txtNombreUsuario)
layout_principal.addRow(layout)
layout_principal.addRow(QLabel(""),cboRol)
layout_principal.addRow(btnCreate, btnInsert)


# 5. ASIGNAR EL ADMINISTRADOR AL PANEL

panel_principal.setLayout(layout_principal)

# 6. PONER EL PANEL A LA VENTANA PRINCIPAL

ventana_principal.setCentralWidget(panel_principal)

# 7. MOSTRAR VENTANA PRINCIPAL

ventana_principal.show()

# 8. EJECUTAR APLICACION

sys.exit(app.exec())      