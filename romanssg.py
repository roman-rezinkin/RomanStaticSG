#main
#Import Statements
from genericpath import isdir, isfile
from posixpath import dirname
import sys
import getopt
import os
import fnmatch
import shutil

#Variables
workingDirectoryPath = os.getcwd()
officialPath = workingDirectoryPath + "/dist"
arrayOfFiles = []
arryOfFilesWithExtension = []
secondArg = ""
isCustomDirectory = False
customDirectoryPath = ""
fileName = ""
dirName = ""
#Functions
# Converting txt files
def conversionFuncFile():
    print("\n~~~ SSG Compiling and Working! ~~~\n")      
    #For each file name convert into html and create new file.
    if (isCustomDirectory == False):
        for aFile in arrayOfFiles:
            try:
                if os.path.isdir("dist"):                         # Check to see if dist exists, if it does, delete children and parent
                    shutil.rmtree(officialPath)
                os.mkdir(officialPath)                            # Try to create new dist folder
                existingFile = open(aFile, "r")                   # Read existing file
                os.chdir(officialPath)                            # Change directories
                aFile = os.path.splitext(aFile)[0]                #Cut off the extension of the file

                n = open(fileName + ".html", "w")                 # Create new File under html extension
                newFile = open(fileName + ".html", "a")           # Open file to append contents
                            
                newFile.write("<!doctype html>\n")
                newFile.write('<html lang="en">\n')
                newFile.write("<head>\n")
                newFile.write('\t<meta charset="utf-8">\n')
                newFile.write('\t<title>' + fileName + '</title>\n')
                newFile.write('\t<meta name="viewport" content="width=device-width, initial-scale=1">\n')
                newFile.write("</head>\n")
                newFile.write("<body>\n")
                            
                temp = existingFile.read().splitlines()
        
                for x in temp:                                  # Loop through the file we opened
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
    else:
        for aFile in arrayOfFiles:
            try:
                existingFile = open(aFile, "r")                   # Read existing file
                os.chdir(customDirectoryPath)                            # Change directories
                aFile = os.path.splitext(aFile)[0]         #Cut off the extension of the file

                n = open(fileName + ".html", "w")                # Create new File under html extension
                newFile = open(fileName + ".html", "a")          # Open file to append contents
                            
                newFile.write("<!doctype html>\n")
                newFile.write('<html lang="en">\n')
                newFile.write("<head>\n")
                newFile.write('\t<meta charset="utf-8">\n')
                newFile.write('\t<title>' + fileName + '</title>\n')
                newFile.write('\t<meta name="viewport" content="width=device-width, initial-scale=1">\n')
                newFile.write("</head>\n")
                newFile.write("<body>\n")
                            
                temp = existingFile.read().splitlines()
        
                for x in temp:                                  # Loop through the file we opened
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
    if (isCustomDirectory == False):                  # Check to see if a custom output directory exists.
        try:
            if os.path.isdir("dist"):                      # Check to see if dist exists, if it does, delete children and parent
                shutil.rmtree(officialPath)
        except OSError as error:
            print("\n--- FAILURE ---")
        os.mkdir(officialPath)                             # Try to create new dist folder
        os.chdir(dirName)
        for aFile in arrayOfFiles:                     #For each file name convert into html and create new file.
            existingFile = open(aFile, "r")            # Read existing file
            os.chdir("../")                            # Change directories
            os.chdir(officialPath)
            aFile = os.path.splitext(aFile)[0]         #Cut off the extension of the file
            
            n = open(aFile + ".html", "w")             # Create new File under html extension
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
            for x in temp:                                  # Loop through the file we opened
                if (x != ""):                               # We dont want <p> tags created for new lines
                    newFile.write("\t<p>" + x + "</p>\n")
            newFile.write("</body>\n")
            newFile.write("</html>")
            existingFile.close()
            n.close()
            newFile.close()
            os.chdir("../")
            os.chdir(dirName)
        print("\n--- SUCCESS ---")
    else:
        currentDirectory = os.getcwd()
        for aFile in arrayOfFiles:
            os.chdir(dirName)
            existingFile = open(aFile, "r")            # Read current existing file
            # os.chdir("../")                          # Change directories
            os.chdir(customDirectoryPath)              # Change directories
            aFile = os.path.splitext(aFile)[0]         #Cut off the extension of the file
            n = open(aFile + ".html", "w")             # Create new File under html extension
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
            for x in temp:                                  # Loop through the file we opened
                if (x != ""):                               # We dont want <p> tags created for new lines
                    newFile.write("\t<p>" + x + "</p>\n")
            newFile.write("</body>\n")
            newFile.write("</html>")
            existingFile.close()
            n.close()
            newFile.close()
            # os.chdir("../")
            os.chdir(currentDirectory)
        print("\n--- SUCCESS ---")
            
#Main Logic
if __name__ == "__main__":
    short_opts = "hi:ov"
    long_opts = ["help", "input=", "output=", "version"]
    temp = sys.argv
    arguments = temp[1:]
    try:
        arg, values = getopt.getopt(arguments, short_opts, long_opts)
    except getopt.error as error:
        print(error)
    if (len(arg) == 0):
        print("Run Help command using -h or --help")
    else:
        for curr_arg, curr_value in arg:
            if curr_arg in ("--version", "-v"):
                print("Welcome to the RomanStaticSG, a Static Site Generator")
                print("The current version is: 0.1")
            elif curr_arg in ("--help", "-h"):
                print("\nHelp Screen\n")
                print("Usage: python romanssg.py\n")
                print("Commands: \nTo get version number use the command: --version, -v")
            elif curr_arg in ("--output", "-o"):
                if os.path.isdir(curr_value):
                    print("Output Directory has been changed to " + curr_value)
                    isCustomDirectory = True
                    customDirectoryPath = curr_value
                else:
                    print("ERROR: Directory does not exist! Please enter a valid directory")
            elif curr_arg in ("--input", "-i"):
                if (os.path.isdir(curr_value)):
                    print("Working on Directory")
                    dirName = curr_value
                    for i in os.listdir(curr_value):
                        if fnmatch.fnmatch(i, "*.txt"):
                            arrayOfFiles.append(i)
                    conversionFuncFolder()
                else:
                    print("Working on File " + curr_value)
                    fileName = curr_value
                    for i in os.listdir("."):
                        if fnmatch.fnmatch(i, "*.txt"):
                            arrayOfFiles.append(i)
                    conversionFuncFile()
            else:
                print("Error")                