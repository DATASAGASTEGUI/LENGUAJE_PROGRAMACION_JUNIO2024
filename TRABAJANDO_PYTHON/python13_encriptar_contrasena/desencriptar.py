import sqlite3, bcrypt

def obtener_conexion():
    nra = ("C:\\LENGUAJE_PROGRAMACION\\TRABAJANDO_PYTHON\\"
           "python13_encriptar_contrasena\\ferreteria.sqlite3")
    conexion = None
    try:
       conexion = sqlite3.connect(nra)
    except sqlite3.Error as error:
       conexion = None
    return conexion

nombre_usuario = input("Ingrese nombre usuario? ")
contrasena = input("Ingrese su contraseña? ")

conexion = obtener_conexion()
cursor = conexion.cursor()
query = "SELECT contrasena FROM Usuario WHERE nombre_usuario = ?"
cursor.execute(query,(nombre_usuario,))
resultado_t = cursor.fetchone()
contrasena_hash = resultado_t[0] # dfasdfsdifasidfjasasdfiiafdasf

contrasena_byte = contrasena.encode()
print("Contraseña ingresada por usuario: ", contrasena)
print("Contraseña recupera base datos  : ", contrasena_hash.encode())

if bcrypt.checkpw(contrasena_byte, contrasena_hash.encode()):
   print("USUARIO CORRECTO")
else:
   print("USUARIO INCORRECTO")

