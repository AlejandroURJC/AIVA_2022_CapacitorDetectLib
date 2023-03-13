import unittest
import capacitor_detection as cd


class Testing(unittest.TestCase):
    def test_helloworld(self):
        """
        Realiza pruebas sobre la función hello world
        """
        self.assertEqual(cd.helloworld(), "hello world")
