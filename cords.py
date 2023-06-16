import pyautogui
import time

while True:
    current_mouse_position = pyautogui.position()  # get current mouse position
    print(current_mouse_position)
    time.sleep(1)  # wait for a second
