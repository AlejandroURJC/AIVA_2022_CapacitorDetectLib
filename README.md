# AIVA_2022_CapacitorDetectLib ![status-in progress-yellow](https://user-images.githubusercontent.com/61578803/224482948-0078baed-9ae3-474f-b31f-4ba6c4329909.svg) ![License](https://img.shields.io/badge/license-GPL%20v3-blue)
Aplicación que localiza los condensadores de una placa base y recomienda o no su compra. Una placa base tiene un coste de 1 €, los condensadores pequeños valen 5 céntimos y los grandes 15 céntimos. Teniendo esto en cuenta, sólamente si la venta de los condensadores supone un beneficio igual o superior a 1 €, se recomendará la compra. En este caso, además se generará un archivo .txt con la localización de los condensadores.
## Instalación 🔧
1. Elija el directorio en el que desea clonar el proyecto: `cd <ruta_directorio>`
2. Dentro del directorio, ejecute el siguiente comando: `git clone https://github.com/AlejandroURJC/AIVA_2022_CapacitorDetectLib.git`
3. Vaya a la carpeta del proyecto: `cd AIVA_2022_CapacitorDetectLib`
4. Instale las dependencias: `pip install -r requirements.txt`

En caso de surgirle dudas sobre cómo clonar un proyecto acceda al siguiente enlace: [Clonar un repositorio](https://docs.github.com/es/repositories/creating-and-managing-repositories/cloning-a-repository).

Mira **Despliegue** para conocer como desplegar el proyecto.

### Pre-requisitos 📋

* Python 3.10 o superior: https://www.python.org/downloads/
* Git bash: https://git-scm.com/downloads

## Despliegue 📦

Para utilizar la aplicación se llamará al .py de la siguiente forma:

`python capacitor_detection.py --img=<ruta en la que se encuentra la imagen de una placa base> --loc=<ruta donde se guardará la localización de los condensadores>`

Este comando mostrará por pantalla la imagen pasada como argumento con la información de los condensadores que tiene la placa base, además de otro texto que valide o no la compra. Si se recomienda la compra, aparte generará un archivo .txt en la carpeta dada como argumento. El archivo generado tendrá el formato `img_loc.txt`, siendo img el nombre de la imagen.

**Ejemplo:**
`python capacitor_detection.py --img=./placa1.jpg --loc=./localizaciones`

El archivo generado tendrá el nombre `placa1_loc.txt`.

## Construido con 🛠️
* [Python](https://www.python.org/) - Lenguaje de programación utilizado.
  * [OpenCV](https://opencv.org/) - Biblioteca principal utilizada en el proyecto.


## Autores ✒️

* **Alejandro Smolarek** - [AlejandroURJC](https://github.com/AlejandroURJC)
* **Mikel Galafate** - [mikelgalafate](https://github.com/mikelgalafate)
