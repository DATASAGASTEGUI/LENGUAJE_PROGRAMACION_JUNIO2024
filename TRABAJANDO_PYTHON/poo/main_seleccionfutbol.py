import os
from herencia_seleccionfutbol import *
import sqlite3

seleccionfutbol_lo = []

def menu():
    
    while True:
          os.system('cls')
          print("MENU")
          print("1. Crear base de datos")
          print("2. Crear objetos y gurardarlos en una lista")
          print("3. Mostrar la lista de objetos")
          print("4. Añadir objetos a la base de datos")
          print("5. Salir")

          opcion = int(input('Ingresar opcion? '))

          if opcion == 1:
             os.system('cls'); crear_base_datos(); os.system('pause')
          elif opcion == 2:
             os.system('cls'); crear_lista_objetos(); os.system('pause')
          elif opcion == 3:
             os.system('cls'); mostrar_lista_objetos(); os.system('pause')
          elif opcion == 4:
             os.system('cls'); anadir_objeto_basedatos(); os.system('pause')
          elif opcion == 5:
             os.system('cls'); break

def obtener_conexion():
    nra = "C:\\LENGUAJE_PROGRAMACION\\TRABAJANDO_PYTHON\\poo\\seleccionfutbol.sqlite3"
    conexion = None
    try:
       conexion = sqlite3.connect(nra)
    except sqlite3.Error as error:
       conexion = None
    return conexion

def crear_base_datos():
    conexion = obtener_conexion()
    if conexion != None:
        print("OK: CONEXION")
        try:
            cursor = conexion.cursor()

            # Crear las tablas
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS SeleccionFutbol (
                id_seleccionfutbol TEXT    PRIMARY KEY,
                nombre             TEXT    NOT NULL,
                apellidos          TEXT    NOT NULL,
                edad               INTEGER NOT NULL
            )
            ''')

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Futbolista (
                id_futbolista      TEXT    PRIMARY KEY,
                dorsal             INTEGER NOT NULL,
                demarcacion        TEXT    NOT NULL,
                FOREIGN KEY (id_futbolista) REFERENCES SeleccionFutbol (id_seleccionfutbol)
            )
            ''')

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Masajista (
                id_masajista       TEXT    PRIMARY KEY,
                titulacion         TEXT    NOT NULL,
                anio_experiencia   INTEGER NOT NULL,
                FOREIGN KEY (id_masajista) REFERENCES SeleccionFutbol (id_seleccionfutbol)
            )
            ''')

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Entrenador (
                id_entrenador TEXT    PRIMARY KEY,
                id_federacion INTEGER NOT NULL,
                FOREIGN KEY (id_entrenador) REFERENCES SeleccionFutbol (id_seleccionfutbol)
            )
            ''')

            # Insertar datos en la tabla SeleccionFutbol
            seleccion_futbol = [
                ('S001', 'Juan', 'Perez', 30),
                ('S002', 'Carlos', 'Lopez', 28),
                ('S003', 'Andres', 'Martinez', 32),
                ('S004', 'Luis', 'Garcia', 27),
                ('S005', 'Miguel', 'Rodriguez', 31),
                ('S006', 'Fernando', 'Fernandez', 29),
                ('S007', 'Pablo', 'Sanchez', 26),
                ('S008', 'Jorge', 'Ramirez', 33),
                ('S009', 'Roberto', 'Diaz', 25),
                ('S010', 'Raul', 'Cruz', 34),
                ('S011', 'Oscar', 'Jimenez', 28),
                ('S012', 'Mario', 'Vargas', 31),
                ('S013', 'Daniel', 'Herrera', 27),
                ('S014', 'Gabriel', 'Torres', 29),
                ('S015', 'Adrian', 'Castro', 30),
                ('S016', 'Francisco', 'Gomez', 26),
                ('S017', 'Ricardo', 'Ruiz', 32),
                ('S018', 'Victor', 'Mendoza', 28),
                ('S019', 'Diego', 'Ortiz', 33),
                ('S020', 'Ivan', 'Silva', 27),
                ('S021', 'Sergio', 'Morales', 25),
                ('S022', 'Edgar', 'Navarro', 31),
                ('S023', 'Martin', 'Rios', 29),
                ('S024', 'Enrique', 'Flores', 26),
                ('S025', 'Tomas', 'Gutierrez', 32),
                ('S026', 'Hugo', 'Peña', 30),
                ('S027', 'Alberto', 'Castillo', 27),
                ('S028', 'Alejandro', 'Aguilar', 31),
                ('S029', 'Javier', 'Mendez', 28),
                ('S030', 'Angel', 'Carrillo', 34),
                ('S031', 'Emilio', 'Salazar', 33),
                ('S032', 'Samuel', 'Vera', 29),
                ('S033', 'Benjamin', 'Soto', 26),
                ('S034', 'Cristian', 'Chavez', 30),
                ('S035', 'Lucas', 'Arias', 25),
                ('S036', 'Nicolas', 'Delgado', 27),
                ('S037', 'Marcelo', 'Fuentes', 32),
                ('S038', 'Antonio', 'Romero', 29),
                ('S039', 'Manuel', 'Ibanez', 28),
                ('S040', 'Sebastian', 'Mejia', 31)
            ]

            cursor.executemany("INSERT INTO SeleccionFutbol (id_seleccionfutbol, nombre, apellidos, edad) VALUES (?, ?, ?, ?)", seleccion_futbol)

            # Insertar datos en Futbolista
            futbolistas = [
                ('S001', 9, 'Delantero'), ('S002', 4, 'Defensa'), ('S003', 10, 'Delantero'),
                ('S004', 5, 'Medio'), ('S005', 3, 'Defensa'), ('S006', 8, 'Medio'),
                ('S007', 11, 'Portero'), ('S008', 6, 'Lateral'), ('S009', 7, 'Delantero'),
                ('S010', 2, 'Defensa')
            ]
            cursor.executemany("INSERT INTO Futbolista (id_futbolista, dorsal, demarcacion) VALUES (?, ?, ?)", futbolistas)

            # Insertar datos en Masajista
            masajistas = [
                ('S011', 'Fisioterapia', 5), ('S012', 'Rehabilitacion', 3), ('S013', 'Deporte', 7),
                ('S014', 'Masaje', 4), ('S015', 'Terapia Deportiva', 6), ('S016', 'Recuperación', 8),
                ('S017', 'Fisioterapia', 2), ('S018', 'Rehabilitacion', 5), ('S019', 'Kinesiología', 3),
                ('S020', 'Masoterapia', 6)
            ]
            cursor.executemany("INSERT INTO Masajista (id_masajista, titulacion, anio_experiencia) VALUES (?, ?, ?)", masajistas)

            # Insertar datos en Entrenador
            entrenadores = [
                ('S021', 1001), ('S022', 1002), ('S023', 1003), ('S024', 1004), ('S025', 1005),
                ('S026', 1006), ('S027', 1007), ('S028', 1008), ('S029', 1009), ('S030', 1010)
            ]
            cursor.executemany("INSERT INTO Entrenador (id_entrenador, id_federacion) VALUES (?, ?)", entrenadores)

            # Guardar y cerrar conexión
            conexion.commit()
            conexion.close()
            print("OK: CREAR BASE DATOS")
        except Exception as e:
            print("ERROR: CREAR BASE DATOS")
    else:
        print("ERROR: CONEXION")

def obtener_lista_seleccionfutbol_objeto():
    conexion = obtener_conexion()
    if conexion != None:
       cursor = conexion.cursor()
       try:
          query_seleccionfutbol = "SELECT * FROM SeleccionFutbol" 
          cursor.execute(query_seleccionfutbol)
          seleccionfutbol_lt = cursor.fetchall()
          for seleccionfutbol_t in seleccionfutbol_lt:
              id_seleccionfutbol, nombre, apellidos, edad = seleccionfutbol_t

              cursor.execute('SELECT * FROM Futbolista WHERE id_futbolista = ?',(id_seleccionfutbol,))
              resultado_t = cursor.fetchone()
              if resultado_t:
                 id_futbolista, dorsal, demarcacion = resultado_t
                 seleccionfutbol_o = Futbolista(id_futbolista, nombre, apellidos, edad, dorsal, demarcacion)
                 seleccionfutbol_lo.append(seleccionfutbol_o)

              cursor.execute('SELECT * FROM Entrenador WHERE id_entrenador = ?',(id_seleccionfutbol,))
              resultado_t = cursor.fetchone()
              if resultado_t:
                 id_entrenador, id_federacion = resultado_t
                 seleccionfutbol_o = Entrenador(id_entrenador, nombre, apellidos, edad, id_federacion)
                 seleccionfutbol_lo.append(seleccionfutbol_o)

              cursor.execute('SELECT * FROM Masajista WHERE id_masajista = ?',(id_seleccionfutbol,))
              resultado_t = cursor.fetchone()
              if resultado_t:
                 id_masajista, titulacion, anio_experiencia = resultado_t
                 seleccionfutbol_o = Masajista(id_masajista, nombre, apellidos, edad, titulacion, anio_experiencia)
                 seleccionfutbol_lo.append(seleccionfutbol_o)
          print("OK: LISTA SELECCION FUTBOL")
          return seleccionfutbol_lo             
       except Exception as e:
          print("ERROR: SELECT ", e)
          return None
    else:
        print("ERROR: CONEXION")

def crear_lista_objetos():
    global seleccionfutbol_lo
    seleccionfutbol_lo.clear()
    seleccionfutbol_lo = obtener_lista_seleccionfutbol_objeto()

def anadir_objeto_basedatos():
    delBosque = Entrenador(1, "Vicente", "Del Bosque", 60, "284EZ89")
    iniesta = Futbolista(2, "Andres", "Iniesta", 29, 6, "Interior Derecho")
    raulMartinez = Masajista(3, "Raúl", "Martinez", 41, "Licenciado en Fisioterapia", 18)
    lista_objetos = [delBosque, iniesta, raulMartinez]
    conexion = obtener_conexion()
    if conexion != None:
        cursor = conexion.cursor()
        try:
          for objeto in lista_objetos:
              if isinstance(objeto,Futbolista): 
                 tupla_padre = (objeto.id_seleccionfutbol,objeto.nombre,objeto.apellidos,objeto.edad)
                 tupla_hijo = (objeto.id_seleccionfutbol,objeto.dorsal,objeto.demarcacion)
                 cursor.execute("INSERT INTO SeleccionFutbol (id_seleccionfutbol, nombre, apellidos, edad) VALUES (?, ?, ?, ?)", tupla_padre)
                 cursor.execute("INSERT INTO Futbolista (id_futbolista, dorsal, demarcacion) VALUES (?, ?, ?)", tupla_hijo)
          
              if isinstance(objeto,Masajista): 
                 tupla_padre = (objeto.id_seleccionfutbol,objeto.nombre,objeto.apellidos,objeto.edad)
                 tupla_hijo = (objeto.id_seleccionfutbol,objeto.titulacion,objeto.anio_experiencia)
                 cursor.execute("INSERT INTO SeleccionFutbol (id_seleccionfutbol, nombre, apellidos, edad) VALUES (?, ?, ?, ?)", tupla_padre)
                 cursor.execute("INSERT INTO Masajista (id_masajista, titulacion, anio_experiencia) VALUES (?, ?, ?)", tupla_hijo)

              if isinstance(objeto,Entrenador): 
                 tupla_padre = (objeto.id_seleccionfutbol,objeto.nombre,objeto.apellidos,objeto.edad)
                 tupla_hijo = (objeto.id_seleccionfutbol,objeto.id_federacion)
                 cursor.execute("INSERT INTO SeleccionFutbol (id_seleccionfutbol, nombre, apellidos, edad) VALUES (?, ?, ?, ?)", tupla_padre)
                 cursor.execute("INSERT INTO Entrenador (id_entrenador, id_federacion) VALUES (?, ?)", tupla_hijo)
          conexion.commit()
          conexion.close()
          print("OK: INSERT")
        except Exception as e:
           print("ERROR: INSERT")
    else:
        print("ERROR: CONEXION")

def mostrar_lista_objetos():
    for seleccionfutbol_o in seleccionfutbol_lo:
        print(seleccionfutbol_o.nombre, end=' ')
        if isinstance(seleccionfutbol_o, Futbolista):
           print('Futbolista')
        if isinstance(seleccionfutbol_o, Masajista):
           print('Masajista')
        if isinstance(seleccionfutbol_o, Entrenador):
           print('Entrenador')

def main():
    menu()
          
if __name__ == "__main__":
   main()