import random


def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("Bienvenido al juego adivinanza")
    print("Debes adivinar un numero entre el 1 y el 100")
    print("Intenta adivinarlo")

    while not adivinado:
        adivinanza = input("Introduce un número del 1 al 100: ")

        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El numero secreto es mayor a {adivinanza}")

            elif adivinanza > numero_secreto:
                print(f"El numero secreto es menor a {adivinanza}")

            else:
                print(
                    f"Felicitaciones has ganado, El numero {adivinanza} es el secreto y los has logrado en {intentos}"
                )

        else:
            print("Introduzca un  umero valido entre el 1 y el 100")


juego_adivinanza()
