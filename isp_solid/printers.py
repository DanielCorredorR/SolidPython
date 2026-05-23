"""Refactored example for the Interface Segregation Principle."""

from abc import ABC, abstractmethod


class Printer(ABC):
    """Define behavior for devices that can print documents."""

    @abstractmethod
    def print(self, document):
        """Print a document."""


class Scanner(ABC):
    """Define behavior for devices that can scan documents."""

    @abstractmethod
    def scan(self, document):
        """Scan a document."""


class Fax(ABC):
    """Define behavior for devices that can fax documents."""

    @abstractmethod
    def fax(self, document):
        """Fax a document."""


class OldPrinter(Printer):
    """Represent a printer that only supports printing."""

    def print(self, document):
        """Print a document in black and white."""
        print(f"Printing {document} in black and white...")


class ModernPrinter(Printer, Scanner, Fax):
    """Represent a multifunction printer."""

    def print(self, document):
        """Print a document in color."""
        print(f"Printing {document} in color...")

    def scan(self, document):
        """Scan a document."""
        print(f"Scanning {document}...")

    def fax(self, document):
        """Fax a document."""
        print(f"Faxing {document}...")
