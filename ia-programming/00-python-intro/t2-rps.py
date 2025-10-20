import random
from enum import IntEnum

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
OPTIONS = [ROCK, PAPER, SCISSORS]

class OpcionInvalidaError(Exception):
    pass

class AccionJuego(IntEnum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

def evaluar_juego(usuario, computadora):
    if usuario == computadora:
        print("Empate!")
        return 0
    elif (
        (usuario == AccionJuego.ROCK and computadora == AccionJuego.SCISSORS) or
        (usuario == AccionJuego.PAPER and computadora == AccionJuego.ROCK) or
        (usuario == AccionJuego.SCISSORS and computadora == AccionJuego.PAPER)
    ):
        print("¡Ganaste!")
        return 1
    else:
        print("Perdiste!")
        return -1

def obtener_eleccion_usuario():
    print("Opciones:")
    for i, opcion in enumerate(OPTIONS):
        print(f"{i}: {opcion}")
    eleccion = input("Elige una opción (0, 1, 2): ")
    try:
        valor = int(eleccion)
        if valor not in [0, 1, 2]:
            raise OpcionInvalidaError("Opción fuera de rango.")
        return AccionJuego(valor)
    except (ValueError, OpcionInvalidaError):
        raise OpcionInvalidaError("Entrada inválida. Debes ingresar 0, 1 o 2.")

def obtener_accion_computadora_aleatoria():
    return AccionJuego(random.choice([0, 1, 2]))

def obtener_accion_ganadora(accion):
    if accion == AccionJuego.ROCK:
        return AccionJuego.PAPER
    elif accion == AccionJuego.PAPER:
        return AccionJuego.SCISSORS
    elif accion == AccionJuego.SCISSORS:
        return AccionJuego.ROCK

def obtener_accion_computadora(historial_usuario):
    if not historial_usuario:
        accion = obtener_accion_computadora_aleatoria()
        print(f"La computadora elige: {OPTIONS[accion]}")
        return accion
    from collections import Counter
    conteo = Counter(historial_usuario)
    accion_frecuente = conteo.most_common(1)[0][0]
    accion_ganadora = obtener_accion_ganadora(accion_frecuente)
    print(f"La computadora elige: {OPTIONS[accion_ganadora]}")
    return accion_ganadora

def jugar_otra_ronda():
    respuesta = input("¿Quieres jugar otra ronda? (s/n): ").strip().lower()
    return respuesta == "s"

def principal():
    historial_juegos = []
    historial_usuario = []
    while True:
        try:
            usuario = obtener_eleccion_usuario()
        except OpcionInvalidaError as e:
            print(e)
            continue
        computadora = obtener_accion_computadora(historial_usuario)
        resultado = evaluar_juego(usuario, computadora)
        historial_juegos.append((usuario, computadora, resultado))
        historial_usuario.append(usuario)
        if not jugar_otra_ronda():
            print("¡Gracias por jugar!")
            break

if __name__ == "__main__":
    principal()