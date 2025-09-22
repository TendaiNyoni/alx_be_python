#!/usr/bin/python3

"""
weather_advice.py
ALX Backend: conditional statements exercise.

Prompts the user for the weather (sunny/rainy/cold) and prints a clothing recommendation.
"""

def recommend(weather):
    """
    Return a clothing recommendation string based on the provided weather string.
    """
    if weather.lower() == 'sunny':
        print("Wear a t-shirt and sunglasses.")
    elif weather.lower() == 'rainy':
        print("Don't forget your umbrella and a raincoat.")
    elif weather.lower == 'cold':
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")

def main():
    weather = input("What's the weather like today? (sunny/rainy/cold): ").strip()
    print(recommend(weather))

if __name__ == "__main__":
    main()
