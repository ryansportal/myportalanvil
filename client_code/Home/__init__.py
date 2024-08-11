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


    #Logout
    
    user = anvil.users.get_user()
    self.user_state(user)
    
  def button_logout_click(self, **event_args):
   anvil.users.logout()
     # Redirect to another form if the user logs out
   if user is None:
      open_form('landing_page')  
  

    

