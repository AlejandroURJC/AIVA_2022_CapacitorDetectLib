import cv2
import capacitor_detection as cd

font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 0.5
color = [0, 0, 255]
thickness = 1
(_, textSize), _ = cv2.getTextSize("Test", font, fontScale, thickness)

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
        output = cv2.cvtColor(cd.read_image(im_path), cv2.COLOR_GRAY2BGR)
        if valid:
            big, small = cd.read_txt(im_path, loc_path)
            for (x, y, r) in big:
                cv2.circle(output, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            for (x, y, r) in small:
                cv2.circle(output, (x, y), r, (255, 0, 0), 4)
                cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
        else:
            print("No válida")
        cv2.imshow("output", output)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def getCap_big_list(self, ):
        return self._cap_big_list

    def getCap_small_list(self, ):
        return self._cap_small_list

    def setCap_big_list(self, c_big_list):
        self._cap_big_list = c_big_list

    def setCap_small_list(self, c_small_list):
        self._cap_small_list = c_small_list
