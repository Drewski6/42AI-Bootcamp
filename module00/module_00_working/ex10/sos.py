import sys

code_dict = {
	"A": ".-",
	"B": "-...",
	"C": "-.-.",
	"D": "-..",
	"E": ".",
	"F": "..-.",
	"G": "--.",
	"H": "....",
	"I": "..",
	"J": ".---",
	"K": "-.-",
	"L": ".-..",
	"M": "--",
	"N": "-.",
	"O": "---",
	"P": ".--.",
	"Q": "--.-",
	"R": ".-.",
	"S": "...",
	"T": "-",
	"U": "..-",
	"V": "...-",
	"W": ".--",
	"X": "-..-",
	"Y": "-.--",
	"Z": "--..",
	"1": ".----",
	"2": "..---",
	"3": "...--",
	"4": "....-",
	"5": ".....",
	"6": "-....",
	"7": "--...",
	"8": "---..",
	"9": "----.",
	"0": "-----",
	" ": "/"
}

input_str = ""
if (len(sys.argv) == 1):
	quit()
for item in range(len(sys.argv)):
	if (item == 0):
		continue
	if (input_str == ""):
		input_str = sys.argv[item]
	else:
		input_str = input_str + " " + sys.argv[item]

for item in input_str:
	print(f"{code_dict[item.upper()]} ", end="")
# print(input_str)
