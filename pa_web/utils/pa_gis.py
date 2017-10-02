from . import geolocator
from flask import current_app
from geopy import Point
from geopy.distance import vincenty

def get_location(location):
    """Return a description of a location retrieved from a geo locator service."""
    return geolocator.geocode(location)

def get_distance_from_arrakeen_m(location):
    """Return distance from arrakeen in meters."""
    l = get_location(location)
    point_location = Point(l.latitude, l.longitude)
    point_arrakeen = Point(current_app.config['PAWEB_ARRAKEEN_LATITUDE'], \
                           current_app.config['PAWEB_ARRAKEEN_LONGITUDE'])
    return vincenty(point_location, point_arrakeen).m 
