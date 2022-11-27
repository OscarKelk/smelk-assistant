# This is the Smelk Assistant
import datetime

from smelk_assistant_base.assistant_functions import time


# Takes in input and completely parses it. Returns the assistant response
def parse_input(user_input: str):
    if "time" in user_input:
        suitable_activity = "to do anything you wish"  # Backup activity if the others dont work for some reason
        hour = datetime.datetime.now().hour
        if 21 <= hour <= 23 or 0 <= hour <= 5:
            suitable_activity = "to go to sleep"
        elif 6 <= hour <= 10:
            suitable_activity = "to get ready for the day"
        elif 11 <= hour <= 16:
            suitable_activity = "to do all the things you yearn for"
        elif 17 <= hour <= 20:
            suitable_activity = "to settle down for the night"

        return f"The time is {time.Current().get_time()}.\nWhat a great time {suitable_activity}!"
    else:
        return "Sorry. I don't know what you're asking for"

