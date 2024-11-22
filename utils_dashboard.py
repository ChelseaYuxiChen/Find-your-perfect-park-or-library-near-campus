"""
Yuxi Chen (Chelsea)
CS 5001, Spring 2024
Final Project
This is the utils file to display a map showing nearby parks and libraries
based on chosen school. !!! UPDATED VERSION!!!
"""

from models.fetch_and_clean_data import (
    fetch_csv_data,
    clean_school_data,
    clean_library_data,
    clean_park_data,
)
from models.library import Library
from models.school import School
from models.park import Park

SCHOOL_CSV_URL = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/schools/exports/csv?lang=en&timezone=America%2FLos_Angeles&use_labels=true&delimiter=%3B"
PARK_CSV_URL = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/parks/exports/csv?lang=en&timezone=America%2FLos_Angeles&use_labels=true&delimiter=%3B"
LIBRARY_CSV_URL = "https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/libraries/exports/csv?lang=en&timezone=America%2FLos_Angeles&use_labels=true&delimiter=%3B"
INDEX_ZERO = 0
INDEX_ONE = 1
INDEX_TWO = 2
INDEX_THREE = 3
INDEX_FOUR = 4
INDEX_FIVE = 5
INDEX_SIX = 6


def school_lists():
    """
    Fetches and cleans school data from the CSV URL, creates School objects, and returns a list of School objects.

    Args:
        None

    Returns:
        list: A list of School objects.
    """
    original_schools = fetch_csv_data(SCHOOL_CSV_URL)
    cleaned_schools = clean_school_data(original_schools)
    schools = []
    for row in cleaned_schools:
        name, category, community, address, geo = (
            row[INDEX_ZERO],
            row[INDEX_ONE],
            row[INDEX_TWO],
            row[INDEX_THREE],
            row[INDEX_FOUR],
        )
        school = School(name, category, community, address, geo)
        schools.append(school)
    return schools


def library_list():
    """
    Fetches and cleans library data from the CSV URL, creates Library objects, and returns a list of Library objects.

    Args:
        None

    Returns:
        list: A list of Library objects.
    """
    original_libraries = fetch_csv_data(LIBRARY_CSV_URL)
    cleaned_libraries = clean_library_data(original_libraries)
    libraries = []
    for row in cleaned_libraries:
        name, url, community, address, geo = (
            row[INDEX_ZERO],
            row[INDEX_ONE],
            row[INDEX_TWO],
            row[INDEX_THREE],
            row[INDEX_FOUR],
        )
        library = Library(name, url, community, address, geo)
        libraries.append(library)
    return libraries


def park_list():
    """
    Fetches and cleans park data from the CSV URL, creates Park objects, and returns a list of Park objects.

    Args:
        None

    Returns:
        list: A list of Park objects.
    """
    original_parks = fetch_csv_data(PARK_CSV_URL)
    cleaned_parks = clean_park_data(original_parks)
    parks = []
    for row in cleaned_parks:
        name, facilities, washrooms, community, street_num, street_name, geo = (
            row[INDEX_ZERO],
            row[INDEX_ONE],
            row[INDEX_TWO],
            row[INDEX_THREE],
            row[INDEX_FOUR],
            row[INDEX_FIVE],
            row[INDEX_SIX],
        )
        park = Park(
            name, facilities, washrooms, community, street_num, street_name, geo
        )
        parks.append(park)
    return parks


def get_school_names(schools):
    """
    Retrieves the names of schools from a list of School objects.

    Args:
        schools (list): A list of School objects.

    Returns:
        list: A list of school names.
    """
    # Get the names of schools for the application
    if not isinstance(schools, list):
        raise TypeError("schools must be a list")

    school_names = []
    for school_obj in schools:
        school_names.append(school_obj.name)
    return school_names
