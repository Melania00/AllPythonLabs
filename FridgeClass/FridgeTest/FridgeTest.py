import unittest

from FridgeClass.Fridge.Fridge import Fridge


class TestFridge(unittest.TestCase):
    def setUp(self):
        self.my_fridge = Fridge("Samsung", "RF28R7351SR", 32, True, "A")

    def test_brand(self):
        self.assertEqual(self.my_fridge.brand, "Samsung")

    def test_model(self):
        self.assertEqual(self.my_fridge.model, "RF28R7351SR")

    def test_capacity(self):
        self.assertEqual(self.my_fridge.capacity, 32)

    def test_defrosting_enabled(self):
        self.assertTrue(self.my_fridge.is_defrosting)

    def test_energy_efficiency_class(self):
        self.assertEqual(self.my_fridge.energy_efficiency_class, "A")

    def test_turn_on_defrosting(self):
        self.my_fridge.turn_on_defrosting()
        self.assertTrue(self.my_fridge.is_defrosting)

    def test_turn_off_defrosting(self):
        self.my_fridge.turn_off_defrosting()
        self.assertFalse(self.my_fridge.is_defrosting)

    def test_delete_model_info(self):
        self.my_fridge.delete_model_info()
        self.assertIsNone(self.my_fridge.model)


if __name__ == "__main__":
    var = unittest.main
