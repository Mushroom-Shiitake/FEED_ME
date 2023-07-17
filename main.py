import os
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename


def clear(): #Clears the console
    os.system('clear')

def welcomeScreen(): #A simple welcomescreen
    clear()
    welcome = 20
    while welcome > 0:
        print('Hello my friend!')
        time.sleep(0.1)
        welcome -= 1
    selectFile()

def selectFile(): #Let the user select a file to be feed
    clear()
    print("Select your file...")
    time.sleep(2)
    Tk().withdraw()
    filePath = askopenfilename()
    getFileSize(filePath)

def getFileSize(file = None): #Gets the file size with the os.path.getsize function.
    if file == None:
        print("Please select a file.")
    else:
        pass

    try:
        fileSize = os.path.getsize(file)
        return fileSize
    except:
        print("An error occurred (Code: 1)")

def FEED_ME(file): #Will make the file bigger with junk
    pass

welcomeScreen()
selectFile()

