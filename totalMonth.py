#!/usr/bin/env python
import os


def readfile():
    allWords = ''
    totalWords = 0
    print totalWords
    for root, dirnames, files in os.walk('./'): 
        print files
        allSentences = []
        allWords = ''
        totalWords = 0
        totalChars = 0
        fileNames = []
        for name in files:
            fileNames.append(name)
        fileNames.sort()
        for name in fileNames:
            with open(os.path.join(root, name), 'rb') as dayText:
                allWords += dayText.read()
                sentenceList = [sentence.strip() for sentence in allWords.split('.')]
                allSentences = sentenceList
        for sentence in allSentences:
            wordList = sentence.split(' ')
            print len(wordList)
            for word in wordList:
                print word
                if word != ' ':
                    totalWords += 1
                    totalChars += len(word)
        print 'allWords:'
        print allWords
        ##print 'allSentences: '
        ##print allSentences
        print 'totalWords: '
        print totalWords
        print fileNames


readfile()

def countWords():
    totalSum = 0
    for x in readfile:
        totalSum += 0 
    for item in tmpList:
        item = item
    return tmpList

