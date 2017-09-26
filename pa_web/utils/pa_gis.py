from . import geolocator

def get_location(location):
    """Return a description of a location retrieved from a geo locator service."""
    return geolocator.geocode(location)
