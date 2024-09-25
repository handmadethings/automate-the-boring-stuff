"# automate-the-boring-stuff" 

# Automate the Boring Stuff
#### By Al Al Sweigart

### Chapter 1 - Python Basics

### Chapter 2 - Flow Control

### Chapter 3 - Functions

### Chapter 4 - Lists

### Chapter 5 - Dictionaries and Structuring Data

### Chapter 6 - Manipulating Strings

### Chapter 7 - Pattern Matching with Regular Expressions

### Chapter 8 - Input Validation

### Chapter 9 – Reading and Writing Files

#### Correct Path
On Windows, paths are written using backslashes (\) as the separator between folder names. The macOS and Linux operating systems, however, use the forward slash (/). If you want your programs to work on all operating systems, use the Path() function in the pathlib module. If you pass it the string values of individual file and folder names in your path, Path() will return a string with a file path using the correct path separators:

<code>
from pathlib import Path
Path('spam', 'bacon', 'eggs')

WindowsPath('spam/bacon/eggs')
str(Path('spam', 'bacon', 'eggs'))
'spam\\bacon\\eggs'
</code>

Note that the convention for importing pathlib is to run *from pathlib import Path*

### Chapter 10 – Organizing Files

### Chapter 11 – Debugging

### Chapter 12 – Web Scraping

### Chapter 13 – Working with Excel Spreadsheets

### Chapter 14 – Working with Google Spreadsheets

### Chapter 15 – Working with PDF and Word Documents

### Chapter 16 – Working with CSV Files and JSON Data

### Chapter 17 – Keeping Time, Scheduling Tasks, and Launching Programs

### Chapter 18 – Sending Email and Text Messages

### Chapter 19 – Manipulating Images

### Chapter 20 – Controlling the Keyboard and Mouse with GUI Automation