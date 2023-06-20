import pyautogui
import time
import winsound

"""
========================================================
CHERWELL MOBILE LIVE INVENTORY AUTOMATION SCRIPT
========================================================
"""

back_button = {"x": 28, "y": 59}
search_bar = {"x": 185, "y": 229}
first_search_result = {"x": 267, "y": 344}
location_field = {"x": 886, "y": 418}
inventory_date_field = {"x": 741, "y": 721}
today_date = {"x": 677, "y": 885}

# Define the new location of the asset
newLocation = ""

# Define the delay time in between interactions
SHORT_DELAY = 1
LONG_DELAY = 2

while True:
    # Switch to the terminal
    print("Switching to the terminal")
    pyautogui.hotkey("alt", "tab")

    # Prompt the user to enter the asset tag
    winsound.Beep(1000, 1000)
    asset_tag = input("Enter the asset tag: ")
    print("Starting asset tag:", asset_tag)

    # Switch to Cherwell
    print("Switching to Cherwell")
    pyautogui.hotkey("alt", "tab")
    time.sleep(SHORT_DELAY)

    # Click on the search bar
    print("  Clicking on the search bar")
    pyautogui.click(**search_bar)

    # Select and delete any existing text in the search bar
    print("  Selecting any existing text and deleting it")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")

    # Type the asset tag and press Enter to start the search
    print(f"  Typing the asset tag {asset_tag} and pressing Enter to search")
    pyautogui.write(asset_tag)
    pyautogui.press("enter")
    print("  Waiting for search results")
    time.sleep(LONG_DELAY)

    # Double click on the first search result
    print("  Clicking on the first search result")
    pyautogui.click(**first_search_result)
    pyautogui.click(**first_search_result)
    time.sleep(LONG_DELAY)

    # Update the location field with the new location
    print("  Updating the location field")
    pyautogui.click(**location_field)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    pyautogui.write(newLocation)
    time.sleep(SHORT_DELAY)

    # Update the inventory date field to today's date
    print("  Updating the inventory date field")
    pyautogui.click(**inventory_date_field)
    time.sleep(SHORT_DELAY)
    pyautogui.click(**today_date)
    time.sleep(SHORT_DELAY)

    print("  Clicking on the back button")
    pyautogui.click(**back_button)
    time.sleep(SHORT_DELAY)

    # Play a sound to indicate that the asset has been updated, and print the completed asset tag
    print(f"Completed asset tag: {asset_tag}\n")
