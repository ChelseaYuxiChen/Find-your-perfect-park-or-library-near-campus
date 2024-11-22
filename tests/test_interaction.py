"""
Yuxi Chen (Chelsea)
CS 5001, Spring 2024
Final Project
This is a Unit tests for the Library class.!!!NEW!!!
Please run this file from terminal using the command: python3 -m unittest tests/test_interaction.py
"""

import unittest
import tkinter as tk
from views.interaction import MapApplication


class TestMapApplication(unittest.TestCase):
    def setUp(self):
        # Create dummy data for testing
        self.schools = ["School1", "School2"]
        self.libraries = ["Library1", "Library2"]
        self.parks = ["Park1", "Park2"]
        self.school_names = ["School1", "School2"]

    def test_init(self):
        app = MapApplication(
            self.schools, self.libraries, self.parks, self.school_names
        )
        self.assertIsInstance(app.master, tk.Tk)
        self.assertEqual(app.master.winfo_toplevel().title(), "Map Application")
        self.assertEqual(
            len(app.school_var.get()), len(self.school_names[0])
        )  # Check if default school is set

    def test_retrieve_user_input_valid(self):
        app = MapApplication(
            self.schools, self.libraries, self.parks, self.school_names
        )
        app.distance_entry.insert(0, "10")  # Insert a valid distance
        input_school, distance = app.retrieve_user_input()
        self.assertEqual(input_school, self.school_names[0])
        self.assertEqual(distance, 10000.0)

    def test_retrieve_user_input_invalid(self):
        app = MapApplication(
            self.schools, self.libraries, self.parks, self.school_names
        )
        app.distance_entry.insert(0, "-10")  # Insert an invalid distance
        with self.assertRaises(ValueError):
            app.retrieve_user_input()


if __name__ == "__main__":
    unittest.main()
