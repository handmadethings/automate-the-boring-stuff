#! python3
# mclip.py - A multi-clipboard program.
'''On Windows, you can create a batch file to run this program with the 
WIN-R Run window. (For more about batch files, see Appendix B.) Enter
the following into the file editor and save the file as mclip.bat in the 
C:\Windows folder:

@py.exe C:\path_to_file\mclip.py %*
@pause

With this batch file created, running the multi-clipboard program on Windows
 is just a matter of pressing WIN-R and typing mclip key phrase.
'''

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyyphrase = sys.argv[1] # First command line arg is the keyphrase

if keyyphrase in TEXT:
    pyperclip.copy(TEXT[keyyphrase])
    print('Text for ' + keyyphrase + ' copied to clipboard')
else:
    print('There is no text for ' + keyyphrase)