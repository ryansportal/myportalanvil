import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
import requests

@anvil.server.callable
def add_suggestion(text, type):
  app_tables.suggestions_2.add_row(text=text, type=type, created=datetime.now())

#@anvil.server.callable
#def get_suggestions_data():
  #suggestions_data = app_tables.suggestions_2.search()
  #return [dict(row) for row in suggestions_data]
ASANA_ACCESS_TOKEN='2/1125336412773364/1208017081650167:703964a591e4b24d9089be1b83604d6c'
ASANA_PROJECT_ID='1206128442907042'
@anvil.server.callable
def get_asana_tasks():
  url = f'https://app.asana.com/api/1.0/projects/{ASANA_PROJECT_ID}/tasks'
  headers = {
        'Authorization': f'Bearer {ASANA_ACCESS_TOKEN}',
    }
  response = requests.get(url, headers=headers)
  if response.status_code == 200:
        tasks = response.json()['data']
        return tasks
  else:
        return {'error': f'Failed to fetch tasks: {response.status_code}'}
