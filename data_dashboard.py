"""
Yuxi Chen (Chelsea)
CS 5001, Spring 2024
Final Project
This is the drive file to display a map showing nearby parks and libraries
based on chosen school. !!!Updated Version!!!
"""

from utils_dashboard import get_school_names, school_lists, library_list, park_list
from views.interaction import MapApplication
import requests


def main():
    """
    Main function that initializes the application and runs the Tkinter application.

    Args:
        None

    Returns:
        None
    """
    try:
        # creates lists of School, Library, and Park objects
        schools = school_lists()
        parks = park_list()
        libraries = library_list()

        # Get the names of schools for the application
        school_names = get_school_names(schools)

        # Initialize the Tkinter application
        app = MapApplication(schools, libraries, parks, school_names)
        app.master.mainloop()

    except TypeError as te:
        print(f"\n TypeError see details below:\n {te}")
    except ConnectionError as ce:
        print(f"\n ConnectionError see details below:\n {ce}")
    except requests.exceptions.HTTPError as http_err:
        raise http_err(f"\n ConnectionError see details below:\n {http_err}")
    except IndexError as ie:
        print(f"\n IndexError see details below:\n {ie}")
    except ValueError as ve:
        print(f"\n ValueError see details below:\n {ve}")


if __name__ == "__main__":
    main()
