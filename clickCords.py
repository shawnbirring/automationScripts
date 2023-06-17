from pynput.mouse import Listener, Button

# this file prints out the coordinates whenever you click your mouse, click at 0,0 to terminate

def on_click(x, y, button, pressed):
    if pressed and button == Button.left:
        print('{{"x": {}, "y": {}}}'.format(x, y))
        if x == 0 and y == 0:  
            return False  # This stops the listener

with Listener(on_click=on_click) as listener:
    listener.join()
