# Administrador general del sistema SOFTWARE FJ

import logging
import os

from reserva import Reserva
from excepciones import (
    DatosInvalidosError,
    ReservaInvalidaError,
    ClienteNoEncontradoError
)

# Crear carpeta y archivo de registros
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8,
)

class Gestor:

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def registrar_cliente(self, cliente):
        if any(c.identificacion == cliente.identificacion
               for c in self.clientes):
            raise DatosInvalidosError("El cliente ya existe")

        self.clientes.append(cliente)
        logging.info("Cliente registrado: %s", cliente.identificacion)

    def registrar_servicio(self, servicio):
        if any(s.codigo == servicio.codigo
               for s in self.servicios):
            raise DatosInvalidosError("El servicio ya existe")

        self.servicios.append(servicio)
        logging.info("Servicio registrado: %s", servicio.codigo)

    def crear_reserva(self, codigo, identificacion, codigo_servicio, duracion):
        try:
            cliente = next(
                c for c in self.clientes
                if c.identificacion == identificacion
            )

            servicio = next(
                s for s in self.servicios
                if s.codigo == codigo_servicio
            )

            if any(r.codigo == codigo for r in self.reservas):
                raise ReservaInvalidaError("Codigo de reserva duplicado")

            reserva = Reserva(codigo, cliente, servicio, duracion)
            self.reservas.append(reserva)

        except StopIteration as error:
            logging.exception("Cliente o servicio no encontrado")
            raise ClienteNoEncontradoError(
                "No se encontro el cliente o servicio"
            ) from error

        except Exception as error:
            logging.exception("Error al crear la reserva")
            if isinstance(error, ReservaInvalidaError):
                raise
            raise ReservaInvalidaError(
                "No fue posible crear la reserva"
            ) from error

        else:
            logging.info("Reserva creada: %s", codigo)
            return reserva

    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente.mostrar_info())

    def listar_servicios(self):
        for servicio in self.servicios:
            print(servicio.describir_servicio())

    def listar_reservas(self):
        for reserva in self.reservas:
            print(reserva.mostrar_info())
