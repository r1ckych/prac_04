
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):

    def __init__(self, name, fuel, fanciness, flagfall=4.5):
        super().__init__(name, fuel)
        self.flagfall = flagfall
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        return self.price_per_km * self.current_fare_distance + self.flagfall

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odo={self.odometer}, {self.current_fare_distance} on current fare," \
               f" {self.price_per_km}/km plus flagfall ${self.flagfall}"
