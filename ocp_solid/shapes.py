"""Refactored example for the Open/Closed Principle."""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Define the contract for geometric shapes."""

    @abstractmethod
    def calculate_area(self):
        """Calculate the shape area."""


class Rectangle(Shape):
    """Represent a rectangle shape."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        """Calculate the rectangle area."""
        return self.width * self.height


class Circle(Shape):
    """Represent a circle shape."""

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        """Calculate the circle area."""
        return pi * self.radius**2


class AreaCalculator:
    """Calculate areas for any shape that follows the Shape contract."""

    @staticmethod
    def calculate(shape):
        """Calculate the area without knowing the concrete shape type."""
        return shape.calculate_area()
