import os, random, re

def menu():
    while True:
          os.system('cls')
          print('MENU')
          print('(1) JUGAR PIEDRA-PAPEL-TIJERA')
          print('(2) SALIR')

          opcion = input('INGRESE OPCION? ')

          if opcion == '1':
             os.system('cls');jugar();os.system('pause')
          elif opcion == '2':
             os.system('cls')
             print('Gracias por si visita. ADIOS')
             os.system('pause')
             break
          
def jugar():
    numero_jugadas = int(input('Cuantas jugadas desea realizar? '))
    empate = 0; ganador=0; perdedor=0
    for i in range(numero_jugadas):
        maquina = random.choice(['piedra','papel','tijera'])
        usuario = entrada_usuario('Número Jugada (piedra-papel-tiera): ' + str((i+1)) + " : ")
        resultado = obtener_resultado_juego(usuario,maquina)
        if resultado == 'Empate':
           empate += 1
        elif resultado == 'Ganar':
           ganador += 1
        else:
           perdedor += 1
    print("Empate   : ", empate)
    print("Ganastes : ", ganador)
    print("Perdistes: ", perdedor)
        
def entrada_usuario(mensaje):
    patron = "(piedra|tijera|papel)"
    cadena = ""
    while True:
          cadena = input(mensaje).lower()
          correcto = re.fullmatch(patron, cadena)
          if not correcto:
             print('Error: Debe ingresar papel, tijera, piedra')
          else:
             break
    return cadena

def obtener_resultado_juego(usuario,maquina):
    if usuario == maquina:
       return "Empate"
    elif (usuario == 'piedra' and maquina == 'tijera') or \
         (usuario == 'papel' and maquina == 'piedra') or \
         (usuario == 'tijera' and maquina == 'papel'):
         return "Ganar"
    else:
         return "Perder"
    
def main():
    menu()
          
if __name__ == "__main__":
   main()


