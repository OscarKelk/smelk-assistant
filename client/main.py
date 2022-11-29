# Client to provide the Smelk Assistant with inputs and to handle responses
import json
import pathlib
import time

from smelk_assistant_base import smelkassistant

config = {}
data = {}
history = []


def create_program_files():
    # Check if files exist and create defaults if not so

    if not pathlib.Path("config.json").is_file():
        with open("config.json", "w") as f:
            json.dump({"data_path": "data.json", "history_path": "history.json", "smelk_logo_path": "smelk_logo.txt"},
                      f, indent=4)

    if not pathlib.Path("data.json").is_file():
        with open("data.json", "w") as f:
            json.dump({"program_opened": 0, "questions_asked": 0}, f, indent=4)

    if not pathlib.Path("history.json").is_file():
        with open("history.json", "w") as f:
            json.dump([], f, indent=4)

    if not pathlib.Path("smelk_logo.txt").is_file():
        with open("smelk_logo.txt", "w") as f:
            f.write("    ________      ________\n"
                    "- ~|        |----|        |~ -\n"
                    "   |        |    |        |\n"
                    "    `.____.'      `.____.'\n"
                    "\n"
                    "\n"
                    "            __ __\n"
                    "            |_|_|\n"
                    "")


def load_config():
    global config
    with open("config.json", "r") as f:
        config = json.load(f)


def load_data():
    global data
    with open(config["data_path"], "r") as f:  # Load from file
        data = json.load(f)

    if "program_opened" not in data:  # Insert program opened count into data
        data["program_opened"] = 0
    data["program_opened"] += 1  # Update program opened count


def load_history():
    global history
    with open(config["history_path"], "r") as f:  # Load from file
        history = json.load(f)


def save_data():
    global data
    with open(config["data_path"], "w") as f:  # Open for writing
        json.dump(data, f, indent=4)  # Write to file


def save_history():
    global history
    with open(config["history_path"], "w") as f:  # Open for writing
        json.dump(history, f, indent=4)  # Write to file


def log_history(question: str, response: str, timestamp: int = int(time.time())):
    history.append({
        "question": question,
        "response": response,
        "timestamp": timestamp
    })


create_program_files()

load_config()
load_data()
load_history()

smelk_logo = pathlib.Path(config["smelk_logo_path"]).read_text()
print(smelk_logo)

if data["program_opened"] < 2:  # Display primary welcome message only on first open
    print("Hi, I'm the Smelk Innovations Personal Assistant.")
    print("I'm here to help you in whatever way possible, there are many things I can do!")

print("Type <exit> to leave")
print("How can we get started?")
while True:
    user_input = input("> ")
    if user_input == "<exit>":
        break
    assistant_response = smelkassistant.parse_input(user_input)

    # Log questions to data and history
    if "questions_asked" not in data:
        data["questions_asked"] = 0
    data["questions_asked"] += 1
    log_history(user_input, assistant_response)

    print("\n", end="")
    print(assistant_response)
    print("\n", end="")

    save_data()
    save_history()

save_data()
save_history()
exit()
