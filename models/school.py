"""
Yuxi Chen (Chelsea)
CS 5001, Spring 2024
Final Project
This is a school class with basic information.!!!Updated Version!!!
"""

from shapely.geometry import Point


class School:
    """
    Represents a school entity with basic information.

    Attributes:
        name (str): The name of the school.
        category (str): The category of the school.
        community (str): The local area where the school is located.
        address (str): The address of the school.
        point (Point): The geographical coordinates of the school.

    Methods:
        __init__: Initializes a School object with the provided attributes.
        update_address: Update the address of the school.
        change_community: Change the community of the school.
        __str__: Returns a string representation of the school object.

    Raises:
        TypeError: If any of the input arguments are not of the expected string type.
    """

    def __init__(self, name, category, community, address, geo):
        """
        Initializes a School object with the provided attributes.

        Args:
            name (str): The name of the school.
            category (str): The category of the school.
            community (str): The local area where the school is located.
            address (str): The address of the school.
            geo (str): The geographical coordinates of the school in the format "latitude,longitude".

        Raises:
            TypeError: If any of the input arguments are not of the expected string type.
        """
        if not isinstance(name, str):
            raise TypeError(f"Function argument:{name} must be of type string.")
        if not isinstance(category, str):
            raise TypeError(f"Function argument:{category} must be of type string.")
        if not isinstance(community, str):
            raise TypeError(f"Function argument:{community} must be of type string.")
        if not isinstance(address, str):
            raise TypeError(f"Function argument:{address} must be of type string.")
        if not isinstance(geo, str):
            raise TypeError(f"Function argument:{geo} must be of type string.")

        self.name = name
        self.category = category
        self.community = community
        self.address = address
        latitude, longitude = map(float, geo.split(","))
        self.point = Point(longitude, latitude)

    def update_address(self, new_address, new_point):
        """
        Update the address of the school.

        Args:
            new_address (str): The new address of the school.
            new_point(Point):The point of the school

        Raises:
            TypeError: If any of the input arguments are not of the expected string type.
        """
        if not isinstance(new_address, str):
            raise TypeError(
                f"New address must be a string, got {type(new_address)} instead."
            )
        if not isinstance(new_point, Point):
            raise TypeError(
                f"New point must be a Point object, got {type(new_point)} instead."
            )

        self.address = new_address
        self.point = new_point
        print("Address updated successfully.")

    def change_community(self, new_community):
        """
        Change the community of the school.

        Args:
            new_address (str): The new address of the school.

        Raises:
            TypeError: If any of the input arguments are not of the expected string type.
        """
        if not isinstance(new_community, str):
            raise TypeError(
                f"New community must be a string, got {type(new_community)} instead."
            )

        self.community = new_community
        print("Community updated successfully.")

    def __str__(self):
        """
        Returns a string representation of the school object.

        Returns:
            str: A string containing the name, category, local area, and address of the school.

        Raises:
            nothing
        """
        return f"{{Name: {self.name}, Category: {self.category}, Local_area: {self.community}, Address: {self.address}}}"
