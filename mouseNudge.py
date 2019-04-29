#! python3.7
# mouseNudge.py - Moves the mouse slightly every 10 seconds.

import pyautogui, time

try:
    while True:
        time.sleep(10)
        pyautogui.moveRel(100, 0)
        print('Nudging...')
        time.sleep(10)
        pyautogui.moveRel(-100, 0)
        print('Nudging...')

except KeyboardInterrupt:
    print('Ended\n')