import readchar

def leer_caracter():
    key = readchar.readchar()
    return key

while True:
   print("Presiona una tecla (sal con la flecha hacia arriba)")
   caracter = leer_caracter()
   print(f"Tecla presionada: {caracter}")
   
   if caracter == "\x1b[A":
       print("Se presionó la flecha hacia arriba. Saliendo...")
       break
