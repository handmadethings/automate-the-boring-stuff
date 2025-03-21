import time, pyautogui

print('Unidler activated, press CTRL-C or move mouse to a corner window to quit.')
try:
    while True:
        pyautogui.move(10, 0, 0.5)
        pyautogui.move(-10, 0, 0.5)
        time.sleep(10)
except KeyboardInterrupt:
    print('Unidler deactivated.')