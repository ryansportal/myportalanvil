from ._anvil_designer import RowTemplate4Template
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate4(RowTemplate4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Inside RowTemplate1 form for each row in the Data Grid
    self.label_feature.text = self.item['feature']
    self.label_category.text = self.item['category']['name']  # Access the 'name' field from the linked 'category'
    self.label_created.text = str(self.item['created'])  # Convert created date to string, if necessary
    self.label_territory.text = self.item['territory']['territory']  # Access the 'name' field from the linked 'category'


    # Any code you write here will run before the form opens.
