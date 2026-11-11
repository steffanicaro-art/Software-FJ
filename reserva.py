# Clase para gestionar las reservas de Software FJ

import logging
from excepciones import ReservaInvalidaError

class Reserva:

    def __init__(self, codigo, cliente, servicio, duracion):
        if not isinstance(codigo, str) or not codigo.strip():
            raise ReservaInvalidaError("Codigo de reserva obligatorio")

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ReservaInvalidaError("La duracion debe ser mayor que cero")

        self.__codigo = codigo
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"

        try:
            self.__costo = servicio.calcular_costo(duracion)
        except Exception as error:
            raise ReservaInvalidaError(
                "No fue posible calcular el costo"
            ) from error

    @property
    def codigo(self):
        return self.__codigo

    @property
    def estado(self):
        return self.__estado

    @property
    def costo(self):
        return self.__costo

    def confirmar(self):
        if self.__estado != "Pendiente":
            raise ReservaInvalidaError("La reserva no puede confirmarse")

        self.__estado = "Confirmada"
        logging.info("Reserva %s confirmada", self.__codigo)

    def cancelar(self):
        if self.__estado == "Cancelada":
            raise ReservaInvalidaError("La reserva ya fue cancelada")

        self.__estado = "Cancelada"
        logging.info("Reserva %s cancelada", self.__codigo)

    def procesar(self):
        try:
            if self.__estado != "Pendiente":
                raise ReservaInvalidaError(
                    "La reserva no esta pendiente"
                )

        except ReservaInvalidaError as error:
            logging.error("Error al procesar reserva: %s", error)
            raise

        else:
            self.confirmar()
            logging.info("Reserva procesada correctamente")

        finally:
            logging.info("Finalizo el procesamiento de la reserva")

    def mostrar_info(self):
        return (
            f"Reserva: {self.__codigo} | "
            f"Cliente: {self.__cliente.nombre} | "
            f"Servicio: {self.__servicio.nombre} | "
            f"Duracion: {self.__duracion} | "
            f"Costo: ${self.__costo:,.2f} | "
            f"Estado: {self.__estado}"
        )
