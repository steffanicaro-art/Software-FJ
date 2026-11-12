# Clase para gestionar las reservas de Software FJ

import logging
from excepciones import ReservaInvalidaError

class Reserva:

    def __init__(self, codigo, cliente, servicio, duracion,
                 descuento=0, impuesto=0):

        if not isinstance(codigo, str) or not codigo.strip():
            raise ReservaInvalidaError("Codigo de reserva obligatorio")

        if (not isinstance(duracion, (int, float))
                or isinstance(duracion, bool) or duracion <= 0):
            raise ReservaInvalidaError("Duracion incorrecta")

        if not hasattr(cliente, "nombre"):
            raise ReservaInvalidaError("Cliente no valido")

        if not callable(getattr(servicio, "calcular_costo", None)):
            raise ReservaInvalidaError("Servicio no valido")

        self.__codigo = codigo
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"

        try:
            self.__costo = servicio.calcular_costo(
                duracion, descuento, impuesto
            )

        except Exception as error:
            logging.exception("Error al calcular el costo")
            raise ReservaInvalidaError(
                "No fue posible calcular el costo"
            ) from error

        logging.info("Reserva creada: %s", codigo)

    @property
    def codigo(self):
        return self.__codigo

    @property
    def estado(self):
        return self.__estado

    @property
    def costo(self):
        return self.__costo

    @property
    def duracion(self):
        return self.__duracion

    # Confirmar reserva
    def confirmar(self):
        if self.__estado != "Pendiente":
            raise ReservaInvalidaError(
                "La reserva no puede confirmarse"
            )

        self.__estado = "Confirmada"
        logging.info("Reserva %s confirmada", self.__codigo)

    # Cancelar reserva
    def cancelar(self):
        if self.__estado == "Cancelada":
            raise ReservaInvalidaError(
                "La reserva ya fue cancelada"
            )

        self.__estado = "Cancelada"
        logging.info("Reserva %s cancelada", self.__codigo)

    # Procesar reserva
    def procesar(self):
        try:
            if self.__estado != "Pendiente":
                raise ReservaInvalidaError(
                    "La reserva no esta pendiente"
                )

        except ReservaInvalidaError:
            logging.exception("Error al procesar la reserva")
            raise

        else:
            self.confirmar()
            logging.info("Reserva procesada correctamente")

        finally:
            logging.info(
                "Finalizo el procesamiento de la reserva"
            )

    # Mostrar informacion
    def mostrar_info(self):
        return (
            f"Reserva: {self.__codigo} | "
            f"Cliente: {self.__cliente.nombre} | "
            f"Servicio: {self.__servicio.nombre} | "
            f"Duracion: {self.__duracion} | "
            f"Costo: ${self.__costo:,.2f} | "
            f"Estado: {self.__estado}"
        )
