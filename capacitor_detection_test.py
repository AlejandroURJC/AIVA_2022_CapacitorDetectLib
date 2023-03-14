import json
import unittest
import capacitor_detection as cd


class CapacitorDetectionTest(unittest.TestCase):
    def test_validate_board(self):
        """
        Comprueba que una placa evaluada como positiva ha sido bien validada
        :return:
        """
        cd.validate_board("test.jpg", "./locations")
        try:
            with open("./locations/test_loc.txt", "r") as f:
                big, small = json.load(f)
                self.assertGreater(len(big) * 0.15 + len(small) * 0.05, 1, "Placa mal validada")
        except OSError as e:
            return

    def test_validate_board_out(self):
        self.assertIsInstance(cd.validate_board("test.jpg", "./locations"), bool)
