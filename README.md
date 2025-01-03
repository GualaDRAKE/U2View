# U2View ~ Script Python que utiliza yt-dlp para reproducir videos de YouTube minetras se descargan. ~

El script ofrece dos opciones al usuario:
1- Descargar un único archivo: Descarga un archivo de video+audio en la resolución más cercana a Full HD, sin informar al usuario la resolución exacta que finalmente se descargará.
2- Descargar video en Full HD: Descarga el video en resolución Full HD (1920x1080), descargando audio y video por separado  así lo dispone YouTube, el problema de esto es que al bajar archivos por separado de audio y video, luego hay que fusionarlos y eso implica que no tenga sentido reproducirlo.

Requisitos:
° VLC.

° yt-dlp.

° Python 3.x.

Instrucciones de uso:
- Asegúrate de tener instalado el Reproductor VLC.
- Clona este repositorio, o descarga, el script U2view.py.
- Instala yt-dlp ejecutando pip install -U yt-dlp. (Ver nota a)
- Ejecuta el script vía "python3 U2view.py". (Ver nota b)
- Ingresa la URL del video de YouTube cuando se solicite.
- Selecciona una de las opciones proporcionadas.
- El script descargará y reproducirá el video según la opción elegida.
¡Disfruta de tus videos de YouTube con U2View!

NOTAS:
a. Actualmente, en distros LiNUX tales como Debian, Ubuntu y derivadas, trabajan python en "Entornos Virtuales", alias "VENV", y para ello hay que ejecutar "python3 -m venv /PATH/mi_entorno_virtual", y luego "source /PATH/mi_entorno_virtual/bin/activate". ;) 
b. Actualmente, en la mayoría de los distros LiNUX, al ejecutar un script de python, el ejecutable va acompañado de un número relacionado con la versión instalada, por ejemplo "python3 nombre_script.py", asegúrate que en tu sistema sea lo mismo ya que existe la psobilidad que el ejecutable no lleve un número al final.
