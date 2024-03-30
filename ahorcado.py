import random

# Lista de palabras para el juego
palabras = ['manzana', 'mango', 'naranja', 'pera', 'uva']

# Seleccionar una palabra aleatoria de la lista
palabra = random.choice(palabras)

intentos = []
intentos_incorrectos = []
max_intentos = 6

print(f"La palabra tiene {len(palabra)} letras.")
print(" ".join("_" * len(palabra)))

while True:
    letra = input("Adivina una letra: ").lower()

    if letra in intentos:
        print("Ya adivinaste esa letra antes.")
    else:
        intentos.append(letra)

        if letra in palabra:
            print("¡Correcto!")
        else:
            print(f"¡Incorrecto! La letra {letra} no está en la palabra.")
            intentos_incorrectos.append(letra)

            if len(intentos_incorrectos) == max_intentos:
                print(f"Fin del juego. Te quedaste sin intentos. La palabra era {palabra}.")
                break

        estado_palabra = ""
        for letra_palabra in palabra:
            if letra_palabra in intentos:
                estado_palabra += letra_palabra
            else:
                estado_palabra += "_"
        print(estado_palabra)

        if "_" not in estado_palabra:
            print("¡Felicidades! Adivinaste la palabra.")
            break

    print(f"Intentos incorrectos: {intentos_incorrectos}")
    print(f"Intentos restantes: {max_intentos - len(intentos_incorrectos)}")
