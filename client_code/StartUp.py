import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import open_form
# This is a module.

def startup():
  try:
    user = anvil.server.call('check_user')
    print(user)
    open_form('Home')
  except anvil.users.AccountIsNotEnabled as e:
    # must be this way round since AccountIsNotEnabled is a subclass of AuthenticationFailes
    print(e)
    open_form('login')
  except anvil.users.AuthenticationFailed as e:
    print(e)
    open_form('login')
  
if __name__ == "__main__":
  startup()
  

