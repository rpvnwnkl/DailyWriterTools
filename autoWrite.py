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

if dirPath not in os.listdir('./'):
    ##creates new directory if the month hasn't been started yet
    os.mkdir(os.path.join(os.getcwd(), dirPath))

fileNamePath = dirPath+'/'+fileName
##establishes fileName's path based of new directory (or old)

os.system('vim '+fileNamePath)
##sends out prompt to open vim with new filename in specified path
##creates a vim environment writing prompt within the terminal 

def cleanFile(fileNamePath):
##start er up with just the
    todaysFile = open(fileNamePath, 'r')
    ##opens file as todaysFile
    todaysLines = todaysFile.read()
    ##reads file as string to todaysLines
    todaysString = todaysLines.replace('\n', ' ')
    ##remove newlines
    todaysNoPunct = todaysString.translate(None, string.punctuation)
    todaysWords = todaysNoPunct.split(' ')
    ##now we have a list of single words from the days writing
    return todaysWords

def countWords(todaysWordList):
    wordCount = 0
    realWords = []
    for word in todaysWordList:
    ##this will add up all the words which we think should qualify
        if word not in ['', ' ', '  ', '   ']:
        ##sifting out empty spaces and the like
            wordCount += 1
            realWords.append(word)
            ##adds word to a cleaned up word list, sans punctuation and spaces
        else:
            pass
    return wordCount

print 'OK, Here Is The Report:\n\n'
print str(countWords(cleanFile(fileNamePath)))+' words for the day. \n So far.... \n\n'

fileNames = []
for fileEntry in os.listdir('./'+dirPath):
    fileNames.append(fileEntry)
fileNames.sort()
##creates a list of the fileNames in the month's directory
print 'Here are the files so far in the month of '+dirPath+': \
        \n '+str(fileNames)+'\n'
    

numWords = 0
for name in fileNames:
    wordsList = cleanFile('./'+dirPath+'/'+name)
    numWords += countWords(wordsList)
print 'and '+str(numWords)+' words for the month. \n So far.......\n'
##Opens each file in fileNames list and counts the words thereh




