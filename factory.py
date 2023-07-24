from car import Car
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SplinderBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires

class CarFactory:
    @staticmethod
    def make_calliope(tire_wear, current_mileage, last_service_mileage, current_date, last_service_date):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SplinderBattery(current_date, last_service_date)
        tires = CarriganTires(tire_wear)
        car = Car(engine, battery)
        return car
    
    @staticmethod
    def make_glissade(current_mileage, last_service_mileage, current_date, last_service_date):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SplinderBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car
    
    @staticmethod
    def make_palindrome(warning_light_is_on, current_date, last_service_date):
        engine = SternmanEngine(warning_light_is_on)
        battery = SplinderBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car
    
    @staticmethod
    def make_rorschach(current_mileage, last_service_mileage, current_date, last_service_date):
        engine = SternmanEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car
    
    @staticmethod
    def make_thovex(current_mileage, last_service_mileage, current_date, last_service_date):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        car = Car(engine, battery)
        return car