"""
Yuxi Chen (Chelsea)
CS 5001, Spring 2024
Final Project
This is the utils file for the final project.!!!Updated Version!!!
"""

import geopandas as gpd  # working with geospatial data
from fiona.crs import from_epsg  # retrieve the CRS based on an EPSG code

WEB_COORDIANTION = 3857
GIS_COORDIANTION = 4326
DEFAULT_DISTANCE = 1000.0


def create_geodataframes(libraries, parks, schools, input_school):
    """
    Creates GeoDataFrames for libraries, parks, and the selected school.

    Args:
        libraries (list): A list of Library objects.
        parks (list): A list of Park objects.
        schools (list): A list of School objects.
        input_school (str): The name of the selected school.

    Returns:
        tuple: A tuple containing GeoDataFrames for libraries, parks, and the selected school.
    """
    # ref Geopandas: https://geopandas.org/en/stable/
    library_geometry_list = []
    for library in libraries:
        library_geometry_list.append(library.point)
    libraries_gdf = gpd.GeoDataFrame(
        libraries, geometry=library_geometry_list, crs=from_epsg(GIS_COORDIANTION)
    )

    park_geometry_list = []
    for park in parks:
        park_geometry_list.append(park.point)
    parks_gdf = gpd.GeoDataFrame(
        parks, geometry=park_geometry_list, crs=from_epsg(GIS_COORDIANTION)
    )

    for school in schools:
        if school.name == input_school:
            selected_school_obj = school
    selected_school_gdf = gpd.GeoDataFrame(
        [selected_school_obj],
        geometry=[selected_school_obj.point],
        crs=from_epsg(GIS_COORDIANTION),
    )

    return libraries_gdf, parks_gdf, selected_school_gdf


def build_buffer_area(selected_school_gdf, distance):
    """
    Builds a buffer area around the selected school.

    Args:
        selected_school_gdf (GeoDataFrame): GeoDataFrame containing the selected school.
        distance (float): The distance to build the buffer area.

    Returns:
        GeoDataFrame: The buffer area around the selected school.
    """
    buffer_area = selected_school_gdf.to_crs(epsg=WEB_COORDIANTION).buffer(
        distance
    )  # creates a buffer area around the selected school(s) in WEB_COORDIANTION system
    buffer_area = buffer_area.to_crs(
        epsg=GIS_COORDIANTION
    )  # transforms this buffer area into GIS_COORDIANTION system
    return buffer_area


def find_parks_and_libraries_within_buffer(parks_gdf, libraries_gdf, buffer_area):
    """
    Finds parks and libraries within the buffer area.

    Args:
        parks_gdf (GeoDataFrame): GeoDataFrame containing park data.
        libraries_gdf (GeoDataFrame): GeoDataFrame containing library data.
        buffer_area (GeoDataFrame): GeoDataFrame representing the buffer area around the school.

    Returns:
        tuple: A tuple containing lists of parks and libraries within the buffer area.
    """
    # Find parks and libraries within the buffer area
    parks_within_buffer = []
    for (
        _,
        park,
    ) in parks_gdf.iterrows():  # not intend to use the row index within the loop
        if park.geometry.within(buffer_area).any():
            parks_within_buffer.append(park)

    libraries_within_buffer = []
    for _, library in libraries_gdf.iterrows():
        if library.geometry.within(buffer_area).any():
            libraries_within_buffer.append(library)
    return parks_within_buffer, libraries_within_buffer
