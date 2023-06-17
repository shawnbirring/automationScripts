import pyautogui
import time

"""
========================================================
CHERWELL INVENTORY AUTOMATION SCRIPT
========================================================

The script carries out the following steps for each asset tag:

1. It logs the number of the current asset tag being processed.
2. It clicks on the search bar.
3. It selects any existing text in the search bar and deletes it.
4. It types in the asset tag and presses Enter to search for the asset.
5. It waits for the search results to appear.
6. It clicks on the first search result.
7. It clicks on the location field, selects any existing text, deletes it, and types in the new location.
8. It clicks on the inventory date field, and then selects today's date.
9. It scrolls down.
10. It clicks on the save button.
11. It clicks on the back button to return to the search page.
12. It waits for it to go back to the search page before starting the next asset tag.

"""

back_button = {"x": 28, "y": 59}
search_bar = {"x": 185, "y": 229}
first_search_result = {"x": 267, "y": 344}
save_button = {"x": 920, "y": 995}
location_field = {"x": 886, "y": 418}
inventory_date_field = {"x": 741, "y": 721}
today_date = {"x": 677, "y": 885}
scroll_location = {"x": 1500, "y": 650}

# Amount of scrolling needed for save button
SCROLL_AMOUNT = 350

# Define the new location of the asset
newLocation = ""

# Define the delay time in between interactions
SHORT_DELAY = 2
LONG_DELAY = 3

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
    time.sleep(LONG_DELAY)

    # Double click on the first search result
    print("  Clicking on the first search result")
    pyautogui.click(**first_search_result)
    pyautogui.click(**first_search_result)
    time.sleep(LONG_DELAY)

    # Scroll up to the top of the page, move the mouse to 50, 50 and then scroll
    print("  Scrolling up to the top of the page")
    pyautogui.moveTo(**scroll_location)
    pyautogui.scroll(SCROLL_AMOUNT)

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

    # Scroll down to the save button
    print("  Scrolling down to the save button")
    pyautogui.moveTo(**scroll_location)
    pyautogui.scroll(-SCROLL_AMOUNT)
    print("  Clicking on the save button")
    pyautogui.click(**save_button)
    time.sleep(LONG_DELAY)

    print("  Clicking on the back button")
    pyautogui.click(**back_button)
    time.sleep(LONG_DELAY)

    print(f"Completed asset tag {i + 1}/{len(asset_tags)}: {asset_tag}\n")

print("All asset tags completed")
