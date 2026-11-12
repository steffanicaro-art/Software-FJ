# Clase para gestionar los clientes de Software FJ

from entidad import Entidad
from excepciones import DatosInvalidosError


class Cliente(Entidad):

    def __init__(self, identificacion, nombre, telefono, correo):
        if not isinstance(identificacion, str) or not identificacion.strip():
            raise DatosInvalidosError("Identificacion obligatoria")

        if not isinstance(nombre, str) or not nombre.strip():
            raise DatosInvalidosError("El nombre es obligatorio")

        if not isinstance(telefono, str) or not telefono.isdigit() or len(telefono) < 7:
            raise DatosInvalidosError("Telefono incorrecto")

        if not isinstance(correo, str) or "@" not in correo or "." not in correo:
            raise DatosInvalidosError("Correo electronico incorrecto")

        super().__init__(identificacion.strip())

        self.__nombre = nombre.strip()
        self.__telefono = telefono
        self.__correo = correo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def telefono(self):
        return self.__telefono

    @property
    def correo(self):
        return self.__correo

    def mostrar_info(self):
        return (
            f"ID: {self.identificacion} | "
            f"Nombre: {self.__nombre} | "
            f"Telefono: {self.__telefono} | "
            f"Correo: {self.__correo}"
        )
