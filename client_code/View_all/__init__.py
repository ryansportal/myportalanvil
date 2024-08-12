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

  
    self.repeating_panel_1.items = app_tables.suggestions_uk.search()

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

  def button_logout_click(self, **event_args):
    anvil.users.logout()
    open_form('login')

  def sortby_change(self, **event_args):
    # Fetch data from the table
   # Get the selected field to sort by
    selected_field = self.sortby.selected_value
    
    # Sort the items in the DataGrid
    if selected_field:
      sorted_data = app_tables.suggestions_uk.search(tables.order_by(selected_field))
      self.repeating_panel_1.items = sorted_data
      
