from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_feature.text = self.item['feature']
    self.label_category.text = self.item['Category']['name']  # Access the 'name' field from the linked 'category'
    self.label_created.text = str(self.item['Created'])  # Convert created date to string, if necessary

   
