import argparse
import cv2
import numpy as np


def helloworld():
    """
    Hace algo
    :return:
    """
    return "hello world"


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--img", help="ruta en la que se encuentra la imagen de una placa base", required=False)
    parser.add_argument("-l", "--loc", help="ruta donde se guardará la localización de los condensadores",
                        required=False)

    args = parser.parse_args()


