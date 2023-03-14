import argparse
import json
import os
import cv2
import numpy as np


def validate_board(im_path, loc_path):
    """

    :param im_path:
    :param loc_path:
    :return:
    """
    segments = seg_image(im_path)
    capacitors = loc_capacitors(segments)
    big, small = extract_types(capacitors)

    if len(big) * 0.15 + len(small) * 0.05 > 1:
        if not os.path.exists(loc_path):
            os.mkdir(loc_path)
        im_name = im_path.split(".")[0]
        f = open(loc_path + "/" + im_name + "_loc.txt", "w")
        json.dump((big, small), f)
        return True
    else:
        return False


def extract_types(capacitors):
    big, small = ([[], [], [], [], [], []], [[], [], []])
    return big, small


def loc_capacitors(segments):
    return []


def seg_image(im_path):
    return []


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--img", help="ruta en la que se encuentra la imagen de una placa base", required=False)
    parser.add_argument("-l", "--loc", help="ruta donde se guardará la localización de los condensadores",
                        required=False)

    args = parser.parse_args()

    validate_board(args.img, args.loc)
