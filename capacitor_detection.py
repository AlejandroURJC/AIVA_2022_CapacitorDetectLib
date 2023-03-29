import os
import cv2
import json
import argparse
from Motherboard import Motherboard

def write_txt(capacitors, im_path, loc_path):
    """
    Escribe la información de condensadores de la placa en un fichero txt
    :param capacitors:
    :param im_path:
    :param loc_path:
    :return:
    """
    if not os.path.exists(loc_path):
        os.mkdir(loc_path)
    im_name = im_path.split(".")[0]
    with open(loc_path + "/" + im_name + "_loc.txt", "w") as f:
        json.dump(capacitors, f)


def read_txt(im_path, loc_path):
    """
    Lee el fichero txt con los datos de condensadores guardados
    :param im_path:
    :param loc_path:
    :return:
    """
    im_name = im_path.split(".")[0]
    try:
        with open(loc_path + "/" + im_name + "_loc.txt", "r") as f:
            return json.load(f)
    except OSError as e:
        return


def read_image(im_path):
    """
    Comprueba si la imagen existe y se lee
    :param im_path:
    :return:
    """
    if os.path.exists(im_path):
        img = cv2.imread(im_path, cv2.IMREAD_GRAYSCALE)
        width = int(img.shape[1] / 3)
        height = int(img.shape[0] / 3)
        dim = (width, height)
        return cv2.resize(img, dim)
    else:
        raise Exception("La imagen no existe")


# TODO implementar extracción de tipos
def extract_types(capacitors):
    """
    Separa los condensadores por tipos (grande o pequeño)
    :param capacitors:
    :return:
    """
    big, small = ([[], [], [], [], [], [], [], []], [])
    return big, small


def loc_capacitors(segments):
    """
    Recibe los segmentos de seg_image y se queda con los que son condensadores
    :param segments:
    :return:
    """
    res = []
    for (x, y, r) in segments:
        # Si el segmento cumple el umbral entonces se crea un condensador y se añade a la lista
        if 4 < r < 11:
            cap = Capacitor((x, y), r)
            res.append(cap)
    return res


# TODO implementar segmentación de la imagen
def seg_image(image):
    """
    Recibe una imagen y la segmenta buscando zonas redondeadas
    :param image:
    :return:
    """


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--img", help="ruta en la que se encuentra la imagen de una placa base", required=False)
    parser.add_argument("-l", "--loc", help="ruta donde se guardará la localización de los condensadores",
                        required=False)

    args = parser.parse_args()
    board = Motherboard()
    valid = board.validate_board(args.img, args.loc)