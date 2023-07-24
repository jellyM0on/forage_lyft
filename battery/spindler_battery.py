from battery import Battery

def add_years_to_date(original_date, years_to_add):
    result = original_date.replace(year=original_date.year + years_to_add)
    return result

class SplinderBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        date_to_service = add_years_to_date(self.last_service_date,2)
        if date_to_service < self.current_date:
            return True
        else:
            return False