
import folium

class Map(folium.Map):
    """A custom Map class that extends folium.Map with layer control.
    
    This class wraps folium.Map and automatically adds layer control
    functionality for better map management.
    """
    
    def __init__(self, center=(0, 0), zoom=2, **kwargs):
        """Initialize a Map instance.
        
        Args:
            center (tuple): The center coordinates of the map as (latitude, longitude).
                Defaults to (0, 0).
            zoom (int): The initial zoom level of the map. Defaults to 2.
            **kwargs: Additional keyword arguments to pass to folium.Map.
        """
        super().__init__(location=center, zoom_start=zoom, **kwargs)
        folium.LayerControl().add_to(self)