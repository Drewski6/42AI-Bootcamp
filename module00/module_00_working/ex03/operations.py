import sys

sys.tracebacklimit = 0
assert (len(sys.argv) == 3), "Number of arguments must equal 2."
try:
    isinstance(int(sys.argv[1]), int)
    isinstance(int(sys.argv[2]), int)
except ValueError:
    print(f"Both arguments should be integers.")

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print(f"Sum:\t\t{num1 + num2}")
print(f"Difference :\t{num1 - num2}")
print(f"Product:\t{num1 * num2}")
print(f"Quotient:\t{num1 / num2}")
print(f"Remainder:\t{num1 % num2}")
