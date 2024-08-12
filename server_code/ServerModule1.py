import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
import requests



@anvil.server.callable
def add_suggestion(feature, category, territory):
  app_tables.suggestions_uk.add_row(feature=feature, category=category, created=datetime.now(), territory=territory)

@anvil.server.callable
def check_user():
  user = anvil.users.get_user()
  if user is None:
    raise anvil.users.AuthenticationFailed('user not logged in')
 