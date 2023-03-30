import capacitor_detection as cd

class Motherboard:
    def __init__(self):
        self._cap_small_list = None
        self._cap_big_list = None

    def validate_board(self, im_path, loc_path="./"):
        """
        Lee la imagen, se segmenta y buscan los condensadores y se clasifican entre grandes y pequeños. Se clasifica como
        válida la placa si da beneficios
        :param im_path:
        :param loc_path:
        :return:
        """
        image = cd.read_image(im_path)
        segments = cd.seg_image(image)
        capacitors = cd.loc_capacitors(segments)
        big, small = cd.extract_types(capacitors)
        validation = len(big) * 0.15 + len(small) * 0.05 > 1
        if validation:
            cd.write_txt((big, small), im_path, loc_path)
        self.show_validation(validation, im_path, loc_path)
        return validation

    def show_validation(self, valid, im_path, loc_path):
        """
        Muestra por pantalla el resultado de la decisión tomada
        :return:
        """
        if valid:
            big, small = cd.read_txt(im_path, loc_path)
            print("Válida")
            # TODO mostrar válido con las localizaciones de big y small
        else:
            print("No válida")
            # TODO mostrar np válido

    def getCap_big_list(self, ):
        return self._cap_big_list

    def getCap_small_list(self, ):
        return self._cap_small_list

    def setCap_big_list(self, c_big_list):
        self._cap_big_list = c_big_list

    def setCap_small_list(self, c_small_list):
        self._cap_small_list = c_small_list
