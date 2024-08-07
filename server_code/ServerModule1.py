import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_suggestion(text, category):
  app_tables.suggestions_2.add_row(text=text, category=category, created=datetime.now())