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


def selectFile(): #Let the user select a file to be feed
    clear()
    print("Select your file...")
    time.sleep(2)
    Tk().withdraw()
    global filePath
    filePath = askopenfilename()
    return filePath


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


def setSize():
    clear()
    print(f'Your file is  big...\nWhat size should it be?')#TODO: Set Variable
    global wishSize
    wishSize = input('Size (GB, MB, KB, B): ')
    wishSize = wishSize.replace(' ', '') #Delets all spaces from userinput
    print(wishSize)
    return wishSize


def FEED_ME(file = None, wishSize = None): #Will make the file bigger with junk (zeroes)
    while getFileSize(file) != wishSize:
        feedFile = open(file, "ab")
        feedFile.write(b'\x00')

if __name__ == "__main__":
    welcomeScreen()

    filePath = selectFile()
    fileSize = getFileSize(filePath)
    wishSize = setSize()
    wishSize = int(wishSize)
    FEED_ME(filePath, wishSize)