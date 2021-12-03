
import random

MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    quick_pick = int(input("How many quick picks? "))
    generate_qp(quick_pick)


def generate_qp(quick_pick):
    for j in range(quick_pick):
        numbers = []
        for i in range(1, 6):
            num = random.randint(MIN_NUMBER, MAX_NUMBER)
            while num in numbers:
                num = random.randint(MIN_NUMBER, MAX_NUMBER)
            numbers.append(num)
            numbers.sort()
        print(numbers)




main()