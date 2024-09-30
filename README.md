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

<code>from pathlib import Path
Path('spam', 'bacon', 'eggs')</code>

Note that the convention for importing pathlib is to run *from pathlib import Path*

#### Using the / Operator to Join Paths
The / operator that we normally use for division can also combine Path objects and strings. This is helpful for modifying a Path object after you’ve already created it with the Path() function.

For example, enter the following into the interactive shell:

<code>
> from pathlib import Path
> Path('spam') / 'bacon' / 'eggs'
WindowsPath('spam/bacon/eggs')
> Path('spam') / Path('bacon/eggs')
WindowsPath('spam/bacon/eggs')
> Path('spam') / Path('bacon', 'eggs')
WindowsPath('spam/bacon/eggs')</code>

#### The Current Working Directory
You can get the current working directory as a string value with the *Path.cwd()* function and change it using *os.chdir()*:

<code>>from pathlib import Path
> import os
> Path.cwd()
WindowsPath('C:/Users/Al/AppData/Local/Programs/Python/Python37')'
>os.chdir('C:\\Windows\\System32')
>Path.cwd()
WindowsPath('C:/Windows/System32')</code>

#### The Home Directory
All users have a folder for their own files on the computer called the home directory or home folder. You can get a Path object of the home folder by calling Path.home():

<code>Path.home()
WindowsPath('C:/Users/Al')</code>

Your scripts will almost certainly have permissions to read and write the files under your home directory, so it’s an ideal place to put the files that your Python programs will work with.
There are also the dot (.) and dot-dot (..) folders. These are not real folders but special names that can be used in a path. A single period (“dot”) for a folder name is shorthand for “this directory.” Two periods (“dot-dot”) means “the parent folder.”

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