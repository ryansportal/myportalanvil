import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
import requests



@anvil.server.callable
def add_suggestion(text, type):
  app_tables.uk.add_row(text=text, type=type, created=datetime.now())


@anvil.server.callable
def get_data():
    # Retrieve data from 'MyTable'
    return app_tables.uk.search()