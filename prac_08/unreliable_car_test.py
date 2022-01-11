
from prac_08.unreliable_car import UnreliableCar
import random


def main():
    my_car = UnreliableCar("Toyota", 100, 45)
    my_car.drive(random.randint(0, 100))
    print(my_car)


main()
