# This is the Smelk Assistant
from datetime import datetime
# Takes in input and completely parses it. Runs appropriate function, Returns the assistant response
def parse_input(user_input: str):
    # get_weather()
    return "Sorry, I'm currently under works."



def get_weather():
    return
    # Apparently https://openweathermap.org/ is a good API to use for this
    # Or https://pypi.org/project/python-weather/ is a module
    # Or I could use selenium for it and scrape it from google

def get_time():
    return f'It is currently {datetime.now().strftime("%I:%M:%p")}. Have a smelkian day!'
    

# Functions we want to include:
# - Accessing Smelk stock price
# e.t.c.

print(get_time())