"""
Yuxi Chen (Chelsea)
CS 5001, Spring 2024
Final Project
This is the visualization file for the final project.!!!Updated Version!!!
"""

import folium  # creating interactive maps
import webbrowser  # opening URLs in the default web browser
import os
from views.utils_views import (
    create_geodataframes,
    build_buffer_area,
    find_parks_and_libraries_within_buffer,
)


WEB_COORDIANTION = 3857
GIS_COORDIANTION = 4326
DEFAULT_DISTANCE = 1000.0
MAX_WIDTH = 350
INDEX_ZERO = 0


def initialize_map(selected_school_gdf):
    """
    Initializes the map with center coordinates and zoom level.

    Args:
        selected_school_gdf (GeoDataFrame): GeoDataFrame containing the selected school.

    Returns:
        folium.Map: Initialized map object.
    """
    # ref Folium: https://pypi.org/project/folium/
    center_lat, center_lng = (
        selected_school_gdf.geometry.y,
        selected_school_gdf.geometry.x,
    )
    map = folium.Map(location=[center_lat, center_lng], zoom_start=14)
    return map


def add_markers_to_map(
    map, selected_school_gdf, parks_within_buffer, libraries_within_buffer
):
    """
    Adds markers for schools, parks, and libraries to the map.

    Args:
        map (folium.Map): Map object to which markers will be added.
        selected_school_gdf (GeoDataFrame): GeoDataFrame containing the selected school.
        parks_within_buffer (list): List of parks within the buffer area.
        libraries_within_buffer (list): List of libraries within the buffer area.

    Returns:
        None
    """
    # ref HTML Tutorial: https://www.w3schools.com/html/
    selected_school_obj = selected_school_gdf.values[INDEX_ZERO][INDEX_ZERO]
    school_pop_text = f"<h3>{selected_school_obj.name}</h3>\
<p><b>Address</b>: {selected_school_obj.address}</p>\
<p><b>Community</b>: {selected_school_obj.community}</p>\
<p><b>Category</b>: {selected_school_obj.category}</p>"
    school_popup = folium.Popup(school_pop_text, max_width=MAX_WIDTH)
    folium.Marker(
        location=[selected_school_gdf.geometry.y, selected_school_gdf.geometry.x],
        popup=school_popup,
        icon=folium.Icon(icon="university", color="blue", prefix="fa"),
    ).add_to(map)

    for park in parks_within_buffer:
        park_obj = park.values[0]
        park_pop_txt = f"<h3>{park_obj.name}</h3>\
<p><b>Address</b>: {park_obj.address}</p>\
<p><b>Community</b>: {park_obj.community}</p>\
<p><b>Facilities</b>: {park_obj.facilities}</p>\
<p><b>Washrooms</b>: {park_obj.washrooms}</p>"
        park_pop_up = folium.Popup(park_pop_txt, max_width=MAX_WIDTH)
        folium.Marker(
            location=[park.geometry.y, park.geometry.x],
            popup=park_pop_up,
            icon=folium.Icon(icon="leaf", color="green"),
        ).add_to(map)

    for library in libraries_within_buffer:
        library_obj = library.values[0]
        library_pop_txt = f"<h3>{library_obj.name}</h3>\
<p><b>Address</b>: {library_obj.address}</p>\
<p><b>Community</b>: {library_obj.community}</p>\
<p><b>Url</b>: <a href={library_obj.url}>{library_obj.url}</a></p>"
        library_pop_up = folium.Popup(library_pop_txt, max_width=MAX_WIDTH)
        folium.Marker(
            location=[library.geometry.y, library.geometry.x],
            popup=library_pop_up,
            icon=folium.Icon(icon="book", color="blue"),
        ).add_to(map)


def add_buffer_area_to_map(map, buffer_area):
    """
    Adds buffer area to the map.

    Args:
        map (folium.Map): Map object to which buffer area will be added.
        buffer_area (GeoDataFrame): GeoDataFrame representing the buffer area around the school.

    Returns:
        None
    """
    folium.GeoJson(buffer_area.to_json(), name="Buffer Area").add_to(map)


def save_and_open_map(map):
    """
    Saves map as html file and opens it in a web browser.

    Args:
        map (folium.Map): Map object to be saved and opened.

    Returns:
        None
    """
    parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    file_path = os.path.join(parent_path, "map.html")
    map.save(file_path)
    webbrowser.open("file://" + file_path)


def display_map(schools, libraries, parks, input_school, distance):
    """
    Displays a map showing nearby parks and libraries based on user input.

    Args:
        schools (list): A list of School objects.
        libraries (list): A list of Library objects.
        parks (list): A list of Park objects.

    Returns:
        None
    """
    if not isinstance(schools, list):
        raise TypeError("schools must be a list")
    if not isinstance(libraries, list):
        raise TypeError("libraries must be a list")
    if not isinstance(parks, list):
        raise TypeError("parks must be a list")

    # get info we need on map
    libraries_gdf, parks_gdf, selected_school_gdf = create_geodataframes(
        libraries, parks, schools, input_school
    )
    buffer_area = build_buffer_area(selected_school_gdf, distance)
    parks_within_buffer, libraries_within_buffer = (
        find_parks_and_libraries_within_buffer(parks_gdf, libraries_gdf, buffer_area)
    )
    # display info we have on map
    map = initialize_map(selected_school_gdf)
    add_markers_to_map(
        map, selected_school_gdf, parks_within_buffer, libraries_within_buffer
    )
    add_buffer_area_to_map(map, buffer_area)
    # save map as html file and open it in a web browser
    save_and_open_map(map)
