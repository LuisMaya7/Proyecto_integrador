Proyecto Integrador Parte 5: Juego de Laberinto Orientado a Objetos
Introducción
Este proyecto se enfoca en la implementación de un juego de laberinto utilizando programación orientada a objetos en Python. A lo largo de las diferentes partes del proyecto, se han desarrollado funcionalidades para el manejo de mapas, movimientos del jugador, y la capacidad de cargar mapas desde archivos externos.

Parte 5: Encapsulando el juego en una clase y Almacenando mapas en archivos
En esta parte del proyecto, se introduce la encapsulación del juego en una clase llamada Juego. Esta clase tiene atributos para el mapa, las posiciones inicial y final del jugador, así como métodos para mostrar el mapa, mover al jugador y verificar si ha llegado al final.

Adicionalmente, se crea la clase JuegoArchivo que hereda de Juego. Esta clase se encarga de leer mapas desde archivos externos, proporcionando una mayor modularidad y separación de los datos del juego.

Instrucciones
Clase Juego
Constructor (__init__): Recibe el mapa, las posiciones inicial y final como parámetros y los almacena como atributos de la clase.

mostrar_mapa(self): Método para imprimir en consola el estado actual del mapa.

mover(self, direccion): Método que permite al jugador moverse en el laberinto en la dirección especificada. Verifica si el movimiento es válido y actualiza la posición del jugador en consecuencia.

verificar_fin(self): Método que devuelve True si el jugador ha llegado al final del laberinto, False en caso contrario.

Clase JuegoArchivo
Constructor (__init__): Recibe la ruta del directorio que contiene los mapas. Lista los archivos disponibles y elige uno al azar para inicializar el juego.

leer_mapa_aleatorio(self, path_a_mapas): Método privado que lee un mapa aleatorio desde un archivo. Se encarga de procesar el contenido del archivo y devolver los datos necesarios para inicializar el juego.

Uso desde el main
python
Copy code
# Importar las clases
from juego import Juego, JuegoArchivo

# Crear instancia de JuegoArchivo con la ruta al directorio de mapas
juego_archivo = JuegoArchivo('ruta/del/directorio/con/mapas')

# Mostrar el mapa inicial
juego_archivo.mostrar_mapa()

# Bucle principal del juego
while not juego_archivo.verificar_fin():
    direccion = input("Ingresa la dirección (arriba, abajo, izquierda, derecha): ")
    if juego_archivo.mover(direccion):
        juego_archivo.mostrar_mapa()

# Mensaje de victoria al llegar al final del laberinto
print("¡Felicidades, has llegado al final!")
Notas adicionales
Asegúrate de tener el directorio juegos con los archivos de mapa en el mismo directorio que tu script principal.

Se han añadido mensajes de depuración en las clases para facilitar la identificación de posibles problemas.

En caso de errores o comportamientos inesperados, revisa la consola para mensajes de depuración que puedan ayudarte a entender el problema.