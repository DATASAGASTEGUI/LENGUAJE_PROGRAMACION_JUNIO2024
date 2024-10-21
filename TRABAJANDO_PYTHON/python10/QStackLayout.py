import sys
from PySide6.QtWidgets import (
     QVBoxLayout, QApplication, QMainWindow, QWidget, 
     QLabel, QLineEdit, QPushButton,
     QHBoxLayout, QStackedLayout
)

def mostrar_panel_1():
    layout_stack.setCurrentIndex(0)

def mostrar_panel_2():
    layout_stack.setCurrentIndex(1)

def mostrar_panel_3():
    layout_stack.setCurrentIndex(2)

# 0. CONSTRUIR UNA APLICACION

app = QApplication(sys.argv) 

# 1. CREAR LA VENTANA PRINCIPAL

ventana_principal = QMainWindow()

# 2. CREAR UN PANEL PRINCIPAL QWIDGET

panel_principal = QWidget()

# 3. CREAR UN ADMINISTRADOR PRINCIPAL PARA ELL PANEL PRINCIPAL

layout_principal = QVBoxLayout()

# 4. CREAR COMPONENTES Y AÑADIRLOS AL ADMINSTRADOR PRINCIPAL

# Panel 1
panel_1 = QWidget()
layout_1 = QHBoxLayout()
lblNombre = QLabel("Nombre?")
txtNombre = QLineEdit()
layout_1.addWidget(lblNombre)
layout_1.addWidget(txtNombre)
panel_1.setLayout(layout_1)

# Panel 2
panel_2 = QWidget()
layout_2 = QHBoxLayout()
lblApellido = QLabel("Apellido?")
txtApellido = QLineEdit()
layout_2.addWidget(lblApellido)
layout_2.addWidget(txtApellido)
panel_2.setLayout(layout_2)

# Panel 3
panel_3 = QWidget()
layout_3 = QVBoxLayout()
btnEnviar = QPushButton("Enviar")
layout_3.addWidget(btnEnviar)
panel_3.setLayout(layout_3)

layout_stack = QStackedLayout()
layout_stack.addWidget(panel_1) # 0
layout_stack.addWidget(panel_2) # 1
layout_stack.addWidget(panel_3) # 2

# LAYOUT DE LOS 3 BOTONES
layout_4 = QHBoxLayout()
btn1 = QPushButton("Panel 1")
btn2 = QPushButton("Panel 2")
btn3 = QPushButton("Panel 3")
btn1.clicked.connect(mostrar_panel_1)
btn2.clicked.connect(mostrar_panel_2)
btn3.clicked.connect(mostrar_panel_3)

layout_4.addWidget(btn1)
layout_4.addWidget(btn2)
layout_4.addWidget(btn3)

layout_principal.addLayout(layout_stack)
layout_principal.addLayout(layout_4)

# 5. PONER EL ADMINISTRADOR PRINCIPAL AL PANEL PRINCIPAL

panel_principal.setLayout(layout_principal)

# 6. PONER EL PANEL PRINCIPAL A LA VENTANA PRINCIPAL

ventana_principal.setCentralWidget(panel_principal)

# 7. MOSTRAR VENTANA PRINCIPAL

ventana_principal.show()

# 8. EJECUTAR APLICACION

sys.exit(app.exec())       