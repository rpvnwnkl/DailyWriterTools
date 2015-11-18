#!/usr/bin/env python

import os
import time
import string

rightNow = time.localtime()
##reads local time as structured format
fileName = time.strftime('%d%a', rightNow)
##converts rightNow time to NumberDay, in format like '17Tue'

dirPath = time.strftime('%B%Y', rightNow)
##sets directory name based off date

if dirPath not in os.listdir(os.getcwd()):
    ##creates new directory if the month hasn't been started yet
    os.mkdir(os.path.join(os.getcwd(), dirPath))

fileNamePath = dirPath+'/'+fileName
##establishes fileName's path based of new directory (or old)

os.system('vim '+fileNamePath)
##sends out prompt to open vim with new filename in specified path
##creates a vim environment writing prompt within the terminal 

todaysFile = open(fileNamePath, 'r')
##opens file as todaysFile
todaysLines = todaysFile.read()
##reads file as string to todaysLines
todaysString = todaysLines.replace('\n', ' ')
##remove newlines
todaysNoPunct = todaysString.translate(None, string.punctuation)
todaysWords = todaysNoPunct.split(' ')
##now we have a list of single words from the days writing

wordCount = 0
realWords = []
for word in todaysWords:
    ##this will add up all the words which we think should qualify
    if word not in ['', ' ', '  ', '   ']:
        ##sifting out empty spaces and the like
        wordCount += 1
        realWords.append(word)
        ##adds word to a cleaned up word list, sans punctuation and spaces
    else:
       pass

print str(wordCount)+' words for the day. \n So far.... '
    






