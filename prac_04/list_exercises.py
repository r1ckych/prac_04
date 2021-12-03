usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    numbers = []
    username = input("Enter your username: ")
    username_checker(username)
    input_elements(numbers)
    print_results(numbers)


def username_checker(username):
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


def input_elements(numbers):
    for i in range(1, 5+1):
        number = float(input("Number: "))
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
