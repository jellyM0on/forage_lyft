import unittest

from tires.octoprime_tires import OctoprimeTires


class TestCarrigan(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0, 0, 3, 0]
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [1, 2, 5, 0]
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())