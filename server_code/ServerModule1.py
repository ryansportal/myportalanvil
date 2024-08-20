import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import date
import requests

#today = str(date.today())

@anvil.server.callable
def add_suggestion(feature, Category, Territory):
  app_tables.suggestions_uk.add_row(feature=feature, Category=Category, Created=date.today(), Territory=Territory)

@anvil.server.callable
def check_user():
  user = anvil.users.get_user()
  if user is None:
    raise anvil.users.AuthenticationFailed('user not logged in')

@anvil.server.callable
def save_home_body_text(updated_text):
 # Try to get the existing row with the name 'home_body'
    setting = app_tables.settings.get(home_body='home_body')
    
    if setting:
        # If the row exists, update it
        setting['home_body'] = updated_text
    else:
        # If the row doesn't exist, create a new one
        app_tables.settings.add_row(home_body='home_body', text=updated_text)