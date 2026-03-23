from abc import ABC, abstractmethod

class animal(ABC):
    def __init__(self,nombre,edad,raza,color,tamaño=float,peso=float):

        self.__nombre = nombre
        self.__edad = edad
        self.__raza = raza 
        self.__color = color
        self.__tamaño = tamaño
        self.__peso = peso

    @property 
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad

    @property
    def raza(self):
        return self.__raza