
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    bill = 0
    current_taxi = None
    menu = input("Let's drive! \nq)uit, c)hoose taxi, d)rive\n >>> ").lower()
    while menu != "q":
        if menu == "c":
            print("Taxis available: ")
            count = 0
            for taxi in taxis:
                print(f"{count} - {taxi}")
                count += 1
            choose_taxi = int(input("Choose taxi: "))
            try:
                if taxis[choose_taxi]:
                    current_taxi = taxis[choose_taxi]
            except IndexError:
                print(f"Invalid taxi choice \n")
        if menu == "d":
            if current_taxi != None:
                drive_distance = int(input("Drive how far? "))
                current_taxi.drive(drive_distance)
                print(f"Your trip cost you {current_taxi.get_fare()}")
                bill += current_taxi.get_fare()
            else:
                print("You need to choose a taxi before you can drive")
        if menu != "c" and menu != "d":
            print("Invalid option")
        print(f"Bill to date: ${bill}")
        menu = input("Let's drive! \nq)uit, c)hoose taxi, d)rive\n >>> ").lower()
    print(f"Total trip cost: {bill}")
    print("Taxis are now: ")
    count_taxis = 0
    for taxi in taxis:
        print(f"{count_taxis} - {taxi}")
        count_taxis += 1


main()
