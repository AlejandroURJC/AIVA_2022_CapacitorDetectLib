import unittest
import capacitor_detection as cd
from Motherboard import Motherboard

testim = "./DB/rec1-1.jpg"
testloc = "./locations"


class CapacitorDetectionTest(unittest.TestCase):
    def test_read_txt(self):
        """
        Comprueba que la función read_txt lee correctamente el fichero
        :return:
        """
        big, small = cd.read_txt(testim, testloc)
        self.assertIsNotNone(big, "Archivo no leído correctamente")
        self.assertIsNotNone(small, "Archivo no leído correctamente")

    def test_write_txt(self):
        """
        Comprueba que la función write_txt escribe correctamente en el fichero
        :return:
        """
        big, small = ([], [])
        cd.write_txt((big, small), testim, testloc)
        new_big, new_small = cd.read_txt(testim, testloc)
        self.assertEqual(big, new_big, "Lo escrito y lo leído no coinciden")
        self.assertEqual(small, new_small, "Lo escrito y lo leído no coinciden")

    def test_validate_board(self):
        """
        Comprueba que una placa evaluada como positiva ha sido bien validada
        :return:
        """
        board = Motherboard()
        self.assertTrue(board.validate_board(testim, testloc), "Placa no válida")
        big, small = cd.read_txt(testim, testloc)
        self.assertGreater(len(big) * 0.15 + len(small) * 0.05, 1, "Placa mal validada")

    def test_read_image(self):
        """
        Comprueba que la imagen se lee correctamente con el tamaño debido
        :return:
        """
        self.assertEqual(cd.read_image(testim).shape, (1093, 1642))

    def test_loc_capacitors(self):
        """
        Comprueba que el número de condensadores detectados en la imagen son los esperados
        :return:
        """
        tuples = cd.seg_image(cd.read_image(testim))
        capacitors = cd.loc_capacitors(tuples)
        self.assertEqual(51, len(capacitors))
