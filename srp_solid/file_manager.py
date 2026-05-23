"""Refactored example for the Single Responsibility Principle."""

from pathlib import Path
from zipfile import ZipFile


class FileManager:
    """Handle file reading and writing operations."""

    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        """Read text from a file."""
        return self.path.read_text(encoding=encoding)

    def write(self, data, encoding="utf-8"):
        """Write text to a file."""
        self.path.write_text(data, encoding=encoding)


class ZipFileManager:
    """Handle file compression and decompression operations."""

    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        """Compress the file into a zip archive with the same base name."""
        zip_path = self.path.with_suffix(".zip")

        with ZipFile(zip_path, mode="w") as archive:
            archive.write(self.path, arcname=self.path.name)

    def decompress(self, output_directory="."):
        """Extract the zip archive into the selected output directory."""
        zip_path = self.path.with_suffix(".zip")

        with ZipFile(zip_path, mode="r") as archive:
            archive.extractall(path=output_directory)
