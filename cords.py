import pyautogui
import time

while True:
    current_mouse_position = pyautogui.position()  # get current mouse position
    print(
        '{{"x": {}, "y": {}}}'.format(
            current_mouse_position.x, current_mouse_position.y
        )
    )
    time.sleep(1)  # wait for a second
