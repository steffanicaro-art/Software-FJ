# Excepciones personalizadas del sistema SOFTWARE FJ

class DatosInvalidosError(Exception):
    """Error cuando los datos ingresados no son validos."""
    pass

class ServicioNoDisponibleError(Exception):
    """Error cuando un servicio no esta disponible."""
    pass

class ReservaInvalidaError(Exception):
    """Error cuando una reserva no cumple las condiciones."""
    pass

class ClienteNoEncontradoError(Exception):
    """Error cuando el cliente no existe en el sistema."""
    pass

class OperacionNoPermitidaError(Exception):
    """Error cuando se intenta realizar una operacion no permitida."""
    pass
