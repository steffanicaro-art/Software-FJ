# Programa principal del sistema SOFTWARE FJ

from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from gestor import Gestor
from excepciones import (
    DatosInvalidosError,
    ReservaInvalidaError,
    ClienteNoEncontradoError,
    ServicioNoDisponibleError
)

def ejecutar_sistema():

    sistema = Gestor()

    # Inicializar variables para evitar errores
    cliente1 = None
    reserva1 = None

    print("\n===================================")
    print("       SISTEMA SOFTWARE FJ")
    print("===================================")

    # OPERACION 1: Registrar primer cliente
    try:
        cliente1 = Cliente(
            "1001", "Carlos Perez", "3001234567",
            "carlos@gmail.com"
        )
        sistema.registrar_cliente(cliente1)
        print("\nCliente 1 registrado correctamente")

    except DatosInvalidosError as error:
        print("Error:", error)

    # OPERACION 2: Registrar segundo cliente
    try:
        cliente2 = Cliente(
            "1002", "Maria Lopez", "3109876543",
            "maria@gmail.com"
        )
        sistema.registrar_cliente(cliente2)
        print("Cliente 2 registrado correctamente")

    except DatosInvalidosError as error:
        print("Error:", error)

    # OPERACION 3: Intentar registrar cliente invalido
    try:
        cliente3 = Cliente("", "", "123", "correo")
        sistema.registrar_cliente(cliente3)

    except DatosInvalidosError as error:
        print("\nError controlado al registrar cliente:", error)

    # OPERACION 4: Crear servicio de sala
    try:
        sala = ReservaSala(
            "S01", "Sala de reuniones", 50000
        )
        sistema.registrar_servicio(sala)
        print("\nServicio de sala registrado")

    except DatosInvalidosError as error:
        print("Error:", error)

    # OPERACION 5: Crear servicio de equipos
    try:
        equipo = AlquilerEquipo(
            "E01", "Computador", 30000
        )
        sistema.registrar_servicio(equipo)
        print("Servicio de equipos registrado")

    except DatosInvalidosError as error:
        print("Error:", error)

    # OPERACION 6: Crear servicio de asesoria
    try:
        asesoria = Asesoria(
            "A01", "Asesoria tecnica", 80000
        )
        sistema.registrar_servicio(asesoria)
        print("Servicio de asesoria registrado")

    except DatosInvalidosError as error:
        print("Error:", error)

    # OPERACION 7: Intentar crear servicio invalido
    try:
        servicio_invalido = ReservaSala(
            "S02", "Sala", -500
        )
        sistema.registrar_servicio(servicio_invalido)

    except DatosInvalidosError as error:
        print("\nError controlado al crear servicio:", error)

    # OPERACION 8: Crear reserva correctamente
    try:
        reserva1 = sistema.crear_reserva(
            "R001", "1001", "S01", 2
        )
        print("\nReserva creada:", reserva1.codigo)

    except (
        ReservaInvalidaError,
        ClienteNoEncontradoError,
        ServicioNoDisponibleError
    ) as error:
        print("Error:", error)

    # OPERACION 9: Procesar y confirmar reserva
    try:
        if reserva1 is not None:
            reserva1.procesar()
            print("Reserva confirmada correctamente")
        else:
            print("No se puede procesar: reserva inexistente")

    except ReservaInvalidaError as error:
        print("Error:", error)

    # OPERACION 10: Intentar registrar cliente duplicado
    try:
        if cliente1 is not None:
            sistema.registrar_cliente(cliente1)

    except DatosInvalidosError as error:
        print("\nError controlado:", error)

    # OPERACION 11: Intentar reservar con cliente inexistente
    try:
        sistema.crear_reserva(
            "R002", "9999", "S01", 1
        )

    except (
        ReservaInvalidaError,
        ClienteNoEncontradoError,
        ServicioNoDisponibleError
    ) as error:
        print("Error controlado:", error)

    # OPERACION 12: Cancelar reserva
    try:
        if reserva1 is not None:
            reserva1.cancelar()
            print("\nReserva cancelada correctamente")

    except ReservaInvalidaError as error:
        print("Error:", error)

    # OPERACION 13: Intentar reservar con servicio inexistente
    try:
        sistema.crear_reserva(
            "R003", "1001", "S99", 1
        )

    except (
        ReservaInvalidaError,
        ClienteNoEncontradoError,
        ServicioNoDisponibleError
    ) as error:
        print("\nError controlado:", error)

    # Mostrar informacion del sistema
    print("\n========== CLIENTES ==========")
    sistema.listar_clientes()

    print("\n========== SERVICIOS ==========")
    sistema.listar_servicios()

    print("\n========== RESERVAS ==========")
    sistema.listar_reservas()

    print("\n===================================")
    print("   PRUEBAS DEL SISTEMA FINALIZADAS")
    print("===================================")

if __name__ == "__main__":
    ejecutar_sistema()
