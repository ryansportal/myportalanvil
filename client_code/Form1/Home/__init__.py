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

    # Any code you write here will run before the form opens.

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
  def nav_link_click(self, **event_args):
    open_form(event_args['sender'].tag.form_to_open)

  self.label_1.text = f"Our URL hash is: {get_url_hash()}"

  if get_url_hash() == 'stats':
   from Stats import Stats
   self.content_panel.clear()
   self.content_panel.add_component(Stats())
  elif get_url_hash() == 'analysis':
    from Analysis import Analysis
    self.content_panel.clear()
    self.content_panel.add_component(Analysis())