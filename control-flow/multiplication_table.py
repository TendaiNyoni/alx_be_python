#!/usr/bin/python3

"""
multiplication_table.py
ALX Backend: practice with for loops.

Prompts the user for a number and prints its multiplication table from 1 to 10.
"""

def main():
    try:
        number = int(input("Enter a number to see its multiplication table: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")

if __name__ == "__main__":
    main()
