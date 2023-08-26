from math import *
import pyperclip
import urllib3

while True:
    filePath = input("Please enter the file path of your aliases file: " )
    try:
        file = open(filePath, "r")
        break
    except:
        print("File not found, try again!")
# c:\My Files\PBCCAliases.txt

theAlias = ""
partsToAdd = []
writeToFile = []

i = 0
f = open("aliases.txt", "w")
f.write("")
f.close()

f = open("aliases.txt", "a")
for line in file:
    findAlias = line.find("!importalias")
    
    if "!importalias" in line:
        i = i + 1

        appendThis = line[findAlias + 1:].rstrip("\n")
        finallyAppend = "!" + appendThis
        partsToAdd.append(finallyAppend)

        if i % 100 == 0:
            theAlias += str(round(i / 100)) + ":\n\n"
            for alias in partsToAdd:
                theAlias += alias; theAlias += " | "

            partsToAdd.clear()
            theAlias = theAlias[:-3]
            pyperclip.copy(theAlias[5:])
            f.write(theAlias)
            theAlias = ""
            # writeToFile.append(theAlias)
            


theAlias += "\n\n\n" + str(ceil(i / 100)) + ":\n\n"
for alias in partsToAdd:
    theAlias += alias; theAlias += " | "

theAlias = theAlias[:-3]

# writeToFile.append(theAlias)
# for line in writeToFile:
    # f.write(line)

f.write(theAlias)

f.close()

input("Alias has been written to a file (in the same directory as this program) and copied to your clipboard!\nPlease note, if you have over 100 commands, only the first 100 commands of your alias will have been copied!")
