import pyautogui
import time

"""
========================================================
CHERWELL DECOMISSION AUTOMATION SCRIPT
========================================================

The script carries out the following steps for each asset tag:

1. It logs the number of the current asset tag being processed.
2. It clicks on the search bar.
3. It selects any existing text in the search bar and deletes it.
4. It types in the asset tag and presses Enter to search for the asset.
5. It waits for the search results to appear.
6. It clicks on the first search result.
7. It clicks on the location field, selects any existing text, deletes it, and types in the new location.
8. It clicks on the primary user field, selects any text, and deletes it.
9. It clicks on the station ID field, selects any text, and deletes it.
10. It clicks on the inventory date field, selects any date, and then selects today's date.
11. It clicks on the decommision button.
12. It clicks on the back button to return to the search page.
13. It waits for it to go back to the search page before starting the next asset tag.

IMPORTANT: 

- To stop the script from running while it is, move your mouse to the top left of the screen.
- Do not use your computer while the script is running, as it controls your mouse and keyboard. 
- The coordinates used in this script might not match the exact location of the buttons on your screen. You need to adjust the x and y values accordingly.
- Make sure Cherwell is open in the search page and in full screen and visible on your screen before running the script.

"""

# Define the coordinates
back_button = {"x": 28, "y": 59}
search_bar = {"x": 185, "y": 229}
primary_user = {"x": 655, "y": 492}
first_search_result = {"x": 267, "y": 344}
location_field = {"x": 886, "y": 418}
station_ID = {"x": 387, "y": 418}
inventory_date_field = {"x": 741, "y": 721}
today_date = {"x": 677, "y": 885}
decommision_button = {"x": 123, "y": 250}

# Define the new location of the asset
newLocation = "BBY-SW01-2055"

# Define the delay time in between interactions
SHORT_DELAY = 1.5
LONG_DELAY = 2.5

# All asset tags in one string
asset_tags_str = """

"""

# Split the string into a list of asset tags and remove the "-"
asset_tags = [tag.replace("-", "") for tag in asset_tags_str.split()]

# Iterate over the list of asset tags
for i, asset_tag in enumerate(asset_tags):
    # Display the current asset tag number and total count
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

    # Clear the primary user field
    print("  Clearing the primary user field")
    pyautogui.click(**primary_user)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    time.sleep(SHORT_DELAY)

    # Clear the station ID field
    print("  Clearing the station ID field")
    pyautogui.click(**station_ID)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    time.sleep(SHORT_DELAY)

    # Update the inventory date field to today's date
    print("  Updating the inventory date field")
    pyautogui.click(**inventory_date_field)
    time.sleep(SHORT_DELAY)
    pyautogui.click(**today_date)
    time.sleep(SHORT_DELAY)

    # Click on the decommision button
    print("  Clicking on the decommision button")
    pyautogui.click(**decommision_button)
    time.sleep(LONG_DELAY)

    # Click on the back button to return to the search page
    print("  Clicking on the back button")
    pyautogui.click(**back_button)
    time.sleep(SHORT_DELAY)

    # Display a message indicating the completion of the current asset tag
    print(f"Completed asset tag {i + 1}/{len(asset_tags)}: {asset_tag}\n")

# Display a message indicating the completion of all asset tags
print("All asset tags completed")
