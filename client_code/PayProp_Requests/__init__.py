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
  def home_button_click(self, **event_args):
    open_form('Home')

  def feedback_button_click(self, **event_args):
    open_form('Feedback') 
  def roadmap_buttton_click(self, **event_args):
   open_form('RoadMap')
  def payprop_requests_button_click(self, **event_args):
    open_form('PayProp_Requests')
  
  
  class PayProp_Requests(PayProp_RequestsTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
        data = anvil.server.call('database_form')

        if data:
          first_item = data [0]
          self.title_label.text = first_item ['type']
          self.author_label.text = first_item ['text']
      

  

 
      