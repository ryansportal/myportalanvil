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
    self.load_asana_tasks()

  def load_asana_tasks(self):
    tasks = anvil.server.call('get_asana_tasks')

    if 'error' in tasks:
      alert(tasks['error'])
    else:
      self.display_tasks(tasks)

  def display_tasks(self, tasks):
    self.repeating_panel.items = tasks
 
  #   data = anvil.server.call('get_suggestions_data')


    #Link Nav Bar
  def home_button_click(self, **event_args):
    open_form('Home')

  def feedback_button_click(self, **event_args):
    open_form('Feedback') 
  def roadmap_buttton_click(self, **event_args):
   open_form('RoadMap')
  def payprop_requests_button_click(self, **event_args):
    open_form('PayProp_Requests')




  



 
      