import os
import shutil
import markdown

# Functions
def getLocalFiles(arrayOfFiles):
    localArr = []
    for i in arrayOfFiles:
        if os.name == "posix":
            temp = os.getcwd() + "/" + str(i)
        else:
            temp = os.getcwd() + "\\" + str(i)
        localArr.append(temp)
    return localArr

# Create Index HTML Page
def createIndexPage(hmtlLang, previousFileNameArr):
    counter = 1
    indexPage = open("index.html", "w")
    indexPage.write("<!doctype html>\n")
    indexPage.write('<html lang="' + hmtlLang + '">\n')
    indexPage.write("<head>\n")
    indexPage.write('\t<meta charset="utf-8">\n')
    indexPage.write("\t<title>" + "Index" + "</title>\n")
    indexPage.write(
        '\t<meta name="viewport" content="width=device-width, initial-scale=1">\n'
    )
    indexPage.write("</head>\n")
    indexPage.write("<body>\n")
    for name in previousFileNameArr:
        linkString = f'<a href="./{name}.html">{counter}. {name}</a><br>'
        indexPage.write(str(linkString))
        counter += 1
    indexPage.close()

def writeToFile(hmtlLang, aFile, fileCounter, striclyFileNames):
    # Read Current Existing File
    originalFile = open(aFile, "r", encoding="utf8")  # Read existing file
    originalFileName, end = os.path.splitext(striclyFileNames[fileCounter])  # Cut off the extension of the file
    temp = originalFile.read().splitlines()
    checkForTheme = temp
    
    # Create new File under html Extension, and open file.
    newFile = open(originalFileName + ".html", "w")
    newFile = open(originalFileName + ".html", "a")
    # Write main html section
    newFile.write("<!doctype html>\n")
    newFile.write('<html lang="' + hmtlLang + '">\n')
    newFile.write("<head>\n")
    newFile.write('\t<meta charset="utf-8">\n')
    newFile.write("\t<title>" + originalFileName + "</title>\n")
    newFile.write('\t<meta name="viewport" content="width=device-width, initial-scale=1">\n')
    for i in checkForTheme:
        if i.startswith("theme"):
            if 'dark' or 'Dark' in i:
                print("We here")
                createCSSFile(True)
                newFile.write('\t<link rel="stylesheet" href="main.css" type="text/css">\n')
                temp.pop(0)
    newFile.write("</head>\n")
    newFile.write("<body>\n")
    # Bulk of Main Logic of reading file and putting it into html file.
    for i in temp:  # Loop through the file we opened
        if i != "":  # We dont want <p> tags created for new lines
            if end == ".txt":
                newFile.write("\t<p>" + i + "</p>\n")
            if end == ".md":
                newFile.write("\t" + markdown.markdown(i) + '\n')
    newFile.write("</body>\n")
    newFile.write("</html>")
    originalFile.close()
    newFile.close()

# Create CSS file
def createCSSFile(hasThemeColor):
    if hasThemeColor:
        cssFile = open("main.css", "w")
        cssFile = open("main.css", "a")
        cssFile.write("body{background-color: #2a2b2d}" + "\n")
        cssFile.write("p, h1, h2, h3, h4, li, ul, code{color: #fefefe}" + "\n")
        cssFile.close()

# Converting txt files
def conversionFuncFile(lang, isCustomDirectory, arrayOfFiles, customDirectoryPath, distFolder):
    # Local Variables
    localFiles = []
    striclyFileNames = arrayOfFiles
    localFiles = getLocalFiles(arrayOfFiles)
    fileCounter = 0
    print("\n~~~ SSG Compiling and Working! ~~~\n")
    # For File name convert into html and create new File.
    if isCustomDirectory is False:
        try:
            if os.path.isdir(
                "dist"
            ):  # Check to see if dist exists, if it does, delete children and parent
                shutil.rmtree(distFolder)
            os.mkdir(distFolder)  # Try to create new dist folder
        except OSError as error:
            print("\n--- FAILURE ---")
            print(error)

        for i in localFiles:
            os.chdir(distFolder)  # Change directories
            writeToFile(lang, i, fileCounter, striclyFileNames) # Call the Write Function
            fileCounter += 1
        print("\n--- SUCCESS ---")
    else:
        for file in localFiles:
            os.chdir(customDirectoryPath)  # Change directories
            writeToFile(lang, file, fileCounter, striclyFileNames) # Call the Write Function
            fileCounter += 1
        print("\n--- SUCCESS ---")

# Converting files from within a folder
def conversionFuncFolder(lang, directoryName, isCustomDirectory, arrayOfFiles, customDirectoryPath, distFolder):
    # Local Variables
    localFiles = []
    striclyFileNames = arrayOfFiles
    fileCounter = 0
    previousFileNameArr = []
    print("\n~~~ SSG Compiling and Working! ~~~\n")
    if isCustomDirectory == False:  # Check to see if a custom output directory exists.
        try:
            if os.path.isdir(
                "dist"
            ):  # Check to see if dist exists, if it does, delete children and parent
                shutil.rmtree(distFolder)
        except OSError as error:
            print("\n--- FAILURE ---")

        # Try to create new dist folder
        os.mkdir(distFolder)
        # Change to specified Folder
        os.chdir(directoryName)
        directoryPath = os.getcwd()
        localFiles = getLocalFiles(arrayOfFiles)

        # Main Logic
        for file in localFiles:
            previousFileNameArr.append(os.path.splitext(striclyFileNames[fileCounter])[0])
            os.chdir(distFolder)
            writeToFile(lang, file, fileCounter, striclyFileNames)
            fileCounter += 1
            os.chdir(directoryPath)

        # Create Custom Index html page with links to all the created files
        os.chdir(distFolder)
        createIndexPage(lang, previousFileNameArr)
        print("\n--- SUCCESS ---")
    else:
        # Change to specified Folder
        os.chdir(directoryName)
        
        # Gather local files and convert them into usable paths
        localFiles = getLocalFiles(arrayOfFiles)
        
        # Main logic
        for file in localFiles:
            directoryPath = os.getcwd()
            previousFileNameArr.append(os.path.splitext(striclyFileNames[fileCounter])[0])
            tempCustomDirectoryPath = os.path.join('../', customDirectoryPath)
            os.chdir(tempCustomDirectoryPath)
            writeToFile(lang, file, fileCounter, striclyFileNames)
            fileCounter += 1
            os.chdir(directoryPath)

        # Create Custom Index html page with links to all the created files
        os.chdir(tempCustomDirectoryPath)
        createIndexPage(lang, previousFileNameArr)
        print("\n--- SUCCESS ---")