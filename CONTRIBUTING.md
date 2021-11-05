# How to Contribute
## Setup
***Python 3.9+ Required***  
You must install Python version 3.9+ in order to develop RomanStaticSG, as well as to even run it.

## To contribute code
The romanssg.py file contains the main logic for the static site generator, and romanSSGUtil.py file contains all the utility functions that help with the main romanssg file.

Feel free to use any logic from Python in order to develop the static site generator, however, if you are implementing utility functions, please make sure to place them inside the romanSSGUtil.py file. This keeps the code more organized.'

## Recommended IDE
For this project, we highly suggest using Visual Studio Code. We have a common settings.json within .vscode folder that includes automatic use of the formatter and linter (Black and Pylint), respectively.

## Formatting your code
This project utilizes the python formatter by the name of "black". Please run this section before committing or pushing any code!
### Installing and Using the Formatter
Run this in your command line to install the formatting:
1.    pip install black

Run this shell script anytime you want to format the two files.
1.    bash formatting.sh

If a new file is introduced, please edit formatting.sh and add the file to the script

## Linting your code
This project utilizes pylint to lint the code to ensure that the conventions of the code are up to standards with PEP8

Run the following command line to install the linter:
1.    pip install pylint

Run this shell script anytime to lint the files
1.    bash linter.sh

If a new file is introduced, please edit linter.sh and add the file to the script

## Developing changes
Please create a branch based off the issue number, as this will ensure that the branches and pull requests are all aligned together, which keeps everything organized.

Once you have introduced a new feature, please commit all your changes and create a PR. From there, one of the code owners will review your changes and approve or request changes.

Once the PR is approved, feel free to merge the changes into the master branch


