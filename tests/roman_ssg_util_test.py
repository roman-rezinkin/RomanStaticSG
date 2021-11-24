"""Testing File for roman_ssg_util"""
import os
import shutil
import src.staticsg.roman_ssg_util


def setup_test():
    """Setup Tests for tests"""
    os.chdir(os.getcwd())
    if os.path.isdir("dist"):
        shutil.rmtree("dist")
    if os.path.isdir("testCustomDirectory"):
        shutil.rmtree("testCustomDirectory")


def test_get_local_files():
    """Test get_local_files function"""
    tempArr = ["File1.txt"]
    if os.name == "posix":
        assert src.staticsg.roman_ssg_util.get_local_files(tempArr) == [
            os.getcwd() + "/" + "File1.txt"
        ]
    else:
        assert src.staticsg.roman_ssg_util.get_local_files(tempArr) == [
            os.getcwd() + "\\" + "File1.txt"
        ]


def test_create_css_file():
    """Test Create CSS File function"""
    src.staticsg.roman_ssg_util.create_css_file(True)
    assert os.path.isfile("./main.css")
    os.remove("main.css")


def test_create_css_file_fail():
    """Test fail of Create CSS File function"""
    src.staticsg.roman_ssg_util.create_css_file(False)
    assert not os.path.isfile("./main.css")


def test_write_to_file():
    """Test write_to_file function"""
    if os.name == "posix":
        filePath = os.getcwd() + "/" + "example.txt"
    else:
        filePath = os.getcwd() + "\\" + "example.txt"
        src.staticsg.roman_ssg_util.write_to_file(
            "en-CA",
            filePath,
            0,
            ["example.txt"],
        )
    assert os.path.isfile("example.html")
    os.remove("example.html")


def test_conversion_func_file_non_custom_dir():
    """Test Conversion File function without Custom Directory"""
    fileArr = []
    fileArr.append("example.txt")
    fileArr.append("test.md")
    if os.name == "posix":
        src.staticsg.roman_ssg_util.conversion_func_file(
            "en-CA",
            False,
            fileArr,
            "",
            os.getcwd() + "/" + "dist",
        )
    else:
        src.staticsg.roman_ssg_util.conversion_func_file(
            "en-CA",
            False,
            fileArr,
            "",
            os.getcwd() + "\\" + "dist",
        )
    assert os.path.isfile("example.html")
    assert os.path.isfile("test.html")


def test_conversion_func_file_custom_dir():
    """Test Conversion File function with Custom Directory"""
    os.chdir("..")
    setup_test()
    fileArr = []
    fileArr.append("example.txt")
    fileArr.append("test.md")
    os.mkdir("testCustomDirectory")
    if os.name == "posix":
        src.staticsg.roman_ssg_util.conversion_func_file(
            "en-CA",
            True,
            fileArr,
            os.getcwd() + "/" + "testCustomDirectory",
            os.getcwd() + "/" + "dist",
        )
    else:
        src.staticsg.roman_ssg_util.conversion_func_file(
            "en-CA",
            True,
            fileArr,
            os.getcwd() + "\\" + "testCustomDirectory",
            os.getcwd() + "\\" + "dist",
        )
    assert os.path.isfile("example.html")
    assert os.path.isfile("test.html")


def test_converstion_func_folder_non_custom_dir():
    """Test Conversion Folder function without Custom Directory"""
    os.chdir("..")
    setup_test()
    arrayOfFiles = []
    arrayOfFiles.append("Silver Blaze.txt")
    arrayOfFiles.append("The Adventure of the Six Napoleans.txt")
    arrayOfFiles.append("The Adventure of the Speckled Band.txt")
    arrayOfFiles.append("The Naval Treaty.txt")
    arrayOfFiles.append("The Red Headed League.txt")
    if os.name == "posix":
        src.staticsg.roman_ssg_util.conversion_func_folder(
            "en-CA",
            os.getcwd() + "/" + "Sherlock-Holmes-Selected-Stories",
            False,
            arrayOfFiles,
            "",
            os.getcwd() + "/" + "dist",
        )
    else:
        src.staticsg.roman_ssg_util.conversion_func_folder(
            "en-CA",
            os.getcwd() + "\\" + "Sherlock-Holmes-Selected-Stories",
            False,
            arrayOfFiles,
            "",
            os.getcwd() + "\\" + "dist",
        )
    assert os.path.isfile("Silver Blaze.html")
    assert os.path.isfile("The Adventure of the Six Napoleans.html")
    assert os.path.isfile("The Adventure of the Speckled Band.html")
    assert os.path.isfile("The Naval Treaty.html")
    assert os.path.isfile("The Red Headed League.html")


def test_converstion_func_folder_custom_dir():
    """Test Conversion Folder function with Custom Directory"""
    os.chdir("..")
    setup_test()
    arrayOfFiles = []
    arrayOfFiles.append("Silver Blaze.txt")
    arrayOfFiles.append("The Adventure of the Six Napoleans.txt")
    arrayOfFiles.append("The Adventure of the Speckled Band.txt")
    arrayOfFiles.append("The Naval Treaty.txt")
    arrayOfFiles.append("The Red Headed League.txt")

    if os.path.isdir("testCustomDirectory"):
        shutil.rmtree("testCustomDirectory")
        os.mkdir("testCustomDirectory")
    else:
        os.mkdir("testCustomDirectory")
    if os.name == "posix":
        src.staticsg.roman_ssg_util.conversion_func_folder(
            "en-CA",
            os.getcwd() + "/" + "Sherlock-Holmes-Selected-Stories",
            True,
            arrayOfFiles,
            os.getcwd() + "/" + "testCustomDirectory",
            os.getcwd() + "/" + "dist",
        )
    else:
        src.staticsg.roman_ssg_util.conversion_func_folder(
            "en-CA",
            os.getcwd() + "\\" + "Sherlock-Holmes-Selected-Stories",
            True,
            arrayOfFiles,
            os.getcwd() + "\\" + "testCustomDirectory",
            os.getcwd() + "\\" + "dist",
        )
    assert os.path.isfile("Silver Blaze.html")
    assert os.path.isfile("The Adventure of the Six Napoleans.html")
    assert os.path.isfile("The Adventure of the Speckled Band.html")
    assert os.path.isfile("The Naval Treaty.html")
    assert os.path.isfile("The Red Headed League.html")
    os.chdir("..")
    shutil.rmtree("testCustomDirectory")
