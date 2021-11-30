"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = random.randint(1, 100)
    result = identify_mark(score)
    print(f"Your score is {score} and it's {result}")


def identify_mark(score):
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    if score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"


main()
