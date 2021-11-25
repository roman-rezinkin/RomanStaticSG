"""
Main Static Site Functionality
"""
# Import Statements
from json.decoder import JSONDecodeError
import sys
import getopt
import os
import fnmatch
import json
from . import roman_ssg_util


def main(arguments):
    # Local Variables
    SHORT_OPTS = "hiovlc"
    LONG_OPTS = ["help", "input=", "output=", "version", "lang=", "config="]
    LANG = ""
    IS_CUSTOMDIRECTORY = False
    arrayOfFiles = []
    CUSTOM_DIRECTORY_PATH = ""
    workingDirectoryPath = os.getcwd()
    distFolder = workingDirectoryPath + "/dist"
    try:
        arg, values = getopt.getopt(arguments, SHORT_OPTS, LONG_OPTS)
    except getopt.error as error:
        print(error)
    if len(arg) == 0:
        print("Run Help command using -h or --help")
    else:
        for curr_arg, curr_value in arg:
            if curr_arg in ("--version", "-v"):
                print("Welcome to the RomanStaticSG, a Static Site Generator")
                print("The current version is: 0.1")
            elif curr_arg in ("--help", "-h"):
                print("\nHelp Screen\n")
                print("Usage: python romanssg.py\n")
                print(
                    "Commands: \nTo get version number use the command: --version, -v"
                )
                print(
                    "To change the output directory to a user specified directory, \
                    run --output= or -o="
                )
                print(
                    "To specify an input, use either a \
                    file or a folder with items inside of it"
                )
                print("To specify input use: --input= or -i=")
            elif curr_arg in ("--config", "-c"):
                # Override other args
                arg = arg[: len(arg)]

                # Open json and store in config
                try:
                    with open(curr_value, "rb") as f:
                        try:
                            config = json.load(f)
                        except JSONDecodeError:
                            print("Invalid JSON")
                            sys.exit(1)
                except FileNotFoundError:
                    print("Config file not found")
                    sys.exit(1)

                # Order the args from the json
                # (Needs to be done because order
                # of args matters with this script)
                config_list = []
                if "lang" in config:
                    config_list.append(("--lang", config["lang"]))
                if "output" in config:
                    config_list.append(("--output", config["output"]))
                if "input" in config:
                    config_list.append(("--input", config["input"]))

                # Add args to be processed
                for argument in config_list:
                    arg.append(argument)
            elif curr_arg in ("--lang", "-l"):
                LANG = curr_value
            elif curr_arg in ("--output", "-o"):
                if os.path.isdir(curr_value):
                    print("Output Directory has been changed to " + curr_value)
                    IS_CUSTOMDIRECTORY = True
                    CUSTOM_DIRECTORY_PATH = curr_value
                else:
                    print(
                        "ERROR: Directory does not exist! \
                        Please enter a valid directory"
                    )
            elif curr_arg in ("--input", "-i"):
                if LANG == "":
                    LANG = "en-CA"
                if os.path.isdir(curr_value):
                    print("Working on Directory")
                    dirName = curr_value
                    for i in os.listdir(curr_value):
                        if fnmatch.fnmatch(i, "*.txt") or fnmatch.fnmatch(i, "*.md"):
                            arrayOfFiles.append(i)
                    roman_ssg_util.conversion_func_folder(
                        LANG,
                        dirName,
                        IS_CUSTOMDIRECTORY,
                        arrayOfFiles,
                        CUSTOM_DIRECTORY_PATH,
                        distFolder,
                    )
                else:
                    print("Working on File " + curr_value)
                    arrayOfFiles.append(curr_value)
                    roman_ssg_util.conversion_func_file(
                        LANG,
                        IS_CUSTOMDIRECTORY,
                        arrayOfFiles,
                        CUSTOM_DIRECTORY_PATH,
                        distFolder,
                    )
            else:
                print("Error")


# Main Logic
if __name__ == "__main__":
    main(sys.argv[1:])
