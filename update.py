import pyautogui
import time

"""
========================================================
CHERWELL AUTOMATION SCRIPT
========================================================

The script carries out the following steps for each asset tag:

1. It clicks on the search bar.
2. It selects any existing text in the search bar and deletes it.
3. It types in the asset tag and presses Enter to search for the asset.
4. It waits for the search results to appear.
5. It clicks on the first search result.
6. It clicks on the location field, selects any existing text, deletes it, and types in the new location.
7. It clicks on the station ID field, selects any text, and deletes it.
8. It clicks on the inventory date field, selects any date, and then selects today's date.
9. It clicks on the decommision button.
10. It clicks on the back button to return to the search page.
11. It waits for it to go back to the search page before starting the next asset tag.

To run the script:

1. Make sure Python is installed on your computer. If not, you can download Python from https://www.python.org/downloads/.
2. Download and install Visual Studio Code from https://code.visualstudio.com/download. After installing, add the Python extension to Visual Studio Code.
3. Open Visual Studio Code, and paste this script into a new file.
4. Replace the asset_tags_str with the asset tags you want to update. Make sure each asset tag is in a new line and enclosed with triple quotes.
5. Save the file with a .py extension.
6. Ensure the x and y coordinates of the buttons are correct with your machine.
7. Press on the run icon at the top right of vs code to execute the script.


IMPORTANT: 

- To stop the script from running while it is, move your mouse to the top left of the screen.
- Do not use your computer while the script is running, as it controls your mouse and keyboard. 
- The coordinates used in this script might not match the exact location of the buttons on your screen. You need to adjust the x and y values accordingly.
- Make sure Cherwell is open in the search page and in full screen and visible on your screen before running the script.

"""

# Define the coordinates
back_button = {"x": 28, "y": 59}
search_bar = {"x": 185, "y": 229}
first_search_result = {"x": 267, "y": 344}
location_field = {"x": 886, "y": 418}
station_ID = {"x": 387, "y": 418}
inventory_date_field = {"x": 700, "y": 800}
today_date = {"x": 735, "y": 715}
decommision_button = {"x": 123, "y": 250}

# Define the new location of the asset
newLocation = "BBY-SW01-2055"

# Define the delay time in between interactions
DELAY_TIME = 3

# All asset tags in one string
asset_tags_str = """

"""

# Split the string into a list of asset tags and remove the "-"
asset_tags = [tag.replace("-", "") for tag in asset_tags_str.split()]

for asset_tag in asset_tags:
    print(f"Starting asset tag {asset_tag}")

    print("  Clicking on the search bar")
    pyautogui.click(**search_bar)
    time.sleep(DELAY_TIME)

    print("  Selecting any existing text and deleting it")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    time.sleep(DELAY_TIME)

    print(f"  Typing the asset tag {asset_tag} and pressing Enter to search")
    pyautogui.write(asset_tag)
    pyautogui.press("enter")
    time.sleep(DELAY_TIME)

    print("  Waiting for search results")
    time.sleep(5)

    print("  Clicking on the first search result")
    pyautogui.click(**first_search_result)
    time.sleep(DELAY_TIME)

    print(
        "  Clicking on the location field, selecting any existing text, deleting it, and typing the new location"
    )
    pyautogui.click(**location_field)
    time.sleep(DELAY_TIME)

    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    time.sleep(DELAY_TIME)

    pyautogui.write(newLocation)
    time.sleep(DELAY_TIME)

    print("  Clicking on the station ID, selecting any text, deleting it")
    pyautogui.click(**station_ID)
    time.sleep(DELAY_TIME)

    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    time.sleep(DELAY_TIME)

    print(
        "  Clicking on the inventory date field, selecting any date and selecting today"
    )
    pyautogui.click(**inventory_date_field)
    time.sleep(DELAY_TIME)

    pyautogui.click(**today_date)
    time.sleep(DELAY_TIME)

    print("  Clicking on the decommision button")
    pyautogui.click(**decommision_button)
    time.sleep(3)

    print("  Clicking on the back button")
    pyautogui.click(**back_button)
    time.sleep(DELAY_TIME)

    print("  Waiting for it to go back to the search page")
    time.sleep(DELAY_TIME)

    print(f"Completed asset tag {asset_tag}\n")

print("All asset tags completed")
