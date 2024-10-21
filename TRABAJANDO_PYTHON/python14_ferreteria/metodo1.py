import mysql.connector




def get_connection():
        connection = mysql.connector.connect(
            host="localhost",
            port = 3306,
            user="root",
            password="12345678",
            database="ferreteria"
        )
        return connection

def get_available_products():
    connection = get_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "SELECT id_producto, nombre, precio, stock FROM Producto WHERE stock > 0"
            cursor.execute(query)
            productos__lt = cursor.fetchall()
            #for producto in productos__lt:
            print(productos__lt)
        
        except Exception as e:
            print("Error query.")
    else:
        print("Error connection.")




if __name__ == "__main__":
    get_available_products()