from battery import battery
from utils import add_years_to_date


class SpindlerBattery(battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        date_which_battery_should_be_serviced_by = add_years_to_date(self.last_service_date, 2)
        if date_which_battery_should_be_serviced_by < self.current_date:
            return True
        else:
            return False
