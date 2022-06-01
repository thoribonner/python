import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
  with open(filepath, "w") as file:
    json.dump(data, file)

def load_data(filepath):
  try:
    with open(filepath, "r") as file:
      data = json.load(file)
      return data
  except:
    return {}


if len(sys.argv) == 2:
  command = sys.argv[1].lower()
  data = load_data(SAVED_DATA)

  if command == "save":
    key = input("Enter a key:\n🔑  ")
    data[key] = clipboard.paste()
    save_data(SAVED_DATA, data)
    print("Clipboard saved.")
  elif command == "load":
    key = input("Enter a key:\n🔑  ")
    if key in data:
      clipboard.copy(data[key])
      print("Clipboard loaded.")
    else:
      print("Key does not exist. Existing data:")
  elif command == "list":
    print(data)
  else:
    print('''
    Unknown command.
    Available commands are:

      SAVE  -  Store current clipboard for later access.

      LOAD  -  Load a previously stored clip to clipboard.

      LIST  -  Display a list of all stored clips.
    ''')
else:
  print('''
  Please pass exactly one command.
  Example:
          python3 multiclip.py save

  Available commands are:

      SAVE  -  Store current clipboard for later access.

      LOAD  -  Load a previously stored clip to clipboard.

      LIST  -  Display a list of all stored clips.
  ''')