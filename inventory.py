import pyautogui
import time

"""
========================================================
CHERWELL INVENTORY AUTOMATION SCRIPT
========================================================

The script carries out the following steps for each asset tag:

Search for it using the search bar
clicks on the first result
updates the location (change this by changing the newLocation variable ex. BBY-SE12-123)
updates the inventoried date to current date
clicks on the back button
repeats this for the list of asset tags (change this by adding in the asset tags in asset_tags_str)

How to run
1. Open Cherwell, and navigate to CMBD (search page)
2. Updade the locations of the buttons to your screen
3. Update the asset_tags_str with the asset tags you want to update
4. Update the newLocation variable with the new location
5. Run the script (run button in top right)

IMPORTANT: DO NOT TOUCH THE KEYBOARD OR MOUSE WHILE SCRIPT IS RUNNING, TO STOP SCRIPT HIT CTRL+C IN CONSOLE
"""

back_button = {"x": 28, "y": 59}
search_bar = {"x": 185, "y": 229}
first_search_result = {"x": 267, "y": 344}
location_field = {"x": 886, "y": 418}
inventory_date_field = {"x": 741, "y": 721}
today_date = {"x": 677, "y": 885}

# Define the new location of the asset
newLocation = "BBY-SE12-301"

# Define the delay time in between interactions
SHORT_DELAY = 1
LONG_DELAY = 2

# All asset tags in one string
asset_tags_str = """

"""

# Split the string into a list of asset tags and remove the "-"
asset_tags = [tag.replace("-", "") for tag in asset_tags_str.split()]

# Iterate over the list of asset tags
for i, asset_tag in enumerate(asset_tags):
    print(f"Starting asset tag {i + 1}/{len(asset_tags)}: {asset_tag}")

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
    time.sleep(SHORT_DELAY)

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

    print(f"Completed asset tag {i + 1}/{len(asset_tags)}: {asset_tag}\n")

print("All asset tags completed")
