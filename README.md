"# automate-the-boring-stuff" 

# Automate the Boring Stuff
#### By Al Sweigart

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

<code>\>\>\> from pathlib import Path
\>\>\> Path('spam', 'bacon', 'eggs')
WindowsPath('spam/bacon/eggs')
\>\>\> str(Path('spam', 'bacon', 'eggs'))
'spam\\bacon\\eggs'</code>

Note that the convention for importing pathlib is to run *from pathlib import Path*

#### Using the / Operator to Join Paths
The / operator that we normally use for division can also combine Path objects and strings. This is helpful for modifying a Path object after you’ve already created it with the Path() function.

For example, enter the following into the interactive shell:

<code>\>\>\> from pathlib import Path
\>\>\> Path('spam') / 'bacon' / 'eggs'
WindowsPath('spam/bacon/eggs')
\>\>\> Path('spam') / Path('bacon/eggs')
WindowsPath('spam/bacon/eggs')
\>\>\> Path('spam') / Path('bacon', 'eggs')
WindowsPath('spam/bacon/eggs')</code>

#### The Current Working Directory
You can get the current working directory as a string value with the *Path.cwd()* function and change it using *os.chdir()*:

<code>\>\>\> from pathlib import Path
\>\>\> import os
\>\>\> Path.cwd()
WindowsPath('C:/Users/Al/AppData/Local/Programs/Python/Python37')'
\>\>\> os.chdir('C:\\Windows\\System32')
\>\>\> Path.cwd()
WindowsPath('C:/Windows/System32')</code>

The *os.getcwd()* function is the older way of getting the current working directory as a string.

#### The Home Directory
All users have a folder for their own files on the computer called the home directory or home folder. You can get a Path object of the home folder by calling Path.home():

<code>\>\>\> Path.home()
WindowsPath('C:/Users/Al')</code>

Your scripts will almost certainly have permissions to read and write the files under your home directory, so it’s an ideal place to put the files that your Python programs will work with.
There are also the dot (.) and dot-dot (..) folders. These are not real folders but special names that can be used in a path. A single period (“dot”) for a folder name is shorthand for “this directory.” Two periods (“dot-dot”) means “the parent folder.”

#### Absolute vs. Relative Paths
There are two ways to specify a file path:

* An absolute path, which always begins with the root folder
* A relative path, which is relative to the program’s current working directory

There are also the dot (.) and dot-dot (..) folders. These are not real folders but special names that can be used in a path. A single period (“dot”) for a folder name is shorthand for “this directory.” Two periods (“dot-dot”) means “the parent folder.”

#### Creating New Folders Using the os.makedirs() Function
Your programs can create new folders (directories) with the *os.makedirs()* function:

<code>\>\>\> import os
\>\>\> os.makedirs('C:\\delicious\\walnut\\waffles')</code>

To make a directory from a Path object, call the mkdir() method. For example, this code will create a spam folder under the home folder on my computer:

<code>\>\>\> from pathlib import Path
\>\>\> Path(r'C:\Users\Al\spam').mkdir()</code>

#### Getting the Parts of a File Path
Given a Path object, you can extract the file path’s different parts as strings using several Path object attributes. These can be useful for constructing new file paths based on existing ones.

<code>\>\>\> p = Path('C:/Users/Al/spam.txt')
\>\>\> p.anchor
'C:\\'
\>\>\> p.parent # This is a Path object, not a string.
WindowsPath('C:/Users/Al')
\>\>\> p.name
'spam.txt'
\>\>\> p.stem
'spam'
\>\>\> p.suffix
'.txt'
\>\>\> p.drive
'C:'</code>

These attributes evaluate to simple string values, except for parent, which evaluates to another Path object.

If you need a path’s dir name and base name together, you can just call os.path.split() to get a tuple value with these two strings, like so:

<code>\>\>\> calcFilePath = 'C:\\Windows\\System32\\calc.exe'
\>\>\> os.path.split(calcFilePath)
('C:\\Windows\\System32', 'calc.exe')</code>

#### Checking Path Validity
Many Python functions will crash with an error if you supply them with a path that does not exist. Luckily, Path objects have methods to check whether a given path exists and whether it is a file or folder. Assuming that a variable p holds a Path object, you could expect the following:

* Calling *p.exists()* returns True if the path exists or returns False if it doesn’t exist.
* Calling *p.is_file()* returns True if the path exists and is a file, or returns False otherwise.
* Calling *p.is_dir()* returns True if the path exists and is a directory, or returns False otherwise.

#### Opening and Reading Files
To open a file with the open() function, you pass it a string path indicating the file you want to open; it can be either an absolute or relative path. The open() function returns a File object. 

<code>\>\>\> helloFile = open(Path.home() / 'hello.txt')
\>\>\> helloContent = helloFile.read()
\>\>\> helloContent
'Hello, world!'</code>

Alternatively, you can use the readlines() method to get a list of string values from the file, one string for each line of text.

<code>\>\>\> sonnetFile = open(Path.home() / 'sonnet29.txt')
\>\>\> sonnetFile.readlines()</code>

**Good practice:** Use the with statement to automatically call close() when the execution leaves the with statement’s block.

<code>\>\>\> with open(Path.home() / 'hello.txt', 'w') as fileObj:
...     fileObj.write('Hello, world!')</code>

#### Writing to Files

Python allows you to write content to a file in a way similar to how the print() function “writes” strings to the screen. Popen the file in write mode and append mode.

Write mode will overwrite the existing file and start from scratch, just like when you overwrite a variable’s value with a new value. Pass 'w' as the second argument to open() to open the file in write mode. Append mode, on the other hand, will append text to the end of the existing file. You can think of this as appending to a list in a variable, rather than overwriting the variable altogether. Pass 'a' as the second argument to open() to open the file in append mode.

<code>\>\>\> baconFile = open('bacon.txt', 'w')   
\>\>\> baconFile.write('Hello, world!\n')
13
\>\>\> baconFile.close()
\>\>\> baconFile = open('bacon.txt', 'a')
\>\>\> baconFile.write('Bacon is not a vegetable.')
25
\>\>\> baconFile.close()
\>\>\> baconFile = open('bacon.txt')
\>\>\> content = baconFile.read()
\>\>\> baconFile.close()
\>\>\> print(content)
Hello, world!
Bacon is not a vegetable.</code>

#### Saving Variables with the shelve Module
You can save variables in your Python programs to binary shelf files using the shelve module. This way, your program can restore data to variables from the hard drive. The shelve module will let you add Save and Open features to your program. For example, if you ran a program and entered some configuration settings, you could save those settings to a shelf file and then have the program load them the next time it is run.

Enter the following into the interactive shell:

<code>\>\>\> import shelve
\>\>\> shelfFile = shelve.open('mydata')
\>\>\> cats = ['Zophie', 'Pooka', 'Simon']
\>\>\> shelfFile['cats'] = cats
\>\>\> shelfFile.close()</code>

Your programs can use the shelve module to later reopen and retrieve the data from these shelf files. Shelf values don’t have to be opened in read or write mode—they can do both once opened. Enter the following into the interactive shell:

<code>\>\>\> shelfFile = shelve.open('mydata')
\>\>\> shelfFile['cats']
['Zophie', 'Pooka', 'Simon']
\>\>\> shelfFile.close()</code>

#### Saving Variables with the pprint.pformat() Function
Say you have a dictionary stored in a variable and you want to save this variable and its contents for future use. Using pprint.pformat() will give you a string that you can write to a .py file. This file will be your very own module that you can import whenever you want to use the variable stored in it.

For example, enter the following into the interactive shell:

<code>\>\>\> import pprint
\>\>\> cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
\>\>\> pprint.pformat(cats)
"[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"
\>\>\> fileObj = open('myCats.py', 'w')
\>\>\> fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
83
\>\>\> fileObj.close()</code>

The benefit of creating a .py file (as opposed to saving variables with the shelve module) is that because it is a text file, the contents of the file can be read and modified by anyone with a simple text editor. For most applications, however, saving data using the shelve module is the preferred way to save variables to a file.

### Chapter 10 – Organizing Files

#### The shutil Module
The shutil (or shell utilities) module has functions to let you copy, move, rename, and delete files in your Python programs.

Calling shutil.copy(source, destination) will copy the file at the path source to the folder at the path destination. (Both source and destination can be strings or Path objects.) If destination is a filename, it will be used as the new name of the copied file.

Calling shutil.move(source, destination) will move the file or folder at the path source to the path destination and will return a string of the absolute path of the new location.

#### Permanently Deleting Files and Folders
You can delete a single file or a single empty folder with functions in the os module, whereas to delete a folder and all of its contents, you use the shutil module.

* Calling os.unlink(path) will delete the file at path.
* Calling os.rmdir(path) will delete the folder at path. This folder must be empty of any files or folders.
* Calling shutil.rmtree(path) will remove the folder at path, and all files and folders it contains will also be deleted.

#### Safe Deletes with the send2trash Module
Since Python’s built-in shutil.rmtree() function irreversibly deletes files and folders, it can be dangerous to use. A much better way to delete files and folders is with the third-party send2trash module.

#### Walking a Directory Tree
Say you want to rename every file in some folder and also every file in every subfolder of that folder. That is, you want to walk through the directory tree, touching each file as you go. Python provides a function to handle this process for you, *the os.walk()* function.

### Chapter 11 – Debugging

#### Raising Exceptions
Often it’s the code that calls the function, rather than the function itself, that knows how to handle an exception. That means you will commonly see a raise statement inside a function and the try and except statements in the code calling the function.

#### Assertions
An assertion is a sanity check to make sure your code isn’t doing something obviously wrong. These sanity checks are performed by assert statements. If the sanity check fails, then an AssertionError exception is raised.
Unlike exceptions, your code should not handle assert statements with try and except; if an assert fails, your program should crash. By “failing fast” like this, you shorten the time between the original cause of the bug and when you first notice the bug.

Assertions are for programmer errors, not user errors. Assertions should only fail while the program is under development; a user should never see an assertion error in a finished program. For errors that your program can run into as a normal part of its operation (such as a file not being found or the user entering invalid data), raise an exception instead of detecting it with an assert statement.

#### Logging
To enable the logging module to display log messages on your screen as your program runs, copy the following to the top of your program:

<code>import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)
s -  %(message)s')</code>

##### Don’t Debug with the print() Function
You may want to use print() calls instead, but don’t give in to this temptation! The nice thing about log messages is that you’re free to fill your program with as many as you like, and you can always disable them later by adding a single logging.disable(logging.CRITICAL) call. Unlike print(), the logging module makes it easy to switch between showing and hiding log messages.

##### Disabling Logging
After you’ve debugged your program, you probably don’t want all these log messages cluttering the screen. The logging.disable() function disables these so that you don’t have to go into your program and remove all the logging calls by hand. You simply pass logging.disable() a logging level, and it will suppress all log messages at that level or lower. So if you want to disable logging entirely, just add logging.disable(logging.CRITICAL)

Since logging.disable() will disable all messages after it, you will probably want to add it near the import logging line of code in your program. This way, you can easily find it to comment out or uncomment that call to enable or disable logging messages as needed.

##### Logging to a File
Instead of displaying the log messages to the screen, you can write them to a text file. The logging.basicConfig() function takes a filename keyword argument, like so:

<code>import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='
%(asctime)s -  %(levelname)s -  %(message)s')</code>

### Chapter 12 – Web Scraping

### Chapter 13 – Working with Excel Spreadsheets
The [openpyxl](https://openpyxl.readthedocs.io/en/stable/) module allows your Python programs to read and modify Excel (and LibreOffice Calc and OpenOffice Calc) spreadsheet files.

### Chapter 14 – Working with Google Spreadsheets

### Chapter 15 – Working with PDF and Word Documents
There are Python modules that make it easy for you to interact with PDFs and Word documents. Two such modules are [PyPDF2](https://pypdf2.readthedocs.io/en/3.x/) and [Python-Docx](https://python-docx.readthedocs.io/en/latest/).

#### Creating PDF:s
The PyPDF2 module doesn’t allow you to create PDF documents directly, but there’s a way to generate PDF files with Python if you’re on Windows and have Microsoft Word installed with the Pywin32 package. With this and the docx module, you can create Word documents and then convert them to PDFs.

### Chapter 16 – Working with CSV Files and JSON Data
#### Reading CSV Files
To read data from a CSV file with the csv module, you need to create a reader object. A reader object lets you iterate over lines in the CSV file.

<code>\>\>\> import csv
\>\>\> exampleFile = open('example.csv')
\>\>\> exampleReader = csv.reader(exampleFile)
\>\>\> exampleData = list(exampleReader)
\>\>\> exampleData</code>

Now that you have the CSV file as a list of lists, you can access the value at a particular row and column with the expression <code>exampleData[row][col]</code>

For large CSV files, you’ll want to use the reader object in a for loop:

<code>\>\>\> for row in exampleReader:
        print('Row #' + str(exampleReader.line_num) + ' ' + str(row))</code>

#### Writing CSV Files
A writer object lets you write data to a CSV file:

<code>\>\>\> import csv
\>\>\> outputFile = open('output.csv', 'w', newline='')
\>\>\> outputWriter = csv.writer(outputFile)
\>\>\> outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])</code>

#### DictReader and DictWriter CSV Objects
For CSV files that contain header rows, it’s often more convenient to work with the *DictReader* and *DictWriter* objects, rather than the *reader* and *writer* objects. These perform the same functions but use dictionaries instead, and they use the first row of the CSV file as the keys of these dictionaries.

<code>\>\>\> import csv
\>\>\> exampleFile = open('exampleWithHeader.csv')
\>\>\> exampleDictReader = csv.DictReader(exampleFile)
\>\>\> for row in exampleDictReader:
...     print(row['Timestamp'], row['Fruit'], row['Quantity'])</code>

### Chapter 17 – Keeping Time, Scheduling Tasks, and Launching Programs

### Chapter 18 – Sending Email and Text Messages

### Chapter 19 – Manipulating Images

### Chapter 20 – Controlling the Keyboard and Mouse with GUI Automation