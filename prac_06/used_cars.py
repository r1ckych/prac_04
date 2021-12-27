"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(100)
    my_car.drive(30)
    my_car.add_fuel(20)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("{} {}, {}".format(my_car.new_car, my_car.fuel, my_car.odometer))
    print("{self.new_car} {self.fuel}, {self.odometer}".format(self=my_car))


main()