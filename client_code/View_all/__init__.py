from ._anvil_designer import View_allTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class View_all(View_allTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.



  def home_button_click(self, **event_args):
     open_form('Home')

  def feedback_button_click(self, **event_args):
    open_form('Feedback')

  def roadmap_buttton_click(self, **event_args):
   open_form('RoadMap')

  def payprop_requests_button_click(self, **event_args):
    open_form('PayProp_Requests')

    # Any code you write here will run before the form opens.
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