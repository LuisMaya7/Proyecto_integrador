import os
import random
from pathlib import Path

class Juego:
    def __init__(self, mapa, inicio, fin):
        self.mapa = mapa
        self.inicio = inicio
        self.fin = fin
        self.px, self.py = inicio

    def mostrar_mapa(self):
        for i, fila in enumerate(self.mapa):
            print(f"{i}: {''.join(fila)}")

    def mover(self, direccion):
        dx, dy = 0, 0
        if direccion == "arriba":
            dx = -1
        elif direccion == "abajo":
            dx = 1
        elif direccion == "izquierda":
            dy = -1
        elif direccion == "derecha":
            dy = 1

        new_px, new_py = self.px + dx, self.py + dy

        if 0 <= new_px < len(self.mapa) and 0 <= new_py < len(self.mapa[0]) and self.mapa[new_px][new_py] != "#":
            self.mapa[self.px][self.py] = "."
            self.px, self.py = new_px, new_py
            self.mapa[self.px][self.py] = "P"
            return True
        else:
            return False

    def verificar_fin(self):
        return (self.px, self.py) == self.fin


class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        mapa, inicio, fin = self.leer_mapa_aleatorio(path_a_mapas)
        super(JuegoArchivo, self).__init__(mapa, inicio, fin)

    def leer_mapa_aleatorio(self, path_a_mapas):
        archivos = os.listdir(path_a_mapas)

        if not archivos:
            raise FileNotFoundError("No hay archivos en el directorio especificado.")

        nombre_archivo = random.choice(archivos)
        path_completo = Path(path_a_mapas) / nombre_archivo

        print(f"Leyendo mapa desde: {path_completo}")

        with open(path_completo, 'r') as archivo_mapa:
            contenido = archivo_mapa.readlines()

        print("Contenido leído:")
        print("".join(contenido))

        if len(contenido) < 3:
            raise ValueError("El archivo de mapa debe contener al menos tres líneas.")

        dimensiones = contenido[0].split()
        if len(dimensiones) != 2:
            raise ValueError("Las dimensiones del mapa deben especificarse como dos números en la primera línea.")

        filas, columnas = int(dimensiones[0]), int(dimensiones[1])

        if len(contenido) < 1 + filas + 1:
            raise ValueError("Las dimensiones del mapa no coinciden con el contenido del archivo.")

        mapa = [linea.strip() for linea in contenido[1:1 + filas]]
        inicio = tuple(map(int, contenido[1 + filas].split()))
        fin = tuple(map(int, contenido[2 + filas].split()))

        print("Mapa leído:")
        for fila in mapa:
            print(fila)

        return mapa, inicio, fin

# EJEMPLO
try:
    juego = JuegoArchivo('ruta/del/directorio/con/mapas')
    juego.mostrar_mapa()

    while not juego.verificar_fin():
        direccion = input("Ingresa la dirección (arriba, abajo, izquierda, derecha): ")
        if juego.mover(direccion):
            juego.mostrar_mapa()

    print("¡Felicidades, has llegado al final!")
except Exception as e:
    print(f"Error: {e}")

