# gesture control python program for controlling certain functions in windows pc
# Code by Harsh Namdev


# add pyautogui library for programmatically controlling the mouse and keyboard.
import pyautogui
import time
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second
# winsound.Beep(frequency, duration)

def action_func(incoming_data):

    # print the incoming data
    print('handy', incoming_data)

    if '0' in incoming_data:        # minimizing window
        # pyautogui.hotkey('winleft', 'down')
        # time.sleep(1)
        pass

    if '1' in incoming_data:                    # if incoming data is 'next'
        # perform "ctrl+pgdn" operation which moves to the next tab
        pyautogui.hotkey('ctrl', 'pgdn')
        time.sleep(1)

    if '2' in incoming_data:                # if incoming data is 'previous'
        # perform "ctrl+pgup" operation which moves to the previous tab
        pyautogui.hotkey('ctrl', 'pgup')
        time.sleep(1)

    if '3' in incoming_data:                    # if incoming data is 'down'
        # pyautogui.press('down')                   # performs "down arrow" operation which scrolls down the page
        pyautogui.scroll(-100)

    if '4' in incoming_data:                      # if incoming data is 'up'
        # pyautogui.press('up')                      # performs "up arrow" operation which scrolls up the page
        pyautogui.scroll(100)

    if '5' in incoming_data:                  # if incoming data is 'change'
        # performs "alt+tab" operation which switches the tab
        # pyautogui.keyDown('alt')
        # pyautogui.press('space')
        # pyautogui.keyUp('alt')
        pyautogui.hotkey('winleft', 'down')   # maximizing window
        time.sleep(1)

    if 'zoomin' in incoming_data:
        pyautogui.hotkey('ctrl', '+')
        # time.sleep(1)

    if 'zoomout' in incoming_data:
        pyautogui.hotkey('ctrl', '-')
        # time.sleep(1)

    if 'terminal' in incoming_data:
        pyautogui.hotkey('winleft','r')
        pyautogui.press('enter')

    if 'closetab' in incoming_data:
        pyautogui.hotkey('ctrl','w')
        # pyautogui.press('enter')
    
    if 'opentab' in incoming_data:
        pyautogui.hotkey('ctrl','t')
        # pyautogui.press('enter')
    
    if 'closewindow' in incoming_data:
        pyautogui.hotkey('alt','f4')

    if 'screenshot' in incoming_data:
        # pyautogui.hotkey('winleft','')
        pyautogui.screenshot(r"F:\[[[[final_project\screenshots\screenshot.png")
        winsound.Beep(frequency, duration)

    
    incoming_data = ""                            # clears the data
