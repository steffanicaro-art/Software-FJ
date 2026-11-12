# Administrador general del sistema SOFTWARE FJ

import logging
import os

from reserva import Reserva
from excepciones import (
    DatosInvalidosError,
    ReservaInvalidaError,
    ClienteNoEncontradoError,
    ServicioNoDisponibleError
)

# Crear carpeta para almacenar los registros
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

class Gestor:

    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    # Registrar clientes
    def registrar_cliente(self, cliente):
        if any(c.identificacion == cliente.identificacion
               for c in self.clientes):
            logging.warning("Intento de registrar cliente duplicado")
            raise DatosInvalidosError("El cliente ya existe")

        self.clientes.append(cliente)
        logging.info("Cliente registrado: %s", cliente.identificacion)

    # Registrar servicios
    def registrar_servicio(self, servicio):
        if any(s.codigo == servicio.codigo
               for s in self.servicios):
            logging.warning("Intento de registrar servicio duplicado")
            raise DatosInvalidosError("El servicio ya existe")

        self.servicios.append(servicio)
        logging.info("Servicio registrado: %s", servicio.codigo)

    # Crear reservas
    def crear_reserva(self, codigo, identificacion,
                      codigo_servicio, duracion):

        try:
            cliente = next(
                (c for c in self.clientes
                 if c.identificacion == identificacion), None
            )

            if cliente is None:
                raise ClienteNoEncontradoError(
                    "El cliente no existe"
                )

            servicio = next(
                (s for s in self.servicios
                 if s.codigo == codigo_servicio), None
            )

            if servicio is None:
                raise ServicioNoDisponibleError(
                    "El servicio no existe o no esta registrado"
                )

            if any(r.codigo == codigo for r in self.reservas):
                raise ReservaInvalidaError(
                    "El codigo de reserva ya existe"
                )

            reserva = Reserva(
                codigo, cliente, servicio, duracion
            )

            self.reservas.append(reserva)

        except (
            ClienteNoEncontradoError,
            ServicioNoDisponibleError,
            ReservaInvalidaError
        ) as error:
            logging.exception("Error al crear la reserva")
            raise

        except Exception as error:
            logging.exception("Error inesperado al crear reserva")
            raise ReservaInvalidaError(
                "No fue posible completar la reserva"
            ) from error

        else:
            logging.info("Reserva creada: %s", codigo)
            return reserva

        finally:
            logging.info("Finalizo el proceso de creacion de reserva")

    # Consultar clientes
    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente.mostrar_info())

    # Consultar servicios
    def listar_servicios(self):
        for servicio in self.servicios:
            print(servicio.describir_servicio())

    # Consultar reservas
    def listar_reservas(self):
        for reserva in self.reservas:
            print(reserva.mostrar_info())
