import re

def format(RawLength:str):
    # Formatting of time into seconds for sleep()
    if bool(re.findall(r"\b\d{2} seconds\b", RawLength)):
        length = int(RawLength[:2])
    if bool(re.findall(r"\b\d{1,2}:\d{2}\b", RawLength)): # m:s
        length = int(RawLength.split(":")[1]) * 60 + int(RawLength.split(":")[1])
    if bool(re.findall(r"\b\d{1,2}:\d{2}:\d{2}\b", RawLength)): # h:m:s
        length = int(RawLength.split(":")[1]) * 3600 + int(RawLength.split(":")[1]) * 60 + int(RawLength.split(":")[1])

    return length
