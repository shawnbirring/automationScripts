import pyautogui
import time

# Define the coordinates
back_button = {"x": 28, "y": 59}
search_bar = {"x": 185, "y": 229}
primary_user = {"x": 655, "y": 492}
first_search_result = {"x": 267, "y": 344}
inventory_date_field = {"x": 741, "y": 721}
today_date = {"x": 677, "y": 885}
decommision_button = {"x": 123, "y": 250}


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
    time.sleep(DELAY_TIME)

    print("  Clicking on the first search result")
    pyautogui.click(**first_search_result)
    pyautogui.click(**first_search_result)
    time.sleep(DELAY_TIME)

    print("  Clicking on the primary user, selecting any text, deleting it")
    pyautogui.click(**primary_user)
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
    time.sleep(DELAY_TIME)

    print("  Clicking on the decommision button")
    pyautogui.click(**decommision_button)
    time.sleep(DELAY_TIME)

    print("  Clicking on the back button")
    pyautogui.click(**back_button)
    time.sleep(DELAY_TIME)

    print("  Waiting for it to go back to the search page")
    time.sleep(DELAY_TIME)

    print(f"Completed asset tag {asset_tag}\n")

print("All asset tags completed")
