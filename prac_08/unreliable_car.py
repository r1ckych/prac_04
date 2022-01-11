"""
CP1404/CP5632 Practical
Unreliable Car class
"""

from prac_06.car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialise a Unreliable car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if distance <= self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            print(f"You can't ride {distance}km")
            return 0

    def __str__(self):
        return "{}, fuel={}, odometer={}".format(self.name, self.fuel, self.odometer)



