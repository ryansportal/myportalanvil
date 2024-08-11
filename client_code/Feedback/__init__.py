from ._anvil_designer import FeedbackTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Feedback(FeedbackTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.category_dd.items = [(r["name"], r) for r in app_tables.categories.search()]
    self.dd_territory.items = [(r["territory"], r) for r in app_tables.territory.search()]

  def category_dd_change(self, **event_args):
    """This method is called when an item is selected"""
  def dd_territory_change(self, **event_args):
    """This method is called when an item is selected"""
    
  def validate_fields(self):
    suggestion = self.suggestion_box.text
    drop_down = self.category_dd.selected_value
    drop_down_territory = self.dd_territory.selected_value
    
    if not suggestion or not drop_down or not drop_down_territory:
      alert("Please complete all fields", title="Validation Error")
      return False
    return True

  def clear_inputs(self):
    self.suggestion_box.text = ""
    self.category_dd.selected_value = None
    self.dd_territory.selected_value = None

  def submit_button_click(self, **event_args):
    if self.validate_fields():
      anvil.server.call(
        "add_suggestion", self.suggestion_box.text, self.category_dd.selected_value, self.dd_territory.selected_value
      )
      alert("Form submitted")
      self.clear_inputs()


   #Link Nav Bar

  def home_button_click(self, **event_args):
    open_form('Home')

  def feedback_button_click(self, **event_args):
    open_form('Feedback')

  def roadmap_buttton_click(self, **event_args):
   open_form('RoadMap')

  def payprop_requests_button_click(self, **event_args):
    open_form('PayProp_Requests')

   # Log Out

  def button_logout_click(self, **event_args):
    anvil.users.logout()
    open_form('login')
 
  
