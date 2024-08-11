from ._anvil_designer import RoadMapTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RoadMap(RoadMapTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)


  
  #Link Nav Bar
  def home_button_click(self, **event_args):
    open_form('Home')
  def feedback_button_click(self, **event_args):
    open_form('Feedback')
  def roadmap_buttton_click(self, **event_args):
   open_form('RoadMap')
  def payprop_requests_button_click(self, **event_args):
    open_form('PayProp_Requests')
  def link_5_click(self, **event_args):
    open_form("View_all")
