# DailyWriterTools
Python tools for writing

- open program
- start writing
- auto saving
- word count output on write
- end file
- creates a text copy of days writing
- creates a text copy of all combined writing
- tells you what files are included
- tells you how many words total

##Currently
- This will run with 'python autoWrite.py' in Terminal
- vim commands rule the day: i to insert, :w to write, and :q to quit, are the basics. type help or something like that. 
- to append to the days writing after the application has already run once, type 'python autoWrite.py' again, then 'shift + g' and then 'shift + a', instead of scrolling to the bottom this will take you there and press 'insert' for you.
- Prints day's total word count
- Prints month's total word count
- Compiles all month's words in single file for you

##Does Not
- Opens text files of what you have written, for the day and for the month, for copying
- Catch any errors: not sure what would happen if there were other files in directory
- Cypher words so the text is unreadable to most people with computer help
- Upload to 750 and NaNoWriMo at EOD or on demand
- Format writing for clean paragraphs and sentence endings 
- Accomodate markdown
- check spelling
- count typing speed


##Problems
- Determine why gedit can't open allWords file
- Word counter is probably inaccurate, has not been tested
- - Design a unit test
- - Think about hyphenated words and how to handle nested punctuation
- Not sure how to read live typing into active python process while maintaining user experience
- - Possibly the readline module can help with this
- - Might involve implementing a gui with qt or tinker

##Solved
- Determine why gedit can't open allWords file
 -- This was because the allWords file was being saved as a giant list of all the letters, not a string of all the lines combined. Currently it seems to work, printing pretty much as it's read/written by user

write one file, rewrites two new files and gives you word counts
