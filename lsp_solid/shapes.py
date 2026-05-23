"""Refactored example for the Liskov Substitution Principle."""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Define behavior shared by all shapes."""

    @abstractmethod
    def calculate_area(self):
        """Calculate the shape area."""


class Rectangle(Shape):
    """Represent a rectangle with independent width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        """Calculate the rectangle area."""
        return self.width * self.height


class Square(Shape):
    """Represent a square without changing rectangle behavior."""

    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        """Calculate the square area."""
        return self.side**2


class AreaReporter:
    """Report areas for any shape that follows the Shape contract."""

    @staticmethod
    def report(shape):
        """Return the area of a shape without depending on its concrete type."""
        return shape.calculate_area()
