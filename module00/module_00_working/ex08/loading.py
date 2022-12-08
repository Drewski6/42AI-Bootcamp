import time
import sys

def ft_progress(lst):
	start_time = 3
	i = 0
	while True:
		print(f"\r{lst[i]}")
		yield lst[i]
		i = i + 1









listy = range(1000)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	time.sleep(0.01)
print()
print(ret)