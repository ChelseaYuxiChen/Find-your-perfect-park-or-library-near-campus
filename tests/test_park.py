"""
Yuxi Chen (Chelsea)
CS 5001, Spring 2024
Final Project
This is a Unit tests for the Park class.!!!Updated Version!!!
Please run this file from terminal using the command: python3 -m unittest tests/test_park.py
"""

import unittest
from shapely.geometry import Point
from models.park import Park


class TestPark(unittest.TestCase):
    def test_init(self):
        name = "Park A"
        facilities = "Playground, Basketball Court"
        washrooms = "Available"
        community = "Community A"
        street_num = "123"
        street_name = "Main St"
        geo = "40.7128,-74.0060"
        park = Park(
            name, facilities, washrooms, community, street_num, street_name, geo
        )

        self.assertEqual(park.name, name)
        self.assertEqual(park.facilities, facilities)
        self.assertEqual(park.washrooms, washrooms)
        self.assertEqual(park.community, community)
        self.assertEqual(park.address, f"{street_num} {street_name}")
        self.assertIsInstance(park.point, Point)
        self.assertEqual(park.point.x, -74.006)
        self.assertEqual(park.point.y, 40.7128)

    def test_update_address(self):
        name = "Park B"
        facilities = "Picnic Area"
        washrooms = "Not Available"
        community = "Community B"
        street_num = "456"
        street_name = "Elm St"
        geo = "34.0522,-118.2437"
        new_address = "789 Oak St"
        new_geo = Point(-118.2437, 34.0522)
        park = Park(
            name, facilities, washrooms, community, street_num, street_name, geo
        )

        park.update_address(new_address, new_geo)

        self.assertEqual(park.address, new_address)
        self.assertEqual(park.point, new_geo)

    def test_update_washrooms(self):
        name = "Park C"
        facilities = "Walking Trails"
        washrooms = "Not Available"
        community = "Community C"
        street_num = "789"
        street_name = "Maple St"
        geo = "41.8781,-87.6298"
        new_washrooms = "Available"
        park = Park(
            name, facilities, washrooms, community, street_num, street_name, geo
        )

        park.update_washrooms(new_washrooms)

        self.assertEqual(park.washrooms, new_washrooms)

    def test_change_community(self):
        name = "Park D"
        facilities = "Tennis Courts"
        washrooms = "Available"
        community = "Community D"
        street_num = "987"
        street_name = "Pine St"
        geo = "51.5074,-0.1278"
        new_community = "Community E"
        park = Park(
            name, facilities, washrooms, community, street_num, street_name, geo
        )

        park.change_community(new_community)

        self.assertEqual(park.community, new_community)

    def test_str(self):
        name = "Park E"
        facilities = "Skate Park"
        washrooms = "Available"
        community = "Community F"
        street_num = "246"
        street_name = "Oak St"
        geo = "45.4215,-75.6972"
        park = Park(
            name, facilities, washrooms, community, street_num, street_name, geo
        )

        expected_str = f"{{Name: {name}, Facilities: {facilities}, Washrooms: {washrooms}, Local_area: {community}, Address: {street_num} {street_name}}}"
        self.assertEqual(str(park), expected_str)


if __name__ == "__main__":
    unittest.main()
