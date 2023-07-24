import unittest
from datetime import date

from battery.spindler_battery import SplinderBattery

class TestSpindler(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2002-05-10")
        last_service_date = date.fromisoformat("2000-01-20")
        battery = SplinderBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2002-01-10")
        last_service_date = date.fromisoformat("2001-01-20")
        battery = SplinderBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())