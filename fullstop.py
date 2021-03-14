import os
# A program corrects the grammar in a line of text. The text is read in from a text file.
#
# The procedure, fullStop, needs to:
#  • ask for a file name as input
#  • read the data from the file using the function getText
#  • replace the first letter after each full stop with a capital letter if it is currently
#    lower case (if the next character is a space, it must check each successive character until
#    it finds a letter)
#  • write the edited data back to the text file.
#
# You can assume the text file only contains upper and lower case letters, spaces and full stops.
#
# Part of the ASCII table has been provided:
#      +----------------+----------------+
#      | ASCII Value    | Character      |
#      +----------------+----------------+
#      | 65             | "A"            |
#      +----------------+----------------+
#      | 90             | "Z"            |
#      +----------------+----------------+
#      | 122            | "a"            |
#      +----------------+----------------+
#      | 32             | " " (space)    |
#      +----------------+----------------+
#      | 46             | "." (full stop)|
#      +----------------+----------------+
#
# The following functions may be used in your answer:
# asc(character) returns the ASCII value for a single character, e.g. asc("A") would return 65.
# upper(character) returns the single character in upper case, e.g. upper("a") would return “A”.
# Write the procedure fullStop.
# (7 marks)

def asc(char):
    return ord(char[0])

def upper(char):
    return char[0].upper()        

def fullStop(FileName):
    myFile = open(FileName, "r")
    fileLines = myFile.read()
    new = ""
    dot = False
    for i in range(len(fileLines)):
        
        if asc(fileLines[i]) == 46:
            dot = True 
        if asc(fileLines[i]) < 65 and dot == True:
            new += fileLines[i]
        elif asc(fileLines[i]) >= 65 and dot == True:
            new += upper(fileLines[i])
            dot = False
        else:
            new += fileLines[i]

    print(new)
    print(fileLines)
    myFile.close()

            
fullStop("FullStop.txt")
#print(count)