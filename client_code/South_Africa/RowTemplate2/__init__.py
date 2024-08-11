from ._anvil_designer import RowTemplate2Template
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate2(RowTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.label_feature.text = self.item['feature']
    self.label_category.text = self.item['category']['name']  # Access the 'name' field from the linked 'category'
    self.label_created.text = str(self.item['created'])  # Convert created date to string, if necessary


    # Any code you write here will run before the form opens.
