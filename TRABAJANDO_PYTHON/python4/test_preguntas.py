import random, os, re

# BASE DE DATOS DE PREGUNTAS
letras_l = ['A', 'B', 'C', 'D']
preguntas_l = [
    {
        'pregunta': '¿La función principal del sistema operativo es?',
        'opciones_l': [
            'Facilitar el uso de la computadora al usuario',
            'Hacer la programación más fácil para los programadores',
            'Administrar recursos',
            'Todas las anteriores'
        ],
        'respuesta': letras_l[3]
    },
    {
        'pregunta': '¿Las partes de un sistema operativo son?',
        'opciones_l': [
            'Núcleo, drivers y programas',
            'Núcleo, consola de comandos y aplicaciones',
            'Núcleo, intérprete de comandos y sistema de archivos',
            'Sistema de archivos, compiladores / intérpretes y administrador de recursos'
        ],
        'respuesta': letras_l[2]
    },
    {
        'pregunta': 'Para poder programar un algoritmo:',
        'opciones_l': [
            'Debe tener un número infinito de pasos.',
            'Debe tener al menos una salida.',
            'Cada paso debe ser escrito lo más corto posible.',
            'Ninguna de las anteriores.'
        ],
        'respuesta': letras_l[2]
    },
    {
        'pregunta': 'El ensamblador y el código máquina son:',
        'opciones_l': [
            'Lenguajes de programación de bajo nivel.',
            'Lenguajes de programación de alto nivel.',
            'Parte del sistema operativo.',
            'Entornos de programación.'
        ],
        'respuesta': letras_l[0]
    },
    {
        'pregunta': 'El compilador de Python permite ejecutar un archivo con extensión .py:',
        'opciones_l': [
            'Siempre que se ejecute como superusuario.',
            'Verdadero.',
            'Falso. Python no tiene compilador.',
            'Falso. Los archivos .py no pueden ser ejecutados.'
        ],
        'respuesta': letras_l[1]
    },
    {
        'pregunta': 'La parte de la computadora responsable de realizar cálculos aritméticos y lógicos se llama:',
        'opciones_l': [
            'RAM',
            'CPU',
            'ROM',
            'Registros'
        ],
        'respuesta': letras_l[1]
    },
    {
        'pregunta': '¿Qué tipo de salidas de energía tiene el bus GPIO?',
        'opciones_l': [
            'De 3.3V y 5V',
            'No tiene salidas de energía',
            'SPI e I2C',
            'PoE (Power over Ethernet)'
        ],
        'respuesta': letras_l[0]
    },
    {
        'pregunta': 'La memoria ROM...',
        'opciones_l': [
            'Es volátil',
            'Tiene gran capacidad',
            'Almacena las instrucciones de arranque del procesador',
            'Almacena el sistema operativo del procesador'
        ],
        'respuesta': letras_l[2]
    },
    {
        'pregunta': 'El siguiente comando de la consola $ mv blink.py blink2.py',
        'opciones_l': [
            'Renombra el archivo blink.py como blink2.py',
            'Es incorrecto.',
            'Renombra el archivo blink2.py como blink.py',
            'Mueve el archivo blink.py a home.'
        ],
        'respuesta': letras_l[0]
    },
    {
        'pregunta': '¿Cuál de las siguientes reglas no es correcta?',
        'opciones_l': [
            'Un símbolo de decisión puede ser alcanzado por varias líneas.',
            'Varias líneas pueden llegar a un símbolo de proceso.',
            'Todos los símbolos deben estar conectados.',
            'Todas las líneas que queramos pueden salir de un símbolo de decisión.'
        ],
        'respuesta': letras_l[3]
    }
]

def menu():
    while True:
          os.system('cls')
          print('MENU')
          print('(1) MOSTRAR TODAS LAS PREGUNTAS')
          print('(2) TEST')
          print('(3) SALIR')

          opcion = input('Ingrese opción? ')

          if opcion == '1':
             os.system('cls');opcion1();os.system('pause')
          elif opcion == '2':
             os.system('cls');opcion2();os.system('pause')
          elif opcion == '3':
             os.system('cls')
             print('Gracias por si visita. ADIOS')
             os.system('pause')
             break
          
def opcion1():
    for index,pregunta_d in enumerate(preguntas_l):
        print((index+1),":",pregunta_d['pregunta'])

def opcion2():
    while True:
          numero_preguntas_aleatorias = int(input('Ingrese número preguntas? '))
          if numero_preguntas_aleatorias > len(preguntas_l):
             continue 
          preguntasaleatorias_l = obtener_preguntas_aleatorias(preguntas_l, numero_preguntas_aleatorias)
          puntaje = 0
          correcta = 0
          for index, pregunta_d in enumerate(preguntasaleatorias_l):
              print(str((index+1))+') '+pregunta_d['pregunta'])
              for i,opcion_s in enumerate(pregunta_d['opciones_l']):
                  print(letras_l[i]+'. '+opcion_s)
              print()
              respuesta_usuario = entrada_opcion('Ingrese su respuesta? ')
              if respuesta_usuario != "":
                    if respuesta_usuario == pregunta_d['respuesta']:
                        puntaje += 1
                        correcta += 1
                    else:
                        puntaje -= 0.25

          print("Puntaje: ", puntaje) 
          print(correcta, " correctas de ", len(preguntasaleatorias_l))

def entrada_opcion(mensaje):
    patron = "(A|B|C|D|)" 
    opcion = ""
    while True:
          opcion = input(mensaje).upper()
          correcto = re.fullmatch(patron,opcion)
          if not correcto:
             print("Error: Sólo debe ingresar A,B,C,D")
          else:
             break
    return opcion

def obtener_preguntas_aleatorias(preguntas_l, numero_preguntas_aleatorias):
    return random.sample(preguntas_l, numero_preguntas_aleatorias)

def main():
    menu()
          
if __name__ == "__main__":
   main()



'''
import random
preguntas_aleatorias_l = random.sample(preguntas_l,3)

for index,pregunta_d in enumerate(preguntas_aleatorias_l):
    print((index+1),":",pregunta_d['pregunta'])
'''