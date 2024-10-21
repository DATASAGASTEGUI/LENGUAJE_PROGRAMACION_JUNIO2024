from abc import ABC, abstractmethod
from tabulate import tabulate

class SeleccionFutbol:

      def __init__(self, id_seleccionfutbol, nombre, apellidos, edad):
            self.id_seleccionfutbol = id_seleccionfutbol
            self.nombre = nombre
            self.apellidos = apellidos
            self.edad = edad

      @abstractmethod
      def consentrarse(self): # Polimorfismo: Cada hijo lo implementa de manera distinta
          pass
      
      @abstractmethod
      def viajar(self): # Polimorfismo: Cada hijo lo implementa de manera distinta
          pass
      
class Futbolista(SeleccionFutbol):
      
      def __init__(self, id_seleccionfutbol, nombre, apellidos, edad, dorsal, demarcacion):
          super().__init__(id_seleccionfutbol, nombre, apellidos, edad)
          self.dorsal = dorsal
          self.demarcacion = demarcacion

      def jugar_partido():
          pass
      
      def entrenar():
          pass

class Entrenador(SeleccionFutbol):
      
      def __init__(self, id_seleccionfutbol, nombre, apellidos, edad, id_federacion):
          super().__init__(id_seleccionfutbol, nombre, apellidos, edad)
          self.id_federacion = id_federacion

      def dirigir_partido():
          pass
      
      def dirigir_entrenamiento():
          pass

class Masajista(SeleccionFutbol):

      def __init__(self, id_seleccionfutbol, nombre, apellidos, edad, titulacion, anio_experiencia):
          super().__init__(id_seleccionfutbol, nombre, apellidos, edad)
          self.titulacion = titulacion
          self.anio_experiencia = anio_experiencia
      
      def dar_masaje():
          pass