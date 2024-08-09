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













  
    def home_button_click(self, **event_args):
     open_form('Home')

    def feedback_button_click(self, **event_args):
     open_form('Feedback') 
    def roadmap_buttton_click(self, **event_args):
     open_form('RoadMap')

    def link_1_click(self, **event_args):
      open_form('Global')

    def link_2_click(self, **event_args):
      open_form('UK')
  