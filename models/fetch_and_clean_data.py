"""
Yuxi Chen (Chelsea)
CS 5001, Spring 2024
Final Project
Fetches CSV data from the specified URL. !!!Updated Version!!!
"""

import requests
import csv

INDEX_ZERO = 0
INDEX_ONE = 1
INDEX_TWO = 2
INDEX_FOUR = 4
INDEX_FIVE = 5
INDEX_SIX = 6
INDEX_SEVEN = 7
INDEX_EIGHT = 8
INDEX_ELEVEN = 11
INDEX_FOURTEEN = 14


def fetch_csv_data(url):
    """
    Fetches CSV data from the specified URL.

    Args:
        url (str): The URL from which to fetch the CSV data.

    Returns:
        list: A list of lists representing the CSV data, where each inner list
        contains the values of a single row.

    Raises:
        ConnectionError: If failed to establish a connection to the server.
        HTTPError: If an HTTP error occurred.
    """

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad status codes (4xx or 5xx)

        # Split the HTTP response text into lines and create a csv.reader object
        csv_reader = csv.reader(response.text.splitlines(), delimiter=";")
        # transform csv to list
        data_list = list(csv_reader)
        return data_list
    except requests.exceptions.ConnectionError:
        raise ConnectionError("Failed to establish a connection to the server.")
    except requests.exceptions.HTTPError:
        raise requests.exceptions.HTTPError("HTTP error occurred.")


def clean_school_data(data_list):
    """
    Cleans and parses the raw school data.

    Args:
        data_list (list): A list of lists representing raw school data.

    Returns:
        list: A list of lists representing cleaned school data, where each inner list
        contains attributes of a single school.

    Raises:
        TypeError: If data_list is not a list.
        IndexError: If an IndexError occurred while parsing the data.
    """
    if not isinstance(data_list, list):
        raise TypeError("data_list must be a list")

    # Skip the header row
    data_list = data_list[1:]
    # Create list of School objects
    schools = []
    for row in data_list:
        try:
            name, category, community, address, geo = (
                row[INDEX_TWO],
                row[INDEX_ONE],
                row[INDEX_FOUR],
                row[INDEX_ZERO],
                row[INDEX_FIVE],
            )
            school = [name, category, community, address, geo]
            schools.append(school)
        except IndexError:
            print("IndexError occurred.")
        except TypeError:
            print("TypeError occurred.")
    return schools


def clean_park_data(data_list):
    """
    Cleans and parses the raw park data.

    Args:
        data_list (list): A list of lists representing raw park data.

    Returns:
        list: A list of lists representing cleaned park data, where each inner list
        contains attributes of a single park.

    Raises:
        TypeError: If data_list is not a list.
        IndexError: If an IndexError occurred while parsing the data.
    """
    if not isinstance(data_list, list):
        raise TypeError("data_list must be a list")

    # Skip the header row
    data_list = data_list[1:]
    # Create list of School objects
    parks = []
    for row in data_list:
        try:
            name, facilities, washrooms, community, street_num, street_name, geo = (
                row[INDEX_ONE],
                row[INDEX_FIVE],
                row[INDEX_SIX],
                row[INDEX_ELEVEN],
                row[INDEX_SEVEN],
                row[INDEX_EIGHT],
                row[INDEX_FOURTEEN],
            )
            park = [
                name,
                facilities,
                washrooms,
                community,
                street_num,
                street_name,
                geo,
            ]
            parks.append(park)
        except IndexError:
            print("IndexError occurred.")
        except TypeError:
            print("TypeError occurred.")
    return parks


def clean_library_data(data_list):
    """
    Cleans and parses the raw library data.

    Args:
        data_list (list): A list of lists representing raw library data.

    Returns:
        list: A list of lists representing cleaned library data, where each inner list
        contains attributes of a single library.

    Raises:
        TypeError: If data_list is not a list.
        IndexError: If an IndexError occurred while parsing the data.
    """
    if not isinstance(data_list, list):
        raise TypeError("data_list must be a list")

    # Skip the header row
    data_list = data_list[1:]
    # Create list of School objects
    libraries = []
    for row in data_list:
        try:
            name, url, community, address, geo = (
                row[INDEX_ONE],
                row[INDEX_TWO],
                row[INDEX_FOUR],
                row[INDEX_ZERO],
                row[INDEX_FIVE],
            )
            library = [name, url, community, address, geo]
            libraries.append(library)
        except IndexError:
            print("IndexError occurred.")
        except TypeError:
            print("TypeError occurred.")
    return libraries
