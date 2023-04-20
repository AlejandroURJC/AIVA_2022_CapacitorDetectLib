import cv2
import os

font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
color = [0, 0, 255]
thickness = 2
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
        import capacitor_detection as cd
        image = cd.read_image(im_path)
        segments = cd.seg_image(image)
        capacitors = cd.loc_capacitors(segments)
        big, small = cd.extract_types(capacitors)
        benefit = len(big) * 0.15 + len(small) * 0.05
        validation = benefit > 1
        if validation:
            cd.write_txt((big, small), im_path, loc_path)
            print(f"Compra recomendada \t Beneficio: {benefit - 1:.2f}€")
        else:
            print("Compra no recomendada")
        self.show_validation(validation, im_path, loc_path)
        return validation

    def show_validation(self, valid, im_path, loc_path):
        """
        Muestra por pantalla el resultado de la decisión tomada
        :return:
        """
        import capacitor_detection as cd
        output = cv2.cvtColor(cd.read_image(im_path), cv2.COLOR_GRAY2BGR)
        if valid:
            big, small = cd.read_txt(im_path, loc_path)
            cv2.putText(output, "Recomendacion: comprar", (40, 40), font, fontScale,
                        [0, 255, 0], thickness, cv2.LINE_AA)
            cv2.putText(output, f"Beneficio: {len(big) * 0.15 + len(small) * 0.05 - 1:.2f}", (40, 80), font, fontScale,
                        [0, 255, 0], thickness, cv2.LINE_AA)
            for (x, y, r) in big:
                cv2.circle(output, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            for (x, y, r) in small:
                cv2.circle(output, (x, y), r, (255, 0, 0), 4)
                cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
        else:
            cv2.putText(output, "Recomendacion: no comprar", (40, 40), font, fontScale,
                        [0, 0, 255], thickness, cv2.LINE_AA)

        if not os.path.exists(loc_path + "/out_im"):
            os.mkdir(loc_path + "/out_im")
        im_name = im_path.split("/")[-1]
        cv2.imwrite(loc_path + "/out_im/out_" + im_name, output)
        #cv2.imshow("output", output)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

    def getCap_big_list(self, ):
        return self._cap_big_list

    def getCap_small_list(self, ):
        return self._cap_small_list

    def setCap_big_list(self, c_big_list):
        self._cap_big_list = c_big_list

    def setCap_small_list(self, c_small_list):
        self._cap_small_list = c_small_list
