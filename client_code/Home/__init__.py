from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  
  def H_home_button_click(self, **event_args):
   open_form('Home')

  def H_feedback_button_click(self, **event_args):
   open_form('Feedback')
