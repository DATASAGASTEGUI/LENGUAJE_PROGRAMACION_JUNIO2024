import os
import random
import re

# BASE DE DATOS
# Lista de opciones disponibles en el juego
opciones = ['piedra', 'papel', 'tijera', 'lagarto', 'spock']

# Reglas de ganadores
# Un diccionario que define qué opciones ganan contra cuáles
ganador = {
    'piedra': ['tijera', 'lagarto'],  # Piedra gana a Tijera y Lagarto
    'papel': ['piedra', 'spock'],      # Papel gana a Piedra y Spock
    'tijera': ['papel', 'lagarto'],    # Tijera gana a Papel y Lagarto
    'lagarto': ['spock', 'papel'],     # Lagarto gana a Spock y Papel
    'spock': ['tijera', 'piedra']      # Spock gana a Tijera y Piedra
}

def menu():
    while True:
        # Limpia la consola según el sistema operativo
        os.system('cls' if os.name == 'nt' else 'clear')  
        print('MENU')
        print('(1) EMPEZAR A JUGAR')
        print('(2) SALIR')
        opcion = input('Ingrese opción: ')
        
        if opcion == '1':
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la consola nuevamente
            jugar()  # Llama a la función jugar
            os.system('pause')  # Pausa para que el jugador vea los resultados
        elif opcion == '2':
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la consola antes de salir
            print('Gracias por su visita: ADIOS')
            os.system('pause')  # Pausa antes de cerrar
            break  # Sale del bucle y termina el programa
        else:
            print('Opción no válida. Intente de nuevo.')  # Mensaje para opciones inválidas

def jugar():
    # Contadores para las victorias de cada jugador
    jugador_ganadas = 0
    computador_ganadas = 0

    for ronda in range(1, 11):  # Bucle para 10 rondas
        print(f'\nRonda {ronda} de 10:')
        jugador = entrada_opcion('Elige piedra, papel, tijera, lagarto o spock: ').lower()  # Obtiene la opción del jugador
        computador = random.choice(opciones)  # Elige una opción aleatoria para el computador
        print(f'El computador eligió: {computador}')
        
        if jugador == computador:  # Compara las elecciones
            print('¡Es un empate!')  # Mensaje de empate
        elif computador in ganador[jugador]:  # Comprueba si el jugador gana
            print('¡Ganaste esta ronda!')
            jugador_ganadas += 1  # Incrementa el contador del jugador
        else:
            print('¡Perdiste esta ronda!')
            computador_ganadas += 1  # Incrementa el contador del computador

    # Resultados finales después de las 10 rondas
    print(f'\nResultados finales tras 10 rondas:')
    print(f'Ganaste: {jugador_ganadas} veces')
    print(f'El computador ganó: {computador_ganadas} veces')

def entrada_opcion(mensaje): 
    # Patrón para validar la entrada del jugador
    patron = '(PIEDRA|PAPEL|TIJERA|LAGARTO|SPOCK|piedra|papel|tijera|lagarto|spock)'  
    while True:
        opcion = input(mensaje).strip()  # Solicita la entrada y elimina espacios en blanco
        if not re.fullmatch(patron, opcion):  # Valida la opción ingresada
            print('Error: Solo debe de ingresar PIEDRA, PAPEL, TIJERA, LAGARTO o SPOCK')
        else:
            return opcion.lower()  # Devuelve la opción en minúsculas

def main():
    menu()  # Inicia el menú principal

if __name__ == "__main__":
    main()  # Llama a la función main si el archivo se ejecuta directamente
