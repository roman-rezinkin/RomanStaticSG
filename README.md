# RomanStaticSG
## Welcome to Romans Static Site Generator v.0.1
## About RomanStaticSG
RomanStaticSG is made in python. It is a simple static site generator. It accepts an input file, or input folder. The current file types that are parsed are text and markdown. Markdown however currently only supports heading level 1 parsing. The program will then take the accepted files and create basic html webpages, as well as an index.html file. The script also allows you to input a custom output directory, so that the files could be saved in a custom location.

## How to Use RomanStaticSG
***Python 3.9+ Required***  
### Method 1
RomanStaticSG is now released with v1.0.4.
To install RomanStaticSG simply enter:  
```python
    pip install staticsg-rrezinkin
```
To use the static site generator, import it as following:  
```python
    from staticsg import romanssg
    romanssg.main(sys.argv[1:])
```
A list of [arguments](#command_list) can be found below.

### Method 2
Fork and clone this repository. Then execute any of the following [commands](#command_list) within the RomanStaticSG folder
    
    python romanssg.py --help

If you run the input command and don't specify the output command, a local folder named "dist" will be created in the directory of the existing file.  
  
**!!NOTE!!**  
  
**If you are executing the following commands from your command line, please navigate to the ```src/staticg``` folder, as the commands below expect that you are located in that directory!!**
## <a name="command_list"></a>Command List
### Help Screen 
```c
    python romanssg.py --help  |  python romanssg.py -h  
      
    Help Screen  
    Usage: python romanssg.py
    Commands:
    To get version number use the command: --version, -v
    To change the output directory to a user specified directory, run --output= or -o=
    To specify an input, use either a file or a folder with items inside of it
```
### Version Check
```java
    python romanssg.py --version  |   python romanssg.py -v

    Welcome to the RomanStaticSG, a Static Site Generator  
    The current version is: 1.0.4
```
### Input Command
To run the input command specify the file name **with** the extension  
```java
    python romanssg.py --input=example.txt    |    python romanssg.py --input=example.md
```

To run the input command with a folder, specify the folder name  
  
**For Unix/Linux**
```java
    python romanssg.py --input=./someFolder   |   python romanssg.py -i=./someFolder
```
**For Windows**
```java
    python romanssg.py --input="C:\Users\Roman Rezinkin\Desktop"    |   python romanssg.py -i="C:\Users\Roman Rezinkin\Desktop"
```
### Output Command
To run the output command specify the custom directory location  
  
#### For Unix/Linux
```java
    python romanssg.py --output=./someFolder
```
-OR-
```java
    python romanssg.py -o=./someFolder
```
#### For Windows
```java
    python romanssg.py --output="C:\Users\Roman Rezinkin\Desktop"    |   python romanssg.py -o="C:\Users\Roman Rezinkin\Desktop"
```
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
