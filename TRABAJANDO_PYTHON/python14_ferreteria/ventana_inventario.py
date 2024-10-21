import sys, os
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QLineEdit, QLabel, QMessageBox, QSpinBox, QHeaderView, QComboBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon
import mysql.connector
from metodos import obtener_conexion

class VentanaInventario(QWidget):
      def __init__(self):
          super().__init__()
          self.personalizar_ventana()
          self.personalizar_componentes()
    
      def personalizar_ventana(self):
        self.setWindowTitle("Ventana Inventario")  # Título para la ventana
        self.setFixedSize(800, 600)  # Tamaño de la ventana ancho y altura
        #self.setStyleSheet("background-color: lightgray;")  # Color de fondo para la ventana

        # Cambiar el icono de la ventanapython9_ventana_menu_mihaita/cross1.png con una ruta absoluta que se crea a partir de una relativa
        ruta_relativa = "python14_ferreteria/cross1.png"
        ruta_absoluta = os.path.abspath(ruta_relativa)
        self.setWindowIcon(QIcon(ruta_absoluta))

      def personalizar_componentes(self):
          layout_principal = QVBoxLayout()

          # COMBOBOX ORDENAR POR STOCK
          self.cboOrdenarStock = QComboBox()
          self.cboOrdenarStock.addItems(["Seleccione ordenar Stock","Ordenar por Stock (Ascendente)", "Ordenar por Stock (Descendente)"])
          self.cboOrdenarStock.currentIndexChanged.connect(self.ordenar_tabla_productos)

          # TABLA
          self.tblTablaProductos = QTableWidget()
          self.tblTablaProductos.setColumnCount(5)
          self.tblTablaProductos.setHorizontalHeaderLabels(["ID","Nombre","Descripción","Precio","Stock"])
          self.tblTablaProductos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

          self.actualizar_tabla_productos()

          # CAJA
          self.txtIdProductoEntrada = QLineEdit()
          self.txtIdProductoEntrada.setPlaceholderText("ID del Producto")

          # SPIN
          self.spinCantidad = QSpinBox()
          self.spinCantidad.setRange(1, 1000)

          # BOTON
          self.btnIncrementarStock = QPushButton("Incrementar Stock")
          self.btnIncrementarStock.clicked.connect(self.incrementar_stock)

          self.btnDecrementarStock = QPushButton("Decremenar Stock")
          self.btnDecrementarStock.clicked.connect(self.decrementar_stock)

          self.btnActualizarTablaProductos = QPushButton("Actualizar Tabla Productos")
          self.btnActualizarTablaProductos.clicked.connect(self.actualizar_tabla_productos)

          layout_horizontal = QHBoxLayout()
          layout_horizontal.addWidget(self.txtIdProductoEntrada)
          layout_horizontal.addWidget(self.spinCantidad)
          layout_horizontal.addWidget(self.btnIncrementarStock)
          layout_horizontal.addWidget(self.btnDecrementarStock)

          layout_principal.addWidget(self.cboOrdenarStock)
          layout_principal.addWidget(self.tblTablaProductos)
          layout_principal.addLayout(layout_horizontal)
          layout_principal.addWidget(self.btnActualizarTablaProductos)

          self.setLayout(layout_principal)

      def incrementar_stock(self):
          conexion = obtener_conexion()
          if conexion != None:
             try:
                 cantidad = self.spinCantidad.value()
                 id_producto = self.txtIdProductoEntrada.text()
                 cursor = conexion.cursor()
                 query =  "UPDATE Producto SET stock = stock + %s WHERE id_producto = %s"
                 cursor.execute(query,(cantidad, id_producto))
                 if cursor.rowcount == 0:
                    QMessageBox.warning(self, "Error", f"ID {id_producto} no encontrado.")
                 else:
                    QMessageBox.information(self, "Ok", f"ID {id_producto} aumento {cantidad} unidades") 
                 conexion.commit()
                 self.actualizar_tabla_productos()

             except mysql.connector.Error as e:
                 QMessageBox.critical(self, "Error", "Query Update")
          else:
              QMessageBox.critical(self, "Error", "Conexion")
              
      def decrementar_stock(self):
          conexion = obtener_conexion()
          if conexion != None:
             try:
                 cantidad = self.spinCantidad.value()
                 id_producto = self.txtIdProductoEntrada.text()
                 cursor = conexion.cursor()
                 query = "SELECT stock FROM Producto WHERE id_producto = %s"
                 cursor.execute(query,(id_producto,))
                 producto_t = cursor.fetchone()
                 if not producto_t:
                    QMessageBox.warning(self, "Error", f"ID {id_producto} no encontrado.")
                    return

                 if cantidad <= producto_t[0]: # stock obtenido de la tabla del producto
                    query =  "UPDATE Producto SET stock = stock - %s WHERE id_producto = %s"
                    cursor.execute(query,(cantidad, id_producto))
                    if cursor.rowcount == 0:
                        QMessageBox.warning(self, "Error", f"ID {id_producto} no encontrado.")
                    else:
                        QMessageBox.information(self, "Ok", f"ID {id_producto} disminuyo {cantidad} unidades") 
                    conexion.commit()
                    self.actualizar_tabla_productos()
                 else:
                    QMessageBox.warning(self, "Error", f"Cantidad {cantidad} debe ser menor o igual al stock {producto_t[0]}") 
             except mysql.connector.Error as e:
                 QMessageBox.critical(self, "Error", "Query Update")
          else:
              QMessageBox.critical(self, "Error", "Conexion")
      
      def actualizar_tabla_productos(self):
          conexion = obtener_conexion()
          if conexion != None:
             try:
                 cursor = conexion.cursor()
                 query = "SELECT id_producto, nombre, descripcion, precio, stock FROM Producto"
                 cursor.execute(query)
                 productos_lt = cursor.fetchall()
                 self.pintar_tabla(productos_lt)
             except mysql.connector.Error as e:
                 QMessageBox.critical(self, "Error", "QUERY SELECT")
          else:
             QMessageBox.critical(self, "Error", "Conexion")

      def pintar_tabla(self,productos_lt):
          self.tblTablaProductos.setRowCount(len(productos_lt))
          for fila, (id_producto,nombre,descripcion,precio,stock) in enumerate(productos_lt):
              self.tblTablaProductos.setItem(fila, 0, QTableWidgetItem(str(id_producto)))
              self.tblTablaProductos.setItem(fila, 1, QTableWidgetItem(nombre))
              self.tblTablaProductos.setItem(fila, 2, QTableWidgetItem(descripcion))
              self.tblTablaProductos.setItem(fila, 3, QTableWidgetItem(str(precio)))
              self.tblTablaProductos.setItem(fila, 4, QTableWidgetItem(str(stock)))

      def ordenar_tabla_productos(self):
          conexion = obtener_conexion()
          if conexion != None:
             try:
                 if self.cboOrdenarStock.currentIndex() == 0:
                    self.actualizar_tabla_productos()
                    return
                 
                 ordenar = ""
                 if self.cboOrdenarStock.currentIndex() == 1:
                    ordenar = "ASC"
                 else:
                    ordenar = "DESC"
                 cursor = conexion.cursor()
                 query = f"SELECT id_producto, nombre, descripcion, precio, stock FROM Producto ORDER BY stock {ordenar}"
                 cursor.execute(query)
                 productos_lt = cursor.fetchall()
                 self.pintar_tabla(productos_lt)
             except mysql.connector.Error as e:
                 QMessageBox.critical(self, "Error", "QUERY SELECT")
          else:
             QMessageBox.critical(self, "Error", "Conexion")
          
if __name__ == "__main__":
   app = QApplication(sys.argv)
   ventana = VentanaInventario()
   ventana.show()
   sys.exit(app.exec())