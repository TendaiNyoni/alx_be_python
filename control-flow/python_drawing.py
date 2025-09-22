"""
pattern_drawing.py
ALX Backend: practice with while loops and nested for loops.

Prompts the user for a positive integer and prints a square pattern of asterisks of that size.
"""

def main():
    try:
        size = int(input("Enter the size of the pattern: "))
        if size <= 0:
            print("Please enter a positive integer greater than 0.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")
        return

    row = 0
    while row < size:
        for col in range(size):
            print("*", end="")  # print * without moving to new line
        print()  # move to next line after finishing one row
        row += 1

if __name__ == "__main__":
    main()
