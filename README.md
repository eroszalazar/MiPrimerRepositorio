# MiPrimerRepositorio
Este es mi primer repositorio, es el juego Ahorcado echo con el lenguaje de programación Python.
  Es una explición de cada codigo que eh echo.
  
                                      Ahorcado

import random: Me sirve para poder elegir aleatoriamente la palabra que haya puesto en el juego.
def obtener_palabra(): creo la funcion de “obtener_palabra” que es para que me proporcione la palabra aleatoria al jugar.

def mostrar_tablero(palabra, intentos): creo la función “mostrar_tablero” que es donde se me mostrara mis intentos restantes y la dicha palabra de juego.
def jugar_ahorcado(): creo la función “jugar_ahorcado” que es donde está todo mi código de juego.
	while true: creo el bucle infinito que corta al terminar el juego (ganándolo, perdiéndolo).
		if (tal cosa) in (otra cosa): es que si esta cosa esta dentro de la otra.
		if letra in letras_adivinadas: si mi letra es igual a a la anterior.
		letras_adivinadas.append(letras): que se agregue a la lista de letra adivinadas.
		if letra in palabra: si mi letra esta en esa palabra.
			for i in range(len(palabra)): está recorriendo la palabra letra por letra para comparar cada letra con la que has ingresado.
				if palabra[i] == letra: si mi letra se encuentra en la palaba que cumpla la función.
					Palabra_oculta = sustituir el “_“ por la letra
			
 		mostrar_tablero(palabra_oculta, intentos): luego de cada letra asignada se muestra el tablero.
		if intentos == 7: básicamente perdi si tuve 7 intentos fallidos
		if ”_” not in palabra_oculta: si ya no estan mas las “_” me da como ganado.

jugar_de_nuevo = pregunta de volver a jugar (s/n)
if jugar_de_nuevo.lower == dependiendo de la respuesta “(s/n)” se jugara de nuevo o no.
	jugar_ahorcado(): responsable de volver a jugar si se cumple ese “if” 

jugar_ahorcado(): inicio del juego
