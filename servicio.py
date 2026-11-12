# Clases para gestionar los servicios de Software FJ

from abc import ABC, abstractmethod
from excepciones import DatosInvalidosError


class Servicio(ABC):

    def __init__(self, codigo, nombre, precio):

        if not isinstance(codigo, str) or not codigo.strip():
            raise DatosInvalidosError("Codigo obligatorio")

        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError("Nombre del servicio obligatorio")

        if (not isinstance(precio, (int, float))
                or isinstance(precio, bool) or precio <= 0):
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

    # Validar y calcular el costo
    def _calcular_total(self, cantidad, descuento, impuesto):

        if (not isinstance(cantidad, (int, float))
                or isinstance(cantidad, bool) or cantidad <= 0):
            raise DatosInvalidosError("Cantidad incorrecta")

        if (not isinstance(descuento, (int, float))
                or isinstance(descuento, bool) or not 0 <= descuento <= 100):
            raise DatosInvalidosError("Descuento incorrecto")

        if (not isinstance(impuesto, (int, float))
                or isinstance(impuesto, bool) or not 0 <= impuesto <= 100):
            raise DatosInvalidosError("Impuesto incorrecto")

        subtotal = cantidad * self._precio
        valor_descuento = subtotal * descuento / 100
        subtotal -= valor_descuento

        return subtotal + (subtotal * impuesto / 100)

    @abstractmethod
    def calcular_costo(self, cantidad=1, descuento=0, impuesto=0):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass


# Servicio de reserva de salas
class ReservaSala(Servicio):

    def calcular_costo(self, cantidad=1, descuento=0, impuesto=0):
        return self._calcular_total(cantidad, descuento, impuesto)

    def describir_servicio(self):
        return f"Reserva de sala: {self.nombre}"


# Servicio de alquiler de equipos
class AlquilerEquipo(Servicio):

    def calcular_costo(self, cantidad=1, descuento=0, impuesto=0):
        return self._calcular_total(cantidad, descuento, impuesto)

    def describir_servicio(self):
        return f"Alquiler de equipo: {self.nombre}"


# Servicio de asesoria especializada
class Asesoria(Servicio):

    def calcular_costo(self, cantidad=1, descuento=0, impuesto=0):
        return self._calcular_total(cantidad, descuento, impuesto)

    def describir_servicio(self):
        return f"Asesoria especializada: {self.nombre}"
