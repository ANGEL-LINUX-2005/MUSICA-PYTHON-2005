# -*- coding: utf-8 -*-

import subprocess
titulo = "MUSICA DE CALIDAD"
print(titulo.center(120))
LOGO = '''
                   ____ 
                .-'    `-.
               /_...._   \\
               || ||||   |
               || ||||   |
              (|| ||||   |
              || ||||   |
              || ||||   |
             / ||||||   |
           .'  ||||||   |
        _.'    | ||||   |
     .-'       | ||||   |
    /          | ||||   |
   |    .-.    | ||||   |
   \\   (   )   | ||||   |
    '-.__.'    |______.-'
               |_| |_| 
             VV-Linux
'''

for linea in LOGO.strip('\n').split('\n'):
    print(linea.center(120))

print('-----------------------------------------------------------')

# Solicitar el URL del video
url = input("Ingrese el URL del video de musica: ")

# Solicitar la ruta donde se guardara la musica
output_path = input("Ingrese la ruta donde se guardara la musica: ")
if not output_path.strip():
    output_path = "."

# Construir el comando para descargar solo la música en formato MP3
command = [
    "yt-dlp",
    "--extract-audio",             # Extraer solo el audio
    "--audio-format", "mp3",       # Convertir a formato MP3
    "--audio-quality", "0",        # Mejor calidad posible
    "-o", f"{output_path}/%(title)s.%(ext)s",  # Definir nombre del archivo
    url
]

# Ejecutar el comando
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Leer la salida y los errores
stdout, stderr = process.communicate()

# Mostrar la salida y errores
if stdout:
    print(stdout)
if stderr:
    print(stderr)

# Verificar el código de salida
if process.returncode == 0:
    print("Musica descargada exitosamente.")
else:
    print("Error en la descarga de la musica.")
