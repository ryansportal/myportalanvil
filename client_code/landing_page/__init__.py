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

   
    def check_user_state(self):
        # GET CURRENT USER
        user = anvil.users.get_user()
        if user is not None:
            # Redirect to 'Home' if the user is already logged in
            if not self.form_redirected:
                open_form('Home')
                self.form_redirected = True
        else:
            # Show login button if no user is logged in
            self.button_login.visible = True
    
    # Log In
    def button_login_click(self, **event_args):
        user = anvil.users.login_with_form(allow_cancel=True)
        self.check_user_state()  # Check user state after login
    
    # Log Out (Assuming logout is handled elsewhere and this form is not used for logout)
    def button_logout_click(self, **event_args):
        anvil.users.logout()
        open_form('landing_page')  # Redirect to landing_page after logging out

    # Ensure proper user state handling on form load
    def user_state(self, user):
        self.button_login.visible = user is None
        self.button_logout.visible = user is not None
