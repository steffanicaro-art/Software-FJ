from abc import ABC, abstractmethod


class Entidad(ABC):

    def __init__(self, identificacion):
        self._identificacion = identificacion

    @property
    def identificacion(self):
        return self._identificacion

    @abstractmethod
    def mostrar_info(self):
        pass
