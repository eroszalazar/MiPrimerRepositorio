import random

def obtener_palabra():
    palabras = ["python", "programacion", "desarrollo", "codigo", "computadora"]
    return random.choice(palabras)

def mostrar_tablero(palabra, intentos):
    print("\nIntentos restantes: {}".format(7 - intentos))
    print("Palabra: {}".format(palabra))
    print("")

def jugar_ahorcado():
    palabra = obtener_palabra()
    palabra_oculta = "_" * len(palabra)
    intentos = 0
    letras_adivinadas = []
    
    print("¡Bienvenido al juego del ahorcado!")
    mostrar_tablero(palabra_oculta, intentos)
    
    while True:
        letra = input("Ingresa una letra: ").lower()
        
        if letra in letras_adivinadas:
            print("Ya has intentado con esa letra. ¡Intenta con otra!")
            continue
        
        letras_adivinadas.append(letra)
        
        if letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    palabra_oculta = palabra_oculta[:i] + letra + palabra_oculta[i+1:]
        else:
            intentos += 1
        
        mostrar_tablero(palabra_oculta, intentos)
        
        if intentos == 7:
            print("¡Oh no! ¡Perdiste! La palabra correcta era '{}'.".format(palabra))
            break
        
        if "_" not in palabra_oculta:
            print("¡Felicidades! ¡Ganaste!")
            break
    
    jugar_de_nuevo = input("¿Deseas jugar de nuevo? (s/n): ")
    if jugar_de_nuevo.lower() == "s":
        jugar_ahorcado()

# Iniciar el juego
jugar_ahorcado()
