from typing import List
from typing import Tuple
from functools import reduce
from parte_5 import Juego, JuegoArchivo

def convertir_a_matriz(laberinto: str) -> List[List[str]]:
    matriz = list(map(list, laberinto.split('\n')))
    return matriz

def leer_mapa_desde_archivo(nombre_archivo: str) -> Tuple[List[List[str]], Tuple[int, int], Tuple[int, int]]:
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    filas, columnas = map(int, lineas[0].split())

    laberinto = reduce(lambda x, y: x + y, lineas[1:1 + filas]).strip()

    inicio = tuple(map(int, lineas[1 + filas].split()))
    fin = tuple(map(int, lineas[2 + filas].split()))

    matriz_laberinto = convertir_a_matriz(laberinto)

    return matriz_laberinto, inicio, fin
def main():
    juego_archivo = JuegoArchivo('ruta/del/directorio/con/mapas')

    juego_archivo.mostrar_mapa()

    while not juego_archivo.verificar_fin():
        direccion = input("Ingresa la dirección (arriba, abajo, izquierda, derecha): ")
        if juego_archivo.mover(direccion):
            juego_archivo.mostrar_mapa()

    print("¡Felicidades, has llegado al final!")

if __name__ == "__main__":
    main()