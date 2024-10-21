import os, random
from misclases import Circulo, area

def ejemplo1():
    c1 = Circulo(random.randint(1,10))
    print("Radio: ", c1.radio)
    c1.radio = 5
    print("Radio: ", c1.radio)

def ejemplo2():
    lista_objetos = []
    for i in range(100):
        c = Circulo(random.randint(1,10))
        lista_objetos.append(c)

    i = 0
    for objeto in lista_objetos:
        i = i + 1
        print(f"Objeto {i} : ", objeto.radio)

def ejemplo3():
    c1 = Circulo(random.randint(1,10))
    print(c1.get_radio())
    # print(c1.__radio) no se puede porque es privado
    c1.set_radio(20)
    print(c1.get_radio())

def ejemplo4():
    radio = int(input('Ingresar radio? '))
    c = Circulo(radio)
    print("Radio: ", c.get_radio())
    print("Area : ", c.area())
    print(c)

    print("Area (llamar función): ", area(radio))

def main():
    ejemplo4()
          
if __name__ == "__main__":
   main()