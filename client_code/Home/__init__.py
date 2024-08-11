from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
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
    open_form('landing_page')  # Redirect to landing_page after logging out

   # Redirect to another form if the user is logged in
    user = anvil.users.get_user()
    self.user_state(user)
    if user is not None:
      open_form('Home')  # Replace 'new_form_name' with the actual form you want to open
      
