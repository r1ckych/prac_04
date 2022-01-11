
from prac_08.taxi import Taxi


def main():
    my_car = Taxi("Prius 1", 100)
    my_car.drive(100)
    print(my_car)
    print(my_car.get_fare())


main()
