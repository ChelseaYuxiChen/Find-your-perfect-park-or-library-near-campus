"""
Yuxi Chen (Chelsea)
CS 5001, Spring 2024
Final Project
This is a park class with basic information.!!!Updated Version!!!
"""

from shapely.geometry import Point


class Park:
    """
    Represents a park entity with basic information.

    Attributes:
        name (str): The name of the park.
        facilities (str): The facilities available in the park.
        washrooms (str): Information about washrooms in the park.
        community (str): The local area where the park is located.
        address (str): The address of the park.
        point (Point): The geographical coordinates of the park.

    Methods:
        __init__: Initializes a Park object with the provided attributes.
        update_address: Update the address of the park.
        update_washrooms: Update the washrooms information of the park.
        change_community: Change the community of the park.
        __str__: Returns a string representation of the park object.
    """

    def __init__(
        self, name, facilities, washrooms, community, street_num, street_name, geo
    ):
        """
        Initializes a Park object with the provided attributes.

        Args:
            name (str): The name of the park.
            facilities (str): The facilities available in the park.
            washrooms (str): Information about washrooms in the park.
            community (str): The local area where the park is located.
            street_num (str): The street number of the park's address.
            street_name (str): The street name of the park's address.
            geo (str): The geographical coordinates of the park in the format "latitude,longitude".
        """
        if not isinstance(name, str):
            raise TypeError(f"Function argument:{name} must be of type string.")
        if not isinstance(facilities, str):
            raise TypeError(f"Function argument:{facilities} must be of type string.")
        if not isinstance(washrooms, str):
            raise TypeError(f"Function argument:{washrooms} must be of type string.")
        if not isinstance(community, str):
            raise TypeError(f"Function argument:{community} must be of type string.")
        if not isinstance(street_num, str):
            raise TypeError(f"Function argument:{street_num} must be of type string.")
        if not isinstance(street_name, str):
            raise TypeError(f"Function argument:{street_name} must be of type string.")
        if not isinstance(geo, str):
            raise TypeError(f"Function argument:{geo} must be of type string.")

        self.name = name
        self.facilities = facilities
        self.washrooms = washrooms
        self.community = community
        self.address = street_num + " " + street_name
        latitude, longitude = map(float, geo.split(","))
        self.point = Point(longitude, latitude)

    def update_address(self, new_address, new_point):
        """
        Update the address of the park.

        Args:
            new_address (str): The new address of the park.
            new_point(Point):The point of the park
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

    def update_washrooms(self, new_washrooms):
        """
        Update the washrooms information of the park.

        Args:
            new_washrooms (str): The new washrooms information of the park.
        """
        if not isinstance(new_washrooms, str):
            raise TypeError(
                f"New community must be a string, got {type(new_washrooms)} instead."
            )

        self.washrooms = new_washrooms
        print("Washrooms updated successfully.")

    def change_community(self, new_community):
        """
        Change the community of the park.

        Args:
            new_address (str): The new address of the park.
        """
        if not isinstance(new_community, str):
            raise TypeError(
                f"New community must be a string, got {type(new_community)} instead."
            )

        self.community = new_community
        print("Community updated successfully.")

    def __str__(self):
        """
        Returns a string representation of the park object.

        Returns:
            str: A string containing the name, facilities, washrooms, local area, and address of the park.

        Raises:
            nothing
        """
        return f"{{Name: {self.name}, Facilities: {self.facilities}, Washrooms: {self.washrooms}, Local_area: {self.community}, Address: {self.address}}}"
