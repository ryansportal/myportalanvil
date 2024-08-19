from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables



class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
   # anvil.users.login_with_form()
   # print(f"This user has logged in: {anvil.users.get_user()['email']}")


        # Example data model
    self.init_components() 


    def home_body_change(self, **event_args):
        # Update the data model with the new text
        self.item['home_body'] = self.home_body.text
        
        # This will automatically update the UI if the text box is bound to self.item['home_body']
        self.refresh_data_bindings()


  
   #Link Nav Bar

  def home_button_click(self, **event_args):
    open_form('Home')

  def feedback_button_click(self, **event_args):
    open_form('Feedback')

  def roadmap_buttton_click(self, **event_args):
   open_form('RoadMap')

  def payprop_requests_button_click(self, **event_args):
    open_form('PayProp_Requests')

  def button_logout_click(self, **event_args):
    anvil.users.logout()
    open_form('login')






 