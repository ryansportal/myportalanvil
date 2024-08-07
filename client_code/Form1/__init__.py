from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    
    # Any code you write here will run before the form opens.
    self.category_dd.items = [(r['name'], r) for r in app_tables.categories.search()]
  
    

  def category_dd_change(self, **event_args):
    """This method is called when an item is selected"""

  def validate_fields(self):
    suggestion = self.suggestion_box.text
    drop_down = self.category_dd.selected_value
    if not suggestion or not drop_down:
      alert('Please complete all fields', title='Validation Error')
      return False
    return True
  
  def clear_inputs (self):
    self.suggestion_box.text = ""
    self.category_dd.selected_value = None

    
  def submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.validate_fields():
      anvil.server.call( 'add_suggestion', self.suggestion_box.text, self.category_dd.selected_value)
      alert("Form submitted")
      self.clear_inputs()

  


  


  
