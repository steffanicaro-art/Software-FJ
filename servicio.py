# Clases para gestionar los servicios de Software FJ

from abc import ABC, abstractmethod
from excepciones import DatosInvalidosError

class Servicio(ABC):

    def __init__(self, codigo, nombre, precio):
        if not isinstance(codigo, str) or not codigo.strip():
            raise DatosInvalidosError("Codigo de servicio obligatorio")

        if not isinstance(precio, (int, float)) or isinstance(precio, bool) or precio <= 0:
            raise DatosInvalidosError("El precio debe ser mayor que cero")

        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @abstractmethod
    def calcular_costo(self, cantidad=1, descuento=0):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

class ReservaSala(Servicio):

    def calcular_costo(self, cantidad=1, descuento=0):
        if cantidad <= 0 or not 0 <= descuento <= 100:
            raise DatosInvalidosError("Cantidad o descuento incorrecto")
        return cantidad * self._precio * (1 - descuento / 100)

    def describir_servicio(self):
        return f"Reserva de sala: {self.nombre}"

class AlquilerEquipo(Servicio):

    def calcular_costo(self, cantidad=1, descuento=0):
        if cantidad <= 0 or not 0 <= descuento <= 100:
            raise DatosInvalidosError("Cantidad o descuento incorrecto")
        return cantidad * self._precio * (1 - descuento / 100)

    def describir_servicio(self):
        return f"Alquiler de equipo: {self.nombre}"

class Asesoria(Servicio):

    def calcular_costo(self, cantidad=1, descuento=0):
        if cantidad <= 0 or not 0 <= descuento <= 100:
            raise DatosInvalidosError("Cantidad o descuento incorrecto")
        return cantidad * self._precio * (1 - descuento / 100)

    def describir_servicio(self):
        return f"Asesoria especializada: {self.nombre}"
