
#!PARA EJECUTAR EL CODIGO INSALAR LA BIBLIOETACA keybord CON 'pip install keyboard'

import os
import keyboard
from typing import List, Tuple

def generar_laberinto(mapa_str: str, end: int) -> List[List[str]]:

    mapa_str = mapa_str.replace('#.\n', '##\n')
    mapa_str += '#' * (end + 1)
    
   
    laberinto = [list(fila) for fila in mapa_str.split("\n")]
    
    return laberinto

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_laberinto(mapa: List[List[str]]):
    limpiar_pantalla()
    for fila in mapa:
        print("".join(fila))

def main_loop(mapa: List[List[str]], pos_inicial: Tuple[int, int], pos_final: Tuple[int, int]):
    px, py = pos_inicial
    
    while (px, py) != pos_final:
        
        mapa[py][px] = 'P'
        mostrar_laberinto(mapa)
        
        tecla = keyboard.read_event(suppress=True).name
         
        nueva_px, nueva_py = px, py
        if tecla == 'up':
            nueva_py -= 1
        elif tecla == 'down':
            nueva_py += 1
        elif tecla == 'left':
            nueva_px -= 1
        elif tecla == 'right':
            nueva_px += 1

        if 0 <= nueva_px < len(mapa[0]) and 0 <= nueva_py < len(mapa) and mapa[nueva_py][nueva_px] != '#':
            mapa[py][px] = '.'
            px, py = nueva_px, nueva_py

if __name__ == "__main__":
    laberinto_str = "##########\n#........#\n#........#\n#........#\n#........#\n#........#\n#........#\n#........#\n#........#\n##########"
    end = 9
    laberinto = generar_laberinto(laberinto_str, end)
    pos_inicial = (0, 0)
    pos_final = (end, end)

    main_loop(laberinto, pos_inicial, pos_final)
