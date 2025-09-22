"""
weather_advice.py
ALX Backend: conditional statements exercise.

Prompts the user for the weather (sunny/rainy/cold) and prints a clothing recommendation.
"""

def recommend(weather):
    """
    Return a clothing recommendation string based on the provided weather string.
    """
    w = str(weather).strip().lower()
    if w == 'sunny':
        return "Wear a t-shirt and sunglasses."
    elif w == 'rainy':
        return "Don't forget your umbrella and a raincoat."
    elif w == 'cold':
        return "Make sure to wear a warm coat and a scarf."
    else:
        return "Sorry, I don't have recommendations for this weather."

def main():
    weather = input("What's the weather like today? (sunny/rainy/cold): ").strip()
    print(recommend(weather))

if __name__ == "__main__":
    main()
