# This is the Smelk Assistant
import datetime
import re
from time import sleep

from smelk_assistant_base.assistant_functions import time,timer


# Takes in input and completely parses it. Returns the assistant response
def parse_input(user_input: str):
    if bool(re.findall(r"\btime\b", user_input)):
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
    elif bool(re.findall(r"\btimer\b", user_input)):
        length = []

        length = re.findall(r"\b\d{1,2} seconds\b", user_input)
        if length == []:
            length1 = re.findall(r"\b\d{1,2}:\d{2}\b", user_input)
            length2 = re.findall(r"\b\d{1,2}:\d{2}:\d{2}\b", user_input) # Check for suitable time formats
            if length2 == []:
                length = length1
            else:
                length = length2

        if length != []:
            waitTime = timer.format(length[0])
            print(f'\nTimer starting: {length[0]}', end='')
            sleep(waitTime)
            return "Time's up!"
        else:
            return "Try again, please provide your desired time in seconds, or M:S"
    else:
        return "Sorry. I don't know what you're asking for"

