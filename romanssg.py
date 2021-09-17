#main
#Import Statements
from genericpath import isdir, isfile
import sys
import os
import fnmatch
import shutil

#Variables
workingDirectoryPath = os.getcwd()
officialPath = workingDirectoryPath + "/dist"
arrayOfFiles = []
arryOfFilesWithExtension = []
secondArg = ""
#Functions
# Converting txt files
def conversionFuncFile():
    print("\n~~~ SSG Compiling and Working! ~~~\n")
            
    #For each file name convert into html and create new file.
    for aFile in arrayOfFiles:
        try:
            if os.path.isdir("dist"):                         # Check to see if dist exists, if it does, delete children and parent
                shutil.rmtree(officialPath)
            os.mkdir(officialPath)                            # Try to create new dist folder
            existingFile = open(aFile, "r")                   # Read existing file
            os.chdir(officialPath)                            # Change directories
            n = open(secondArg + ".html", "x")              # Create new File under html extension
            newFile = open(secondArg + ".html", "a")        # Open file to append contents
                        
            newFile.write("<!doctype html>\n")
            newFile.write('<html lang="en">\n')
            newFile.write("<head>\n")
            newFile.write('\t<meta charset="utf-8">\n')
            newFile.write('\t<title>' + secondArg + '</title>\n')
            newFile.write('\t<meta name="viewport" content="width=device-width, initial-scale=1">\n')
            newFile.write("</head>\n")
            newFile.write("<body>\n")
                        
            temp = existingFile.read().splitlines()
      
            for x in temp:                            # Loop through the file we opened
                if (x != ""):                               # We dont want <p> tags created for new lines
                    newFile.write("\t<p>" + x + "</p>\n")
            newFile.write("</body>\n")
            newFile.write("</html>")
            existingFile.close()
            n.close()
            newFile.close()
            print("\n--- SUCCESS ---")
        except OSError as error:
            print("\n--- FAILURE ---")
            print(error) 

# Converting files from within a folder
def conversionFuncFolder():
    print("\n~~~ SSG Compiling and Working! ~~~\n")
    try:
        if os.path.isdir("dist"):                         # Check to see if dist exists, if it does, delete children and parent
                shutil.rmtree(officialPath)
    except OSError as error:
        print("\n--- FAILURE ---")
        print(error)
    os.mkdir(officialPath)                            # Try to create new dist folder
    os.chdir(secondArg)        
    #For each file name convert into html and create new file.
    for aFile in arrayOfFiles:
        existingFile = open(aFile, "r")            # Read existing file
        os.chdir("../")                            # Change directories
        os.chdir(officialPath)
        n = open(aFile + ".html", "x")             # Create new File under html extension
        newFile = open(aFile + ".html", "a")       # Open file to append contents
                        
        newFile.write("<!doctype html>\n")
        newFile.write('<html lang="en">\n')
        newFile.write("<head>\n")
        newFile.write('\t<meta charset="utf-8">\n')
        newFile.write('\t<title>' + aFile + '</title>\n')
        newFile.write('\t<meta name="viewport" content="width=device-width, initial-scale=1">\n')
        newFile.write("</head>\n")
        newFile.write("<body>\n")
                        
        temp = existingFile.read().splitlines()
        for x in temp:                            # Loop through the file we opened
            if (x != ""):                               # We dont want <p> tags created for new lines
                newFile.write("\t<p>" + x + "</p>\n")
        newFile.write("</body>\n")
        newFile.write("</html>")
        existingFile.close()
        n.close()
        newFile.close()
        os.chdir("../")
        os.chdir(secondArg)
    print("\n--- SUCCESS ---")
            
#Main Logic
if __name__ == "__main__":
    if (len(sys.argv) == 1): # If Empty, show available commands
        print("\nFor a list of commands please run:\n\npython romanssg.py --help")
    if (len(sys.argv) > 1):  # If arguments are biggest than one (since the first is the .py file)
        if (sys.argv[1] == "--version" or sys.argv[1] == "-v"): #If user typed in version
            print("Welcome to the RomanStaticSG, a Static Site Generator")
            print("The current version is: 0.1")
        if (sys.argv[1] == "--help" or sys.argv[1] == "-h"): #If user typed in help
            print("\nHelp Screen\n")
            print("Usage: python romanssg.py\n")
            print("Commands: \nTo get version number use the command: --version, -v")
        if (sys.argv[1] == "--input" or sys.argv[1] == "-i"):
            secondArg = sys.argv[2]
            if (os.path.isdir(secondArg)):
                print("Working on Directory")
                for fileName in os.listdir(secondArg):
                    if fnmatch.fnmatch(fileName, "*.txt"):
                        arrayOfFiles.append(fileName)
                conversionFuncFolder()
            elif (os.path.isfile(secondArg)):
                print("Working on File")
                for fileName in os.listdir("."):
                    if fnmatch.fnmatch(fileName, "*.txt"):
                        arrayOfFiles.append(fileName)
                conversionFuncFile()
            else:
                print('\nIt seems you are working with a directory.\nPlease use "" around the directory\nExample would be: "C:\Desktop"')
        else:
            print("Invalid command, please run:\n\n\tpython romanssg.py --help")