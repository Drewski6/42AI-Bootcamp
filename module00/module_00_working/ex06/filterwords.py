import sys
import string

#sys.tracebacklimit = 0
assert (len(sys.argv) == 3), "ERROR"

try:
	size_w = int(sys.argv[2])
except ValueError:
	print("ERROR")
	quit()

input_str = sys.argv[1]
for item in string.punctuation:
	input_str = input_str.replace(item, '')

input_lst = input_str.split(' ')

final_lst = [item for item in input_lst if len(item) > int(sys.argv[2])]
print(final_lst)
