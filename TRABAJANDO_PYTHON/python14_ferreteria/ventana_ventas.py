import sys,os
from datetime import datetime
import bcrypt
import mysql.connector
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QMessageBox, QTableWidget, QTableWidgetItem, QHBoxLayout, QHeaderView,
    QComboBox, QSpinBox
)
from PySide6.QtGui import QFont, QIcon
from PySide6.QtCore import Qt
from metodos import obtener_productos_disponibles, obtener_conexion

class VentanaVentas(QWidget):
      def __init__(self):
          super().__init__()
          self.productos_disponibles_d = {}
          self.carrito_lt = []

          self.personalizar_ventana()
          self.personalizar_componentes()
    

      def personalizar_ventana(self):
        self.setWindowTitle("Ventana Venta")  # Título para la ventana
        self.setFixedSize(800, 600)  # Tamaño de la ventana ancho y altura
        #self.setStyleSheet("background-color: lightgray;")  # Color de fondo para la ventana

        # Cambiar el icono de la ventanapython9_ventana_menu_mihaita/cross1.png con una ruta absoluta que se crea a partir de una relativa
        ruta_relativa = "python14_ferreteria/cross1.png"
        ruta_absoluta = os.path.abspath(ruta_relativa)
        self.setWindowIcon(QIcon(ruta_absoluta))

      def personalizar_componentes(self):
          layout_principal = QVBoxLayout()
          # TABLA
          self.tblCarrito = QTableWidget()
          self.tblCarrito.setColumnCount(5)
          self.tblCarrito.setHorizontalHeaderLabels(["ID","Producto","Cantidad","Precio","Subtotal"])
          self.tblCarrito.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
          # COMBOBOX
          self.cboSeleccionProducto = QComboBox()
          self.cargar_datos_combobox()

          # SPIN
          self.spinCantidad = QSpinBox()
          self.spinCantidad.setRange(1,100)

          # BOTONES
          self.btnAnadirCarrito = QPushButton("Añadir al Carrito")
          self.btnAnadirCarrito.clicked.connect(self.agregar_al_carrito)

          self.btnEliminarSeleccion = QPushButton("Eliminar Seleccion")
          self.btnEliminarSeleccion.clicked.connect(self.eliminar_seleccion)

          # CREAR ADMINISTRADOR HORIZONTAL
          layout_horizontal = QHBoxLayout()
          layout_horizontal.addWidget(self.cboSeleccionProducto)
          layout_horizontal.addWidget(self.spinCantidad)
          layout_horizontal.addWidget(self.btnAnadirCarrito)
          layout_horizontal.addWidget(self.btnEliminarSeleccion)

          # ETIQUETA
          self.lblTotal = QLabel("Total: €0.00")
          self.lblTotal.setAlignment(Qt.AlignRight)

          # BOTON CONFIRMAR VENTA
          self.btnConfirmarVenta = QPushButton("Confirmar Venta")
          self.btnConfirmarVenta.clicked.connect(self.confirmar_venta)

          layout_principal.addWidget(self.tblCarrito)
          layout_principal.addLayout(layout_horizontal)
          layout_principal.addWidget(self.lblTotal)
          layout_principal.addWidget(self.btnConfirmarVenta)

          self.setLayout(layout_principal)
    
      def cargar_datos_combobox(self):
          self.productos_disponibles_d = obtener_productos_disponibles()
          self.cboSeleccionProducto.clear()
          self.cboSeleccionProducto.addItems(self.productos_disponibles_d.keys())

      def agregar_al_carrito(self):
          producto_seleccionado = self.cboSeleccionProducto.currentText()
          print(producto_seleccionado)
          cantidad = self.spinCantidad.value()

          if producto_seleccionado not in self.productos_disponibles_d:
             QMessageBox.warning(self, "Error", "Producto no disponible") 
             return
          
          id_producto, nombre, precio, stock = self.productos_disponibles_d[producto_seleccionado]

          if cantidad > stock:
             QMessageBox.warning(self, "Error", "Stock insuficiente") 
             return
          # ACTUALIZAR STOCK
          self.productos_disponibles_d[producto_seleccionado] = (id_producto, nombre, precio, stock - cantidad)
          
          subtotal = round(precio * cantidad,2)
          self.carrito_lt.append((id_producto, nombre, cantidad, precio, subtotal))
          self.actualizar_tabla_carrito()
      
      def actualizar_tabla_carrito(self):
          self.tblCarrito.setRowCount(len(self.carrito_lt))
          total = 0
          for fila, (id_producto,nombre,cantidad,precio,subtotal) in enumerate(self.carrito_lt):
              total = total + subtotal
              # PINTAR TABLA
              self.tblCarrito.setItem(fila, 0, QTableWidgetItem(str(id_producto)))
              self.tblCarrito.setItem(fila, 1, QTableWidgetItem(nombre))
              self.tblCarrito.setItem(fila, 2, QTableWidgetItem(str(cantidad)))
              self.tblCarrito.setItem(fila, 3, QTableWidgetItem(str(precio)))
              self.tblCarrito.setItem(fila, 4, QTableWidgetItem(f"{subtotal:.2f}"))
          self.lblTotal.setText(f"Total: ${total:.2f}")

      def confirmar_venta(self):
          conexion = obtener_conexion()
          if conexion != None:
             try:
                total = 0
                for _,_,_,_,subtotal in self.carrito_lt:
                    total = total + subtotal

                cursor = conexion.cursor()
                query = "INSERT INTO Venta (fecha, total) VALUES (%s, %s)"
                cursor.execute(query,(datetime.now(),total))
                id_venta = cursor.lastrowid

                #cantidad, id_producto
                query1 = "INSERT INTO DetalleVentas (id_venta,id_producto,cantidad,subtotal) VALUES (%s,%s,%s,%s)"
                query2 = "UPDATE Producto SET stock = stock - %s WHERE id_producto = %s"
                # (id_producto, nombre, cantidad, precio, subtotal) = carrito_lt
                for id_producto,_,cantidad,_,subtotal in self.carrito_lt:
                    cursor.execute(query1, (id_venta,id_producto,cantidad,subtotal))
                    cursor.execute(query2,(cantidad, id_producto))

                conexion.commit()
                QMessageBox.information(self, "Ok", "Confirmar Ventana") 
                self.carrito_lt.clear()
                self.actualizar_tabla_carrito()
                self.cargar_datos_combobox()
             except Exception as e:
                 QMessageBox.critical(self, "Error", "Confirmar Ventana") 
          else:
             QMessageBox.critical(self, "Error", "Conexion")

      def eliminar_seleccion(self):
          fila_seleccionada = self.tblCarrito.currentRow() 

          if fila_seleccionada == -1:
             QMessageBox.warning(self, "Error", "Seleccione un producto para eliminar")
             return

          # Restituir stock del producto eliminado
          id_producto, nombre, cantidad, _, _ = self.carrito_lt.pop(fila_seleccionada)

          producto_key = next(k for k, v in self.productos_disponibles_d.items() if v[0] == id_producto)
          id_producto, nombre, precio, stock = self.productos_disponibles_d[producto_key]
          self.productos_disponibles_d[producto_key] = (id_producto, nombre, precio, stock + cantidad)
          self.actualizar_tabla_carrito()

if __name__ == "__main__":
   app = QApplication(sys.argv)
   ventana = VentanaVentas()
   ventana.show()
   sys.exit(app.exec())





