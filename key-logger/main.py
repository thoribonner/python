import json
import pynput
from pynput.keyboard import Key, Listener, KeyCode

KEYLOG = "keylog.json"


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


key_data = load_data(KEYLOG)


def on_press(key):
    pass


def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False
    else:
        try:
            key_data[key.char] += 1
            save_data(KEYLOG, key_data)
        except AttributeError:
            print('special key {0} pressed'.format(key))
            pass


with Listener(on_press=on_press,
              on_release=on_release) as listener:
    listener.join()

#abcdefghijklmnopqrstuvwxyz1234567890,./;'[]\-=`<>?:"{}|~!@#$%^&*()_+