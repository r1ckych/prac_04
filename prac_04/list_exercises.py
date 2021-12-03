
def main():
    numbers = []
    input_elements(numbers)
    print_results(numbers)


def input_elements(numbers):
    for i in range(1, 5+1):
        number = float(input("Number"))
        numbers.append(number)
    return numbers


def print_results(numbers):
    print(numbers)
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers {sum(numbers) / len(numbers)}")


main()
