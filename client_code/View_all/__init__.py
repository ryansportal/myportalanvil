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

#Sort and Order
    
# Initialize dropdowns
    self.drop_down_sort.items = [("Category", "Category"), ("Created", "Created"), ("Territory", "Territory")]
    self.drop_down_order.items = [("Ascending", "Ascending"), ("Descending", "Descending")]

        # Bind the update button click event to the method
    self.update_button.set_event_handler('click', self.update_sorting_order)

        # Load initial data
    self.apply_sorting()

  def submit_button_click(self, **event_args):
        # Apply sorting based on the current dropdown values
        self.apply_sorting()
 

  def apply_sorting(self):
        # Get selected values from dropdowns
        sort_field = self.drop_down_sort.selected_value
        sort_order = self.drop_down_order.selected_value

        # Ensure we have valid selections
        if not sort_field or not sort_order:
            return

        # Determine the sort order (ascending or descending)
        ascending = sort_order == "Ascending"

        # Fetch and sort data
        sorted_data = app_tables.suggestions_uk.search(
            tables.order_by(sort_field, ascending=ascending)
        )

        # Update the repeating panel with sorted data
        self.repeating_panel_1.items = sorted_data