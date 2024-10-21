import sys
from PySide6.QtWidgets import (
     QVBoxLayout, QApplication, QMainWindow, QWidget, 
     QLabel, QStackedLayout, QPushButton, QHBoxLayout
)
from PySide6.QtGui import QPixmap

def mostrar_anterior():
    index = layout_stack.currentIndex() # 5
    if index > 0:
       layout_stack.setCurrentIndex(index - 1)
    else:
       layout_stack.setCurrentIndex(layout_stack.count()-1) # 20 - 1 = 19
   
def mostrar_siguiente():
    index = layout_stack.currentIndex()
    if index < layout_stack.count()-1:
       layout_stack.setCurrentIndex(index + 1)
    else:
       layout_stack.setCurrentIndex(0)

# 0. CONSTRUIR UNA APLICACION

app = QApplication(sys.argv) 

# 1. CREAR LA VENTANA PRINCIPAL

ventana_principal = QMainWindow()

# 2. CREAR UN PANEL PRINCIPAL QWIDGET

panel_principal = QWidget()

# 3. CREAR UN ADMINISTRADOR PRINCIPAL PARA ELL PANEL PRINCIPAL

layout_principal = QVBoxLayout()

# 4. CREAR COMPONENTES Y AÑADIRLOS AL ADMINSTRADOR PRINCIPAL

layout_stack = QStackedLayout()

# PRIME BLOQUE
imagenes_l = []
ruta_absoluta = "C:\\LENGUAJE_PROGRAMACION\\TRABAJANDO_PYTHON\\python11_stack_imagenes\\imagenes"
for i in range(1,21,1):
    if i < 10:
       s = "0" + str(i) # 01
    else:
       s = str(i)       # 11  
    ruta_foto = f"{ruta_absoluta}\\{s}.png"
    imagenes_l.append(ruta_foto)

for imagen in imagenes_l:
    panel = QWidget()
    layout = QVBoxLayout()
    lblImagen = QLabel()

    pixmap = QPixmap(imagen)

    if pixmap.isNull():
       lblImagen.setText("Imagen no se puede cargar")
    else:
       lblImagen.setPixmap(pixmap.scaled(300,400))

    layout.addWidget(lblImagen)
    panel.setLayout(layout)

    layout_stack.addWidget(panel) # 0, 1, 2, ... 19

# SEGUNDO BLOQUE

layout_botones = QHBoxLayout()

btnAnterior = QPushButton("Anterior")
btnSiguiente = QPushButton("Siguiente")

btnAnterior.clicked.connect(mostrar_anterior)
btnSiguiente.clicked.connect(mostrar_siguiente)

layout_botones.addWidget(btnAnterior)
layout_botones.addWidget(btnSiguiente)

# PONER LOS DOS BLOQUES ANTERIORES AL PRINCIPAL

layout_principal.addLayout(layout_stack)
layout_principal.addLayout(layout_botones)

# layout_stack.setCurrentIndex(5)

# 5. PONER EL ADMINISTRADOR PRINCIPAL AL PANEL PRINCIPAL

panel_principal.setLayout(layout_principal)

# 6. PONER EL PANEL PRINCIPAL A LA VENTANA PRINCIPAL

ventana_principal.setCentralWidget(panel_principal)

# 7. MOSTRAR VENTANA PRINCIPAL

ventana_principal.show()

# 8. EJECUTAR APLICACION

sys.exit(app.exec())       