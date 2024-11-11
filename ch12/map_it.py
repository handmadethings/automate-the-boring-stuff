#! python3
# map_it.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get adress from the command line.
    address = ' '.join(sys.arv[1:])
else:
    # Get address from the clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)