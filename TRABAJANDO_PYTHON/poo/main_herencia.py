from herencia import Trabajador, Conserje, Secretaria, Directivo
import os

trabajadores_ld = [ 
{
    'id_trabajador': 'T1',
    'nombre': 'Miguel',
    'tipo_trabajador': 'Conserje',
    'horas_trabajadas': 130
},
{
    'id_trabajador': 'T2',
    'nombre': 'Carlos',
    'tipo_trabajador': 'Conserje',
    'horas_trabajadas': 160
},
{
    'id_trabajador': 'T3',
    'nombre': 'María',
    'tipo_trabajador': 'Secretaria',
    'horas_trabajadas': 160,
    'incentivos': 200
},
{
    'id_trabajador': 'T4',
    'nombre': 'Melissa',
    'tipo_trabajador': 'Secretaria',
    'horas_trabajadas': 160,
    'incentivos': 0
},
{
    'id_trabajador': 'T5',
    'nombre': 'Carlos',
    'tipo_trabajador': 'Directivo',
    'base': 5000,
    'dietas': 2000,
    'metas': 1000
}
]

def ejemplo1():
    for trabajador_d in trabajadores_ld:
        if trabajador_d['tipo_trabajador'] == 'Conserje':
           trabajador = Conserje(trabajador_d['horas_trabajadas'])
           print(trabajador_d['nombre'], " Sueldo: ", trabajador.sueldo())
        if trabajador_d['tipo_trabajador'] == 'Secretaria':
           trabajador = Secretaria(trabajador_d['horas_trabajadas'], trabajador_d['incentivos'])
           print(trabajador_d['nombre'], " Sueldo: ", trabajador.sueldo())
        if trabajador_d['tipo_trabajador'] == 'Directivo':
           trabajador = Directivo(trabajador_d['base'], trabajador_d['dietas'], trabajador_d['metas'], )
           print(trabajador_d['nombre'], " Sueldo: ", trabajador.sueldo())

def main():
    os.system("cls")
    ejemplo1()

if __name__ == "__main__":
   main()