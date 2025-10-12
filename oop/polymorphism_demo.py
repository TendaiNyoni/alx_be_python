# polymorphism_demo.py

import math

# Base Class
class Shape:
    def area(self):
        """Base method that must be overridden by derived classes"""
        raise NotImplementedError("Subclasses must implement this method")


# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Calculates area of a rectangle"""
        return self.length * self.width


# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculates area of a circle"""
        return math.pi * (self.radius ** 2)

