"""
Yuxi Chen (Chelsea)
CS 5001, Spring 2024
Final Project
This is the interaction file for the final project.!!! UPDATED VERSION!!!
"""

import tkinter as tk  # creating GUI applications
from views.visualization import display_map

DEFAULT_DISTANCE = 1000.0
TRANS_KM = 1000
INDEX_ZERO = 0


class MapApplication:
    """
    Represents a Tkinter application for displaying maps with schools, libraries, and parks.

    Attributes:
        master: The root window of the application.
        schools (list): A list of School objects.
        libraries (list): A list of Library objects.
        parks (list): A list of Park objects.
        school_names (list): A list of school names for selection.

    Methods:
        __init__: Initializes the MapApplication with the root window and other necessary components.
        retrieve_user_input: Fetches selected school and entered distance from GUI elements.
    """

    def __init__(self, schools, libraries, parks, school_names):
        """
        Initializes the MapApplication with the root window and other necessary components.

        Args:
            schools (list): A list of School objects.
            libraries (list): A list of Library objects.
            parks (list): A list of Park objects.
            school_names (list): A list of school names for selection.

        Returns:
            None
        """
        # initialize the instance of the root window and set its title
        # ref Tkinter: https://www.linkedin.com/learning/python-gui-development-with-tkinter-2
        root = tk.Tk()
        root.geometry("800x600")
        self.master = root
        self.master.title("Map Application")

        # Create GUI elements for school selection and distance input
        self.school_label = tk.Label(self.master, text="Select school:")
        self.school_label.pack()
        self.school_var = tk.StringVar()
        self.school_var.set(school_names[INDEX_ZERO])  # set default school
        self.school_option = tk.OptionMenu(
            self.master, self.school_var, *school_names
        )  # Creating an option menu for selecting schools
        self.school_option.pack()

        self.distance_label = tk.Label(
            self.master, text="Enter distance (in kilometers):"
        )
        self.distance_label.pack()
        self.distance_entry = tk.Entry(self.master)
        self.distance_entry.pack()

        # Create GUI elements for confirm button and error message window
        def show_map():
            try:
                input_school, distance = self.retrieve_user_input()
                display_map(schools, libraries, parks, input_school, distance)
            except ValueError:
                # Display error message in a pop-up window
                error_message = tk.Toplevel(self.master)
                error_message.title("Error")
                error_message.geometry("300x100")
                error_label = tk.Label(
                    error_message, text="Distance must be a number greater than zero."
                )
                error_label.pack()
                confirm_button = tk.Button(
                    error_message, text="Confirm", command=error_message.destroy
                )
                confirm_button.pack()

        self.show_button = tk.Button(
            self.master, text="Show Nearby Parks And Libraries", command=show_map
        )
        self.show_button.pack()

        # Frame for displaying the map
        self.map_frame = tk.Frame(self.master)
        self.map_frame.pack()

    def retrieve_user_input(self):
        """
        Fetches selected school and entered distance from GUI elements.

        Returns:
            tuple: A tuple containing the selected school name and entered distance.
        """
        # Fetch selected school and entered distance from GUI elements
        input_school = self.school_var.get()
        distance_str = self.distance_entry.get()

        # Handle the distance information
        if distance_str:
            distance = float(distance_str)
            if distance <= 0:
                raise ValueError("Distance must be a number greater than zero.")
            distance *= TRANS_KM
        else:
            distance = DEFAULT_DISTANCE

        return input_school, distance
