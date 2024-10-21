import math

class Circulo:

      # CONSTRUCTOR (INICIALIZAR LOS ATRIBUTOS OBJETO)
      def __init__(self, radio):
          self.__radio = radio # publico sin raya, privado con raya

      def set_radio(self, radio):
          self.__radio = radio

      def get_radio(self):
          return self.__radio
      
      def area(self):
          return math.pi * self.__radio * self.__radio
          # return math.pi() * self.radio ** 2
          # return math.pi() * math.pow(self.radio,2)
      
      def __str__(self):
          return f'Radio: {self.__radio} Area: {self.area()}' # return "Radio:" + str(self.radio)
      
def area(radio):
    return math.pi * math.pow(radio,2)

