import sys
from PySide6.QtWidgets import QHBoxLayout, QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton

# 0. CONSTRUIR UNA APLICACION

app = QApplication(sys.argv)

# 1. CREAR LA VENTANA PRINCIPAL

ventana_principal = QMainWindow()

# 2. CREAR UN PANEL QWIDGET

panel = QWidget()

# 3. CREAR UN ADMINISTRADOR(LAYOUT) DEL PANEL

layout = QHBoxLayout()

# 4. CREAR COMPONENTES Y GESTINARLOS CON EL ADMINSTRADOR

lblNombre = QLabel("Nombre?")
txtNombre = QLineEdit()

lblApellido = QLabel("Apellido?")
txtApellido = QLineEdit()

btnEnviar = QPushButton("Enviar")

# Agregando etiquetas y campos de entrada

layout.addWidget(lblNombre)
layout.addWidget(txtNombre)
layout.addWidget(lblApellido)
layout.addWidget(txtApellido)
layout.addWidget(btnEnviar)

# 5. ASIGNAR EL ADMINISTRADOR AL PANEL

panel.setLayout(layout)

# 6. PONER EL PANEL A LA VENTANA PRINCIPAL

ventana_principal.setCentralWidget(panel)

# 7. MOSTRAR VENTANA PRINCIPAL

ventana_principal.show()

# 8. EJECUTAR APLICACION

sys.exit(app.exec())        