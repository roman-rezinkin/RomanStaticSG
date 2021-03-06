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
```
pip install black
```
Run this shell script anytime you want to format the two files.
```
bash formatting.sh
```
If a new file is introduced, please edit formatting.sh and add the file to the script

## Linting your code
This project utilizes pylint to lint the code to ensure that the conventions of the code are up to standards with PEP8

Run the following command line to install the linter:
```
pip install pylint
```
Run this shell script anytime to lint the files
```
bash linter.sh
```
If a new file is introduced, please edit linter.sh and add the file to the script

## Developing changes
Please create a branch based off the issue number, as this will ensure that the branches and pull requests are all aligned together, which keeps everything organized.

Once you have introduced a new feature, please commit all your changes and create a PR. From there, one of the code owners will review your changes and approve or request changes.

Once the PR is approved, feel free to merge the changes into the master branch

## Testing your changes
This project utilizes pytest. We implemented it inorder to ensure the code that is written operates correctly. Whenever you introduce a new function or change any kind of code within our static site generator, it is essential to introduce or change the tests.
### Setting up Pytest
Run the following command:
```
pip install -U pytest
```
I highly recommend using Visual Studio as we have setup a settings.json that enables auto rerunning of tests, as well it features a nice UI that allows for running individual tests and all the tests combined.
### Writing the tests
For pytest to work please follow the following syntax when naming a specific test
```
test_some_function_test
```
It is important to include the test in the first part of the test as thats the only way that pytest understands that it is a test