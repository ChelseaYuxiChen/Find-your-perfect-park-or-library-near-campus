"""
Yuxi Chen (Chelsea)
CS 5001, Spring 2024
Final Project
This is a Unit tests for the Library class.!!!Updated Version!!!
Please run this file from terminal using the command: python3 -m unittest tests/test_library.py
"""

import unittest
from shapely.geometry import Point
from models.library import Library


class TestLibrary(unittest.TestCase):
    def test_init(self):
        name = "Library A"
        url = "http://example.com/libraryA"
        community = "Community A"
        address = "123 Main St"
        geo = "40.7128,-74.0060"
        library = Library(name, url, community, address, geo)

        self.assertEqual(library.name, name)
        self.assertEqual(library.url, url)
        self.assertEqual(library.community, community)
        self.assertEqual(library.address, address)
        self.assertIsInstance(library.point, Point)
        self.assertEqual(library.point.x, -74.006)
        self.assertEqual(library.point.y, 40.7128)

    def test_update_address(self):
        name = "Library B"
        url = "http://example.com/libraryB"
        community = "Community B"
        address = "456 Elm St"
        geo = "34.0522,-118.2437"
        new_address = "789 Oak St"
        new_geo = Point(-118.2437, 34.0522)
        library = Library(name, url, community, address, geo)

        library.update_address(new_address, new_geo)

        self.assertEqual(library.address, new_address)
        self.assertEqual(library.point, new_geo)

    def test_change_community(self):
        name = "Library C"
        url = "http://example.com/libraryC"
        community = "Community C"
        address = "789 Maple St"
        geo = "41.8781,-87.6298"
        new_community = "Community D"
        library = Library(name, url, community, address, geo)

        library.change_community(new_community)

        self.assertEqual(library.community, new_community)

    def test_str(self):
        name = "Library D"
        url = "http://example.com/libraryD"
        community = "Community E"
        address = "987 Pine St"
        geo = "51.5074,-0.1278"
        library = Library(name, url, community, address, geo)

        expected_str = (
            f"{{Name: {name}, Url: {url}, Local_area: {community}, Address: {address}}}"
        )
        self.assertEqual(str(library), expected_str)


if __name__ == "__main__":
    unittest.main()
