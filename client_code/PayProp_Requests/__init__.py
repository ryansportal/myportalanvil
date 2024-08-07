from ._anvil_designer import PayProp_RequestsTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class PayProp_Requests(PayProp_RequestsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    #Link Nav Bar
  def H_home_button_click(self, **event_args):
    open_form("Home")
  def H_feedback_button_click(self, **event_args):
    open_form("Feedback")
  def H_PP_Requests_click(self, **event_args):
    open_form("PayProp_Requests")
  def h_roadmap_click(self, **event_args):
    open_form("RoadMap")
