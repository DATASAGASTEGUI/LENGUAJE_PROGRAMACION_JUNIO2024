import mysql.connector

def obtener_conexion():
    conexion = None
    try:
       conexion = mysql.connector.connect(
       host="localhost",
       user="root",
       port="3307",
       password="12345678",
       database="ferreteria")
    except Exception as e:
       print(e)
       conexion = None
    return conexion

def obtener_productos_disponibles():
    conexion = obtener_conexion()
    if conexion != None:
       try:
          cursor = conexion.cursor()
          query = "SELECT id_producto, nombre, precio, stock FROM Producto WHERE stock > 0"
          cursor.execute(query)
          productos_lt = cursor.fetchall()
          productos_disponibles_d = {}
          productos_disponibles_d = {f"{p[0]} - {p[1]}": p for p in productos_lt}
          print(productos_disponibles_d)
       except Exception as e:
          print("ERROR: QUERY SELECT", e)  
    else:
       print("ERROR: CONEXION")  
    return productos_disponibles_d

print("hola")

if __name__ == "__main__":
   print("hola")
   obtener_productos_disponibles()
   print("llego")