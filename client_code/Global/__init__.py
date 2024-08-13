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
    
# Initialize dropdowns
    self.drop_down_sortglobal.items = [("Category", "Category"), ("Created", "Created")]
    self.drop_down_orderglobal.items = [("Ascending", "Ascending"), ("Descending", "Descending")]

        # Define the territories to be excluded
    self.excluded_territories = ["UK", "South Africa", "US & CA"]

        # Load initial data with sorting
    self.apply_sorting()

    def get_filtered_items(self):
        """Retrieve filtered items based on the excluded territories."""
        excluded_territory_rows = [app_tables.territory.get(Territory=name) for name in self.excluded_territories]

        # Filter out None in case some territories are not found
        excluded_territory_rows = [row for row in excluded_territory_rows if row is not None]

        # Build the query to exclude items linked to the specified territories
        if excluded_territory_rows:
            exclusion_conditions = [q.all_of(Territory=row) for row in excluded_territory_rows]
            query_condition = q.not_(q.any_of(*exclusion_conditions))
        else:
            query_condition = q.all_of()  # This will match all items

        return query_condition

    def apply_sorting(self):
        """Apply sorting and filtering, then update the display."""
        # Get selected values from dropdowns
        sort_field = self.drop_down_sortglobal.selected_value
        sort_order = self.drop_down_orderglobal.selected_value

        # Ensure we have valid selections
        if not sort_field or not sort_order:
            return

        # Determine the sort order (ascending or descending)
        ascending = sort_order == "Ascending"

        # Combine filtering and sorting
        query_condition = self.get_filtered_items()
        sorted_data = app_tables.suggestions_uk.search(
            query_condition,
            tables.order_by(sort_field, ascending=ascending)
        )

        # Update the repeating panel with the filtered and sorted data
        self.repeating_panel_1.items = sorted_data

  def submit_buttonglobal_click(self, **event_args):
        """Triggered when the update button is clicked."""
        self.apply_sorting()



  
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
