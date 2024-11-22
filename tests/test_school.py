"""
Yuxi Chen (Chelsea)
CS 5001, Spring 2024
Final Project
This is a Unit tests for the School class.!!!Updated Version!!!
Please run this file from terminal using the command: python3 -m unittest tests/test_school.py
"""

import unittest
from shapely.geometry import Point
from models.school import School


class TestSchool(unittest.TestCase):
    def test_init(self):
        name = "Test School"
        category = "Primary"
        community = "Test Community"
        address = "123 Test St"
        geo = "49.2827,-123.1207"
        school = School(name, category, community, address, geo)
        self.assertEqual(school.name, name)
        self.assertEqual(school.category, category)
        self.assertEqual(school.community, community)
        self.assertEqual(school.address, address)
        self.assertIsInstance(school.point, Point)

    def test_update_address(self):
        name = "Test School"
        category = "Primary"
        community = "Test Community"
        address = "123 Test St"
        geo = "49.2827,-123.1207"
        school = School(name, category, community, address, geo)

        new_address = "456 New St"
        new_geo = "49.2800,-123.1180"
        new_point = Point(float(new_geo.split(",")[1]), float(new_geo.split(",")[0]))
        school.update_address(new_address, new_point)

        self.assertEqual(school.address, new_address)
        self.assertEqual(school.point, new_point)

    def test_change_community(self):
        name = "Test School"
        category = "Primary"
        community = "Test Community"
        address = "123 Test St"
        geo = "49.2827,-123.1207"
        school = School(name, category, community, address, geo)

        new_community = "New Test Community"
        school.change_community(new_community)

        self.assertEqual(school.community, new_community)

    def test_str(self):
        name = "Test School"
        category = "Primary"
        community = "Test Community"
        address = "123 Test St"
        geo = "49.2827,-123.1207"
        school = School(name, category, community, address, geo)

        expected_output = f"{{Name: {name}, Category: {category}, Local_area: {community}, Address: {address}}}"
        self.assertEqual(str(school), expected_output)


if __name__ == "__main__":
    unittest.main()
