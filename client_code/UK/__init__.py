from ._anvil_designer import UKTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class UK(UKTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  # Any code you write here will run before the form opens.
    self.category_dd.items = [(r["name"], r) for r in app_tables.categories.search()]

  def category_dd_change(self, **event_args):
    """This method is called when an item is selected"""

  def validate_fields(self):
    suggestion = self.suggestion_box.text
    drop_down = self.category_dd.selected_value
    if not suggestion or not drop_down:
      alert("Please complete all fields", title="Validation Error")
      return False
    return True

  def clear_inputs(self):
    self.suggestion_box.text = ""
    self.category_dd.selected_value = None

  def submit_button_click(self, **event_args):
    if self.validate_fields():
      anvil.server.call(
        "add_suggestion", self.suggestion_box.text, self.category_dd.selected_value
      )
      alert("Form submitted")
      self.clear_inputs()

    


























  
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
