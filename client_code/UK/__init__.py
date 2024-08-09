from ._anvil_designer import UKTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class UK(UKTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)


     # Load the data into the RepeatingPanel
    self.load_suggestions_data()
    
  def load_suggestions_data(self):
    suggestions_data = anvil.server.call('get_suggestions_data')  # Call the server function
    self.repeating_panel.items = suggestions_data  # Assuming you have a RepeatingPanel to display the data
   
   
  
#Nav
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

  def data_grid_UK_show(self, **event_args):
   self.repeating_panel = self.load_suggestions_data()
