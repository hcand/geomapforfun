"""Main module."""

import ipyleaflet


class Map(ipyleaflet.Map):
    """A custom Map class that extends ipyleaflet.Map.

    This class wraps ipyleaflet.Map and provides convenient methods
    for adding basemaps and Google map layers.
    """

    def __init__(self, center=[0, 0], zoom=2, height="600px", **kwargs):
        """Initialize a Map instance.

        Args:
            center (list): The center coordinates of the map as [latitude, longitude].
                Defaults to [0, 0].
            zoom (int): The initial zoom level of the map. Defaults to 2.
            height (str): The height of the map widget as a CSS value. Defaults to '600px'.
            **kwargs: Additional keyword arguments to pass to ipyleaflet.Map.
        """
        super().__init__(center=center, zoom=zoom, **kwargs)
        self.layout.height = height

    def add_basemap(self, basemap="OpenStreetMap"):
        """Add a basemap layer to the map.

        Args:
            basemap (str): The name of the basemap to add. Defaults to 'OpenStreetMap'.
                This should correspond to an ipyleaflet.basemaps attribute.
        """
        url = eval(f"ipyleaflet.basemaps.{basemap}").url
        tile_layer = ipyleaflet.TileLayer(url=url, name=basemap)
        self.add_layer(tile_layer)
        # basemaps = {
        #    "OpenStreetMap":ipyleaflet.basemaps.OpenStreetMap.Mapnik,
        #    "OpenTopoMap":ipyleaflet.basemaps.OpenTopoMap
        # }

        # if basemap in basemaps:
        #    tile_layer = basemaps[basemap]
        #    url = tile_layer['url']
        #    self.add_layer(ipyleaflet.TileLayer(url=url, name=basemap))

    def add_google_map(self, map_type="ROADMAP"):
        """Add a Google map layer to the map.

        Args:
            map_type (str): The type of Google map to add. Options are:
                - 'ROADMAP': Standard road map (default)
                - 'SATELLITE': Satellite imagery
                - 'HYBRID': Satellite with labels
                - 'TERRAIN': Terrain map
                Defaults to "ROADMAP".
        """
        map_types = {"ROADMAP": "m", "SATELLITE": "s", "HYBRID": "y", "TERRAIN": "p"}
        map_type = map_types[map_type.upper()]
        url = (
            f"https://mt1.google.com/vt/lyrs={map_type.lower()}&x={{x}}&y={{y}}&z={{z}}"
        )
        layer = ipyleaflet.TileLayer(url=url, name="Google map")
        self.add_layer(layer)
