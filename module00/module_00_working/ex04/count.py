import sys
import string


sys.tracebacklimit = 0
def text_analyzer(input_str=""):
    """
    text_analyzer - A function that takes a string and prints the number of
    uppercase
    letters, lowercase letters, space characters, and puncutation marks.
    Takes a string or nothing. If nothing is given, will prompt user for
    input through the terminal.
    """
    if input_str == "":
        input_str = input("What is the text to analyze?\n")
    assert (isinstance(input_str, str)), "Please assure that your input is a string."
    uppercase_letters = 0
    lowercase_letters = 0
    space_char = 0
    punctuation = 0
    for letter in input_str:
        if letter.isupper() is True:
            uppercase_letters += 1
        if letter.islower() is True:
            lowercase_letters += 1
        if letter.isspace() is True:
            space_char += 1
        if letter in string.punctuation:
            punctuation += 1
    print(f"The text contains {len(input_str)} character(s)")
    print(f"- {uppercase_letters} upper letter(s)")
    print(f"- {lowercase_letters} lower letter(s)")
    print(f"- {punctuation} punctuation mark(s)")
    print(f"- {space_char} space(s)")


assert (len(sys.argv) <= 2), "Too many arguments."
if len(sys.argv) == 2:
    text_analyzer(str(sys.argv[1]))
    assert (isinstance(sys.argv[1], str)), "input was not a string"
else:
    text_analyzer()
