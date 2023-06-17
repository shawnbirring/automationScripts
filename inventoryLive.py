import pyautogui
import time

back_button = {"x": 28, "y": 59}
search_bar = {"x": 185, "y": 229}
first_search_result = {"x": 267, "y": 344}
save_button = {"x": 920, "y": 995}
location_field = {"x": 886, "y": 418}
inventory_date_field = {"x": 741, "y": 721}
today_date = {"x": 677, "y": 885}
scroll_location = {"x": 1500, "y": 650}

SCROLL_AMOUNT = 350
newLocation = ""
SHORT_DELAY = 0
LONG_DELAY = 0

# Run indefinitely until manually stopped
while True:

    asset_tag = input("Please enter the asset tag or type 'exit' to stop the program: ")
    
    if asset_tag.lower() == 'exit':
        break

    asset_tag = asset_tag.replace("-", "")

    print(f"Processing asset tag: {asset_tag}")

    print("  Clicking on the search bar")
    pyautogui.click(**search_bar)

    print("  Selecting any existing text and deleting it")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")

    print(f"  Typing the asset tag {asset_tag} and pressing Enter to search")
    pyautogui.write(asset_tag)
    pyautogui.press("enter")
    print("  Waiting for search results")
    time.sleep(LONG_DELAY)

    print("  Clicking on the first search result")
    pyautogui.click(**first_search_result)
    pyautogui.click(**first_search_result)
    time.sleep(LONG_DELAY)

    print("  Scrolling up to the top of the page")
    pyautogui.moveTo(**scroll_location)
    pyautogui.scroll(SCROLL_AMOUNT)

    print("  Updating the location field")
    pyautogui.click(**location_field)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    pyautogui.write(newLocation)
    time.sleep(SHORT_DELAY)

    print("  Updating the inventory date field")
    pyautogui.click(**inventory_date_field)
    time.sleep(SHORT_DELAY)
    pyautogui.click(**today_date)
    time.sleep(SHORT_DELAY)

    print("  Scrolling down to the save button")
    pyautogui.moveTo(**scroll_location)
    pyautogui.scroll(-SCROLL_AMOUNT)
    print("  Clicking on the save button")
    pyautogui.click(**save_button)
    time.sleep(LONG_DELAY)

    print("  Clicking on the back button")
    pyautogui.click(**back_button)
    time.sleep(LONG_DELAY)

    print(f"Completed asset tag: {asset_tag}\n")
