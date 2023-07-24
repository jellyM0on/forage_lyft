import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery

class TestNubbin(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2004-05-10")
        last_service_date = date.fromisoformat("2000-01-20")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2000-01-10")
        last_service_date = date.fromisoformat("2003-01-20")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())