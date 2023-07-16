import os
import time


file = None


def clear():
    os.system('clear')

def welcomeScreen():
    clear()
    welcome = 20
    while welcome > 0:
        print('Hello my friend!')
        time.sleep(0.1)
        welcome -= 1

def selectFile():
    pass

def getFileSize(file = None):
    #fileSize = os.path.getsize(file)
    #return fileSize
    pass

def FEED_ME(file):
    pass

welcomeScreen()