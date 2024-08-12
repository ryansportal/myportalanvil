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

    self.sortby.change = self.sortby_change
    self.order_by.change = self.sortby_change#
  
  def sortby_change(self, **event_args):
    # Get the selected field to sort by
    self.selected_field = self.sortby.selected_value
    # Determine the sort order
    self.sort_order = self.order_by.selected_value  # Assuming you have a dropdown or toggle named 'sort_order'
     
# Call a method to apply the sorting
    self.apply_sorting()   
    
  def apply_sorting(self):
        self.apply_sorting()
 #   if not self.selected_field:
 #       return  # No field selected, so do nothing

  #  if self.sort_order == "Ascending":
  #      sorted_data = app_tables.suggestions_uk.search(tables.order_by(self.selected_field))
  #  elif self.sort_order == "Descending":
  #      sorted_data = app_tables.suggestions_uk.search(tables.order_by(self.selected_field, ascending=False))

  #  self.repeating_panel_1.items = sorted_data
    
  def outlined_button_1_click(self, **event_args):
   #  Sort the items in the DataGrid
    if self.selected_field:
        if self.sort_order == "Ascending":
            sorted_data = app_tables.suggestions_uk.search(tables.order_by(self.selected_field))
        elif self.sort_order == "Descending":
            sorted_data = app_tables.suggestions_uk.search(tables.order_by(self.selected_field, ascending=False))

        
        self.repeating_panel_1.items = sorted_data


 
