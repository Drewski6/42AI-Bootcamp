import sys

string = ""
for item in sys.argv[1:]:
    if (item == sys.argv[1]):
        string = string + item
    else:
        string = string + " " + item
print(string[::-1].swapcase())
