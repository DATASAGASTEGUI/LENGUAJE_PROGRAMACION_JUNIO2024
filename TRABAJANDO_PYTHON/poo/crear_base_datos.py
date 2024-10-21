import os, sqlite3

trabajadores_ld = [ 
{
    'id_trabajador': 'T1',
    'nombre': 'Miguel',
    'apellido': 'Roncal',
    'tipo_trabajador': 'Conserje',
    'horas_trabajadas': 130
},
{
    'id_trabajador': 'T2',
    'nombre': 'Carlos',
    'apellido': 'Alva',
    'tipo_trabajador': 'Conserje',
    'horas_trabajadas': 160
},
{
    'id_trabajador': 'T3',
    'nombre': 'María',
    'apellido': 'Prado',
    'tipo_trabajador': 'Secretaria',
    'horas_trabajadas': 160,
    'incentivos': 200
},
{
    'id_trabajador': 'T4',
    'nombre': 'Melissa',
    'apellido': 'Martinez',
    'tipo_trabajador': 'Secretaria',
    'horas_trabajadas': 160,
    'incentivos': 0
},
{
    'id_trabajador': 'T5',
    'nombre': 'Carlos',
    'apellido': 'Goycochea',
    'tipo_trabajador': 'Directivo',
    'base': 5000,
    'dietas': 2000,
    'metas': 1000
}
]

def obtener_conexion():
    nra = "C:\\LENGUAJE_PROGRAMACION\\TRABAJANDO_PYTHON\\poo\\trabajador.sqlite3"
    conexion = None
    try:
       conexion = sqlite3.connect(nra)
    except sqlite3.Error as error:
       conexion = None
    return conexion

def crear_tablas():
    conexion = obtener_conexion()
    if conexion != None:
       cursor = conexion.cursor()
       try:
            query_trabajador = '''
                    CREATE TABLE IF NOT EXISTS Trabajador (
                       id_trabajador TEXT NOT NULL PRIMARY KEY,
                       nombre        TEXT NOT NULL,
                       apellido      TEXT NOT NULL
                    );
            '''
            query_directivo = '''
                    CREATE TABLE IF NOT EXISTS Directivo (
                       id_directivo TEXT     NOT NULL PRIMARY KEY,
                       metas        INTEGER  NOT NULL,
                       dietas       INTEGER  NOT NULL,
                       base         INTEGER  NOT NULL,
                                    FOREIGN KEY (id_directivo) REFERENCES Trabajador (id_trabajador)
                    );
            '''

            query_secretaria = '''
                    CREATE TABLE IF NOT EXISTS Secretaria (
                       id_secretaria    TEXT    NOT NULL PRIMARY KEY,
                       horas_trabajadas INTEGER NOT NULL,
                       incentivos       INTEGER NOT NULL,
                                        FOREIGN KEY (id_secretaria) REFERENCES Trabajador (id_trabajador)
                    );
            '''

            query_conserje = '''
                    CREATE TABLE IF NOT EXISTS Conserje (
                       id_conserje      TEXT    NOT NULL PRIMARY KEY,
                       horas_trabajadas INTEGER NOT NULL,
                                        FOREIGN KEY (id_conserje) REFERENCES Trabajador (id_trabajador)
                    );
            '''
            cursor.execute(query_trabajador)
            cursor.execute(query_directivo)
            cursor.execute(query_secretaria)
            cursor.execute(query_conserje)

            print("OK: CREATE TABLE")
       except Exception as e:
            print("ERROR: CREATE TABLE")

    else:
       print("ERROR: CONEXION")
 
def insertar_registros():
    conexion = obtener_conexion()
    if conexion != None:
       cursor = conexion.cursor()
       try:
          query_trabajador = "INSERT INTO Trabajador (id_trabajador, nombre, apellido) VALUES (?,?,?);"
          query_directivo = "INSERT INTO Directivo (id_directivo, metas, dietas, base) VALUES (?,?,?,?)"
          query_secretaria = "INSERT INTO Secretaria (id_secretaria, horas_trabajadas, incentivos) VALUES (?,?,?)"
          query_conserje = "INSERT INTO Conserje (id_conserje, horas_trabajadas) VALUES (?,?)" 

          for trabajador_d in trabajadores_ld:
              id_trabajador = trabajador_d['id_trabajador']
              nombre = trabajador_d['nombre']
              apellido = trabajador_d['apellido']
              tipo_trabajador = trabajador_d['tipo_trabajador']
              cursor.execute(query_trabajador,(id_trabajador,nombre,apellido))
              if tipo_trabajador == 'Directivo':
                 metas = trabajador_d['metas']
                 dietas = trabajador_d['dietas']
                 base = trabajador_d['base']
                 cursor.execute(query_directivo,(id_trabajador,metas,dietas,base))
              if tipo_trabajador == 'Secretaria':
                 horas_trabajadas = trabajador_d['horas_trabajadas']
                 incentivos = trabajador_d['incentivos']
                 cursor.execute(query_secretaria,(id_trabajador,horas_trabajadas,incentivos))
              if tipo_trabajador == 'Conserje':
                 horas_trabajadas = trabajador_d['horas_trabajadas']
                 cursor.execute(query_conserje,(id_trabajador,horas_trabajadas,))
              print("OK: INSERT")
          conexion.commit()
       except Exception as e:
         print("ERROR: INSERT", e)  
    else:
       print("ERROR: CONEXION1")

def main():
    os.system("cls")
    crear_tablas()
    insertar_registros()
          
if __name__ == "__main__":
   main()