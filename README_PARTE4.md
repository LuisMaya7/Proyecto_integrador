Laberinto Interactivo
Este es un programa simple en Python que te permite interactuar con un laberinto en la consola. Puedes moverte por el laberinto usando las teclas de flechas y llegar desde la posición inicial hasta la posición final.

Requisitos
Asegúrate de tener instalada la biblioteca keyboard antes de ejecutar el programa:

bash
Copy code
pip install keyboard
Uso
Ejecuta el script Python laberinto_interactivo.py.
bash
Copy code
python laberinto_interactivo.py
El laberinto se generará en la consola con un punto de inicio (.) y un punto final (.).

Utiliza las teclas de flechas (↑, ↓, ←, →) para moverte por el laberinto.

El objetivo es llegar al punto final para completar el laberinto.

Configuración del Laberinto
Puedes configurar el laberinto utilizando la página https://www.dcode.fr/maze-generator y ajustando las configuraciones según tus preferencias. Copia el laberinto generado en el código como el valor de la variable laberinto_str.

Notas
El carácter # representa las paredes en el laberinto.
El carácter . representa los caminos disponibles.
El carácter P representa tu posición en el laberinto.