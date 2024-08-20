from ._anvil_designer import HomeTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables



class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
     # Set initial text
   # Define the mu_home_body variable
        self.mu_home_body = (
            "Vision and Strategy: Define the product's vision, strategy, and roadmap. "
            "Ensure the product aligns with the company’s overall goals and market needs.\n"
            "Cross-functional Leadership: Act as the bridge between different departments - "
            "Work closely with dev, design, marketing, sales and client services.\n"
            "Prioritization: Prioritize features, set timelines, and manage the product backlog. "
            "Decide what gets built and when.\n"
            "Management: Communicate with senior leadership team to align expectations and keep "
            "them informed about the product's progress and direction.\n"
            "Market Research: Analyze market trends, customer feedback, and competition.\n\n"
            "Strong communication and organizational skills.\n"
            "Strategic thinking and problem-solving abilities. Change from reactive to proactive.\n"
            "Good understanding of the market, customers, competition, and the user interface.\n"
            "Work collaboratively with multiple departments and territories and pull in the "
            "correct resource to avoid issues or delays further down the line."
        )

        # Set the text area value to mu_home_body
        self.home_body.text = self.mu_home_body

  def home_body_change(self, **event_args):
 # Update the mu_home_body variable with the text area content
    self.mu_home_body = self.home_body.text
    
    # Example: Save to a database or server
    anvil.server.call('save_home_body_text', self.mu_home_body)


  
   #Link Nav Bar

  def home_button_click(self, **event_args):
    open_form('Home')

  def feedback_button_click(self, **event_args):
    open_form('Feedback')

  def roadmap_buttton_click(self, **event_args):
   open_form('RoadMap')

  def payprop_requests_button_click(self, **event_args):
    open_form('PayProp_Requests')

  def button_logout_click(self, **event_args):
    anvil.users.logout()
    open_form('login')






 