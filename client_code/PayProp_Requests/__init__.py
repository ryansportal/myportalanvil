from ._anvil_designer import PayProp_RequestsTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class PayProp_Requests(PayProp_RequestsTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings
        self.init_components(**properties)

          # Example coordinates for the marker
        latitude = 51.271240
        longitude = 0.191750
      
        base64_icon = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAP1BMVEXbNSn////ZHQb22djYEgDaKBj109LroJ3niobaKxzZIAzzzcvaJRTWAADwubfbLiHjc2733tzlg37gX1jrpKEDjV34AAABNElEQVR4nO3bsW6DMBiF0RQIgZKE0Ob9n7WLWWoGTEX+UJ0zX1n6Vss+nQAAAAAAAAAAAAAAAADgvVyrvV2DA+/13u6xiVX9sbe6UqhQoUKFChUqVKhQoUKFChXGFA7tVsNBCm+fW90OUthsPq5R+HoKCykMoLCQwgAKCykMoLCQwgAKCykMoLCQwgAKCykMoLCQwgAKCykMoLCQwgAKCykMoLDQgQvHhYcXYz47buH4aIff2keeeNzCvluYdX22UxhAYaJwpjCAwkThTGEAhYnCmcIAChOFM4UB/lL41fyjPzOLhdNx/z2tLFxJ4c4UJgoVBlKYKFQYSGGiUGEghYnCdy6cdi+cYgv77pJ5nrPZ+P3MdystXFi9VH/OLczGhdlKwYEAAAAAAAAAAAAAAAAAkPkBqLktxBvvZ98AAAAASUVORK5CYII="


        # Create a marker using the correct syntax
        marker = GoogleMap.Marker(
            position=GoogleMap.LatLng(latitude, longitude),  # Position of the marker
            title="UK",  # Title when hovering over the marker
            icon={
                'url': base64_icon,  # Base64 encoded image data
                'scaledSize': GoogleMap.Size(30, 30)  # Resize the icon (width, height in pixels)
            }
        )
      
              # Example coordinates for the second marker
        latitudesa = -30.559483
        longitudesa = 22.937506

     # Create the second marker with a custom icon
        markersa = GoogleMap.Marker(
            position=GoogleMap.LatLng(latitudesa, longitudesa),
            title="SA",
            icon={
                'url': base64_icon,  # Base64 encoded image data
                'scaledSize': GoogleMap.Size(30, 30)  # Resize the icon (width, height in pixels)
            }
        )

                    # Example coordinates for the second marker
        latitudeus = 35.4279545,
        longitudeus = -100.6958721

     # Create the second marker with a custom icon
        markerus = GoogleMap.Marker(
            position=GoogleMap.LatLng(latitudeus, longitudeus),
            title="US",
            icon={
                'url': base64_icon,  # Base64 encoded image data
                'scaledSize': GoogleMap.Size(30, 30)  # Resize the icon (width, height in pixels)
            }
        )

                          # Example coordinates for the second marker
        latitudeca = 50.393303
        longitudeca = -99.8181455

     # Create the second marker with a custom icon
        markerca = GoogleMap.Marker(
            position=GoogleMap.LatLng(latitudeca, longitudeca),
            title="CA",
            icon={
                'url': base64_icon,  # Base64 encoded image data
                'scaledSize': GoogleMap.Size(30, 30)  # Resize the icon (width, height in pixels)
            }
        )

      
        # Add the marker to the GoogleMap component
        self.map_1.add_component(marker)
        self.map_1.add_component(markersa)
        self.map_1.add_component(markerus)
        self.map_1.add_component(markerca)
      


     

        
 
    def home_button_click(self, **event_args):
     open_form('Home')
    def feedback_button_click(self, **event_args):
     open_form('Feedback') 
    def roadmap_buttton_click(self, **event_args):
     open_form('RoadMap')
    def payprop_requests_button_click(self, **event_args):
      open_form('PayProp_Requests')
  

    def link_1_click(self, **event_args):
      open_form('Global')
    def link_2_click(self, **event_args):
      open_form('UK')
    def link_3_click(self, **event_args):
      open_form('South_Africa')
    def link_4_click(self, **event_args):
      open_form('US_CA')
    def link_5_click(self, **event_args):
      open_form("View_all")

    def button_logout_click(self, **event_args):
      anvil.users.logout()
      open_form('login')


