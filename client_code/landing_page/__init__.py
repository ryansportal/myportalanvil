from ._anvil_designer import landing_pageTemplate
from anvil import *
import anvil.server
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class landing_page(landing_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

   
  #GET CURRENT USER
    user = anvil.users.get_user()
    self.user_state(user)
  
# Log In 
    
  def button_login_click(self, **event_args):
    user = anvil.users.login_with_form(allow_cancel=True)
    self.user_state(user)
    

  def user_state(self, user):
    self.button_login.visible = user is None
  

  # Redirect to another form if the user is logged in
    if user is not None:
      open_form('Home')  # Replace 'new_form_name' with the actual form you want to open
  
