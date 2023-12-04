import subprocess
import threading
import os
import yt_dlp

def descargar_y_reproducir_video(video_url):
    # Configuración de yt_dlp para descargar en la mejor calidad en un único archivo
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'video_descargado.%(ext)s',
        'merge_output_format': 'mp4',
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Descargar el video
        ydl.download([video_url])

def reproducir_video(video_filename):
    # Usar subprocess para abrir un reproductor de video sin interfaz gráfica
    reproducir_comando = [
        'cvlc', '--no-xlib', '--play-and-exit', video_filename
    ]
    subprocess.run(reproducir_comando)

if __name__ == "__main__":
    # Solicitar la URL del video
    video_url = input("Ingresa la URL del video de YouTube: ")

    # Crear un hilo para la descarga y reproducción en paralelo
    hilo_descarga_y_reproduccion = threading.Thread(target=descargar_y_reproducir_video, args=(video_url,))

    # Iniciar el hilo
    hilo_descarga_y_reproduccion.start()

    # Esperar un momento antes de iniciar la reproducción para permitir que se descargue algo del contenido
    # Puedes ajustar este tiempo según sea necesario
    esperar_segundos = 5
    print(f'Esperando {esperar_segundos} segundos antes de iniciar la reproducción...')
    hilo_descarga_y_reproduccion.join(timeout=esperar_segundos)

    # Obtener el nombre del archivo descargado (considerando la extensión .part)
    video_filename = 'video_descargado.mp4.part'

    # Verificar si el archivo final existe antes de intentar reproducir
    if os.path.exists(video_filename):
        print('Iniciando reproducción...')
        # Iniciar la reproducción en un nuevo hilo
        hilo_reproduccion = threading.Thread(target=reproducir_video, args=(video_filename,))
        hilo_reproduccion.start()
    else:
        print(f'Error: No se encontró el archivo {video_filename}')

    # Esperar a que ambos hilos terminen
    hilo_descarga_y_reproduccion.join()
    if 'hilo_reproduccion' in locals():
        hilo_reproduccion.join()

    print('Proceso completo.')
