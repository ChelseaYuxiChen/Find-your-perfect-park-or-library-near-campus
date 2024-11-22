"""
Yuxi Chen (Chelsea)
CS 5001, Spring 2024
Final Project
This is a Unit tests for the utils dashboard.!!!Updated Version!!!
Please run this file from terminal using the command: python3 -m unittest tests/test_utils_dashboard.py
"""

import unittest
from models.library import Library
from models.school import School
from models.park import Park
from utils_dashboard import get_school_names


class TestModels(unittest.TestCase):
    def test_create_school_objects(self):
        # Testing the creation of School objects from mock data
        mock_data = [
            ["School1", "Primary", "Community1", "123 Test St", "49.2827,-123.1207"],
            ["School2", "Secondary", "Community2", "456 Test St", "49.2827,-123.1207"],
        ]
        schools = []
        for row in mock_data:
            school = School(*row)
            schools.append(school)
        self.assertEqual(len(schools), 2)
        self.assertIsInstance(schools[0], School)
        self.assertIsInstance(schools[1], School)

    def test_create_park_objects(self):
        # Testing the creation of Park objects from mock data
        mock_data = [
            [
                "Park1",
                "Facilities1",
                "Washrooms1",
                "Community1",
                "123",
                "Test St",
                "49.2827,-123.1207",
            ],
            [
                "Park2",
                "Facilities2",
                "Washrooms2",
                "Community2",
                "456",
                "Test St",
                "49.2827,-123.1207",
            ],
        ]
        parks = []
        for row in mock_data:
            park = Park(*row)
            parks.append(park)
        self.assertEqual(len(parks), 2)
        self.assertIsInstance(parks[0], Park)
        self.assertIsInstance(parks[1], Park)

    def test_create_library_objects(self):
        # Testing the creation of Library objects from mock data
        mock_data = [
            ["Library1", "URL1", "Community1", "123 Test St", "49.2827,-123.1207"],
            ["Library2", "URL2", "Community2", "456 Test St", "49.2827,-123.1207"],
        ]
        libraries = []
        for row in mock_data:
            library = Library(*row)
            libraries.append(library)
        self.assertEqual(len(libraries), 2)
        self.assertIsInstance(libraries[0], Library)
        self.assertIsInstance(libraries[1], Library)


class TestGetSchoolNames(unittest.TestCase):
    def test_get_school_names(self):
        # Testing the get_school_names function with mock School objects
        schools = [
            School(
                "School1", "Primary", "Community1", "123 Test St", "49.2827,-123.1207"
            ),
            School(
                "School2", "Secondary", "Community2", "456 Test St", "49.2827,-123.1207"
            ),
        ]
        names = get_school_names(schools)
        self.assertEqual(names, ["School1", "School2"])


if __name__ == "__main__":
    unittest.main()
