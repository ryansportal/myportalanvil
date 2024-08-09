import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

@anvil.server.callable
def add_suggestion(text, type):
  app_tables.suggestions_2.add_row(text=text, type=type, created=datetime.now())

def get_suggestions_data():
  suggestions_data = app_tables.suggestions_2.search()
  return [dict(row) for row in suggestions_data]

  
