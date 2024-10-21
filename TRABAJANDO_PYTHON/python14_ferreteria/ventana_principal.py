import sys,os
import bcrypt
import mysql.connector
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QMessageBox, QTableWidget, QTableWidgetItem, QHBoxLayout, QHeaderView, QMainWindow
)
from PySide6.QtGui import QFont, QIcon

from ventana_gestion_usuarios import VentanaGestionUsuarios
from ventana_ventas import VentanaVentas
from ventana_inventario import VentanaInventario

class VentanaPrincipal(QMainWindow):
      def __init__(self, rol, objeto_ventana_login):
          super().__init__()
          self.setWindowTitle("Ventana Principal")  # Título para la ventana
          self.setFixedSize(400, 200)  # Tamaño de la ventana ancho y altura

          # Cambiar el icono de la ventanapython9_ventana_menu_mihaita/cross1.png con una ruta absoluta que se crea a partir de una relativa
          ruta_relativa = "python14_ferreteria/cross1.png"
          ruta_absoluta = os.path.abspath(ruta_relativa)
          self.setWindowIcon(QIcon(ruta_absoluta)) 

          layout_principal = QVBoxLayout()
          panel_principal = QWidget() 
          panel_principal.setLayout(layout_principal) 
          self.setCentralWidget(panel_principal)

          self.rol = rol
          self.objeto_ventana = objeto_ventana_login

          if rol == 'Administrador':
             self.abrir_ventana_menu_administrador(layout_principal)
          elif rol == 'Cajero':
             self.abrir_ventana_menu_cajero(layout_principal)
          elif rol == 'Almacén':
            self.abrir_ventana_menu_alamacen(layout_principal)
          
      def abrir_ventana_menu_administrador(self, layout_principal):
          btnCerrarSesion = QPushButton("Cerrar Sesión")
          btnCerrarSesion.clicked.connect(self.cerrar_sesion)
          btnGestionUsuarios = QPushButton("Gestión Usuarios")
          btnGestionUsuarios.clicked.connect(self.abrir_ventana_gestion_usuarios)
          btnGestionProductos = QPushButton("Gestión Productos")
          layout_principal.addWidget(btnGestionUsuarios)
          layout_principal.addWidget(btnGestionProductos)
          layout_principal.addWidget(btnCerrarSesion)

      def abrir_ventana_menu_cajero(self, layout_principal):
          btnCerrarSesion = QPushButton("Cerrar Sesión")
          btnCerrarSesion.clicked.connect(self.cerrar_sesion)
          btnVenta = QPushButton("Venta")
          btnVenta.clicked.connect(self.abrir_ventana_venta)
          layout_principal.addWidget(btnCerrarSesion)
          layout_principal.addWidget(btnVenta)

      def abrir_ventana_menu_almacen(self, layout_principal):
          btnCerrarSesion = QPushButton("Cerrar Sesión")
          btnCerrarSesion.clicked.connect(self.cerrar_sesion)
          btnAlmacen = QPushButton("Almacen")
          btnAlmacen.clicked.connect(self.abrir_ventana_inventario)
          layout_principal.addWidget(btnCerrarSesion)
          layout_principal.addWidget(btnAlmacen)

      def abrir_ventana_gestion_usuarios(self):
          self.ventana_gestion_usuarios = VentanaGestionUsuarios()
          self.ventana_gestion_usuarios.show()

      def abrir_ventana_venta(self):
          self.ventana_venta = VentanaVentas()
          self.ventana_venta.show()

      def abrir_ventana_inventario(self):
          self.ventana_gestion_usuarios = VentanaInventario()
          self.ventana_gestion_usuarios.show()

      def cerrar_sesion(self):
          self.close()
          self.objeto_ventana.show()

          
          