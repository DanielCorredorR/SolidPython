"""Refactored example for the Dependency Inversion Principle."""

from abc import ABC, abstractmethod


class DataSource(ABC):
    """Define the contract for objects that provide data."""

    @abstractmethod
    def get_data(self):
        """Return data from any source."""


class FrontEnd:
    """Display data provided by an abstract data source."""

    def __init__(self, data_source):
        self.data_source = data_source

    def display_data(self):
        """Display data without depending on a concrete implementation."""
        data = self.data_source.get_data()
        print("Display data:", data)


class DatabaseDataSource(DataSource):
    """Provide data from a database."""

    def get_data(self):
        """Return data from the database."""
        return "Data from the database"


class ApiDataSource(DataSource):
    """Provide data from an API."""

    def get_data(self):
        """Return data from the API."""
        return "Data from the API"
