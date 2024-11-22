"""
Yuxi Chen (Chelsea)
CS 5001, Spring 2024
Final Project
This is a Unit tests for the fetch and clean data.!!!Updated Version!!!
Please run this file from terminal using the command: python3 -m unittest tests/test_fetch_and_clean_data.py
"""

import unittest
import requests
import requests_mock
from models.fetch_and_clean_data import (
    fetch_csv_data,
    clean_school_data,
    clean_park_data,
    clean_library_data,
)


class TestFetchCSVData(unittest.TestCase):
    def test_fetch_csv_data_success(self):
        with requests_mock.Mocker() as mocker:
            url = "http://example.com/data.csv"
            mocker.get(url, text="1,2,3\n4,5,6\n")

            expected_data = [['1,2,3'], ['4,5,6']]
            self.assertEqual(fetch_csv_data(url), expected_data)

    def test_fetch_csv_data_connection_error(self):
        with requests_mock.Mocker() as mocker:
            url = "http://example.com/data.csv"
            mocker.get(url, exc=requests.exceptions.ConnectionError)

            with self.assertRaises(ConnectionError):
                fetch_csv_data(url)

    def test_fetch_csv_data_http_error(self):
        with requests_mock.Mocker() as mocker:
            url = "http://example.com/data.csv"
            mocker.get(url, status_code=404)

            with self.assertRaises(requests.exceptions.HTTPError):
                fetch_csv_data(url)


class TestCleaningFunctions(unittest.TestCase):
    def test_clean_school_data(self):
        data_list = [
            ["Address", "Category", "Name", "Other", "Community", "Geo"],
            ["Address2", "Category2", "School2", "Other", "Community2", "2.0,2.0"],
        ]
        expected_result = [
            ["School2", "Category2", "Community2", "Address2", "2.0,2.0"]
        ]
        self.assertEqual(clean_school_data(data_list), expected_result)

    def test_clean_park_data(self):
        data_list = [
            [
                "Other",
                "Name",
                "Other",
                "Other",
                "Other",
                "Facilities",
                "Washrooms",
                "Street_num",
                "Street_name",
                "Other",
                "Other",
                "Community",
                "Other",
                "Other",
                "Geo",
            ],
            [
                "Other",
                "Test Park",
                "Other",
                "Other",
                "Other",
                "Playground",
                "Yes",
                "123",
                "Test St",
                "Other",
                "Other",
                "Test Community",
                "Other",
                "Other",
                "0.0,0.0",
            ],
        ]
        expected_result = [
            [
                "Test Park",
                "Playground",
                "Yes",
                "Test Community",
                "123",
                "Test St",
                "0.0,0.0",
            ]
        ]
        self.assertEqual(clean_park_data(data_list), expected_result)

    def test_clean_library_data(self):
        data_list = [
            ["Address", "Name", "URL", "other", "Community", "Geo"],
            [
                "123 Test St",
                "Test Library",
                "http://test.com",
                "other",
                "Test Community",
                "0.0,0.0",
            ],
        ]
        expected_result = [
            [
                "Test Library",
                "http://test.com",
                "Test Community",
                "123 Test St",
                "0.0,0.0",
            ]
        ]
        self.assertEqual(clean_library_data(data_list), expected_result)


if __name__ == "__main__":
    unittest.main()
