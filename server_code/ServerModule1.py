import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime

@anvil.server.callable
def add_suggestion(text, category, attachments):
  app_tables.suggestions_2.add_row(text=text, category=category, created=datetime.now(), attachments=attachments)