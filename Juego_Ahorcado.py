import random


def obtener_palabra_secreta():
    palabras = [
        "python",
        "java",
        "javascript",
        "angular",
        "django",
        "tensorflow",
        "react",
        "typescript",
        "git",
        "flask",
    ]
    return random.choice(palabras)


def mostrar_proceso(palabra_secreta, letras_adivinadas):
    adivinado = ""

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"
    return adivinado


def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False

    print("Bienvenido al juego del ahorcado")
    print(f"Tienes {intentos} intentos para adivinar la palabra secreta")
    print(mostrar_proceso(palabra_secreta, letras_adivinadas), "La palabra secreta tiene:", len(palabra_secreta), "letras")

    while not juego_terminado and intentos > 0:
        adivinanza = input("Introduce una letra: ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor introduzca una letra validad(Solo escribir 1 letra por intentos)")

        elif adivinanza in letras_adivinadas:
            print("Ya has utilizado esa letra prueba otra")

        else:
            letras_adivinadas.append(adivinanza)

            if adivinanza in palabra_secreta:
                print(f"Haz acertado, la letra '{adivinanza}' es una letra de la palabra")
            else:
                intentos -= 1
                print(f"Fallaste, la letra '{adivinanza}' no es una letra de la palabra ")
                print(f"Te quedan '{intentos}'","intentos")

        proceso_actual = mostrar_proceso(palabra_secreta, letras_adivinadas)
        print(proceso_actual)

        if "_" not in proceso_actual:
            juego_terminado = True
            print(f"¡Has ganado! La palabra completa es: '{palabra_secreta.capitalize()}'")

    if intentos == 0:
        print(f"¡Has perdido! se te acabaron los intentos. la palabra era '{palabra_secreta.capitalize()}'")


juego_ahorcado()
