import sys

sys.tracebacklimit = 0
try:
    int(sys.argv[1])
except:
    raise AssertionError("argument is not an integer")
if (len(sys.argv) > 2):
    raise AssertionError("more than one argument are provided")

if (int(sys.argv[1]) == 0):
    print("I'm Zero.")
elif (int(sys.argv[1]) % 2 == 0):
    print("I'm Even.")
else:
    print("I'm Odd.")
