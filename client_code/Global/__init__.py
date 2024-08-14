from ._anvil_designer import GlobalTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Global(GlobalTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

# Populate data 1
    
# Define the territories to be excluded
    excluded_territories = ["UK", "South Africa", "US & CA"]  # List of territory names to exclude
        
        # Retrieve the rows to be excluded from the 'territory' table
    excluded_territory_rows = [app_tables.territory.get(Territory=name) for name in excluded_territories]

        # Filter out None in case some territories are not found
    excluded_territory_rows = [row for row in excluded_territory_rows if row is not None]

        # Build the query to exclude items linked to the specified territories
    if excluded_territory_rows:
            # Create a list of query conditions to exclude
            exclusion_conditions = [q.all_of(Territory=row) for row in excluded_territory_rows]
            # Use q.not_ to exclude items linked to any of these territories
            query_condition = q.not_(q.any_of(*exclusion_conditions))
    else:
            # If no territories are found, do not exclude any items
            query_condition = q.all_of()  # This will match all items

        # Fetch and display items from suggestions_uk based on the filter
    self.repeating_panel_1.items = app_tables.suggestions_uk.search(query_condition)


  #Sort and Order
    
  # Initialize dropdowns
    self.drop_down_sort.items = [("Category", "Category"), ("Created", "Created")]
    self.drop_down_order.items = [("Ascending", "Ascending"), ("Descending", "Descending")]
    
        # Bind the update button click event to the method
    #self.update_button.set_event_handler('click', self.update_sorting_order)

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





  # Populate data 2
    
# Define the territories to be excluded
   excluded_territories = ["UK", "South Africa", "US & CA"]  # List of territory names to exclude
        
        # Retrieve the rows to be excluded from the 'territory' table
   excluded_territory_rows = [app_tables.territory.get(Territory=name) for name in excluded_territories]

        # Filter out None in case some territories are not found
   excluded_territory_rows = [row for row in excluded_territory_rows if row is not None]

        # Build the query to exclude items linked to the specified territories
   if excluded_territory_rows:
            # Create a list of query conditions to exclude
            exclusion_conditions = [q.all_of(Territory=row) for row in excluded_territory_rows]
            # Use q.not_ to exclude items linked to any of these territories
            query_condition = q.not_(q.any_of(*exclusion_conditions))
   else:
            # If no territories are found, do not exclude any items
            query_condition = q.all_of()  # This will match all items

        # Fetch and display items from suggestions_uk based on the filter
   self.repeating_panel_1.items = app_tables.suggestions_uk.search(query_condition)


  
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
  def link_5_click(self, **event_args):
    open_form('View_all')

  def button_logout_click(self, **event_args):
    anvil.users.logout()
    open_form('login')
