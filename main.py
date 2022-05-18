import time
from datetime import datetime
from pynput.keyboard import Controller, Key
from zoom_calls import zoom_calls
import webbrowser

ZOOM_LINK = HOUR = 0
START_TIME = MIN = 1
END_TIME = 2
EVENT_NAME = 3

keyboard = Controller()

isStarted = False

for call in zoom_calls:
    while True:
        if not isStarted:
            print("Waiting for " + call[EVENT_NAME] +
                  " to start at " + call[START_TIME] + "...")
            if datetime.now().hour == int(call[START_TIME].split(':')[HOUR]) and datetime.now().minute == int(call[START_TIME].split(':')[MIN]):
                webbrowser.open(call[ZOOM_LINK])
                isStarted = True
        else:
            print("Waiting for " + call[EVENT_NAME] +
                  " to end at " + call[END_TIME] + "...")
            if datetime.now().hour == int(call[END_TIME].split(':')[HOUR]) and datetime.now().minute == int(call[END_TIME].split(':')[MIN]):
                keyboard.press(Key.cmd)
                keyboard.press('w')  # Default end-call for zoom is Cmd/Ctrl W
                time.sleep(1)
                keyboard.press(Key.enter)
                isStarted = False
                break  # Move on to the next zoom call in the array
        time.sleep(5)
