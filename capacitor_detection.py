import os
import cv2
import json
import argparse


def validate_board(im_path, loc_path="./"):
    """
    Lee la imagen, se segmenta y buscan los condensadores y se clasifican entre grandes y pequeños. Se clasifica como
    válida la placa si da beneficios
    :param im_path:
    :param loc_path:
    :return:
    """
    image = read_image(im_path)
    segments = seg_image(image)
    capacitors = loc_capacitors(segments)
    big, small = extract_types(capacitors)

    if len(big) * 0.15 + len(small) * 0.05 > 1:
        write_txt((big, small), im_path, loc_path)
        return True
    else:
        return False


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


def show_validation(valid, im_path, loc_path):
    """
    Muestra por pantalla el resultado de la decisión tomada
    :return:
    """
    if valid:
        big, small = read_txt(im_path, loc_path)
        print("Válida")
        # TODO mostrar válido con las localizaciones de big y small
    else:
        print("No válida")
        # TODO mostrar np válido


def read_image(im_path):
    """
    Comprueba si la imagen existe y se lee
    :param im_path:
    :return:
    """
    if os.path.exists(im_path):
        return cv2.imread(im_path, 0)
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


# TODO implementar localizar condensadores
def loc_capacitors(segments):
    """
    Recibe los segmentos de seg_image y se queda con los que son condensadores
    :param segments:
    :return:
    """
    return []


# TODO implementar segmentación de la imagen
def seg_image(image):
    """
    Recibe una imagen y la segmenta buscando zonas redondeadas
    :param image:
    :return:
    """
    return []


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--img", help="ruta en la que se encuentra la imagen de una placa base", required=False)
    parser.add_argument("-l", "--loc", help="ruta donde se guardará la localización de los condensadores",
                        required=False)

    args = parser.parse_args()

    valid = validate_board(args.img, args.loc)
    show_validation(valid, args.img, args.loc)
