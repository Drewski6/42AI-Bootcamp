import random

number = random.randint(1, 99)
print("This is an interactive guessing game!\n" \
		"You have to enter a number between 1 and 99 to find out the secret number.\n" \
		"Type 'exit' to end the game.\n" \
		"Good luck!\n")

user_input = ""
i = 0
while (user_input != 'exit'):
	i = i + 1
	user_input = input("\nWhat's your guess between 1 and 99?\n")
	try:
		int(user_input)
	except ValueError:
		if (user_input != 'exit'):
			print("That's not a number.")
		continue
	try:
		assert (int(user_input) > 0 and int(user_input) < 100)
	except AssertionError:
		print("That number is not between 1 and 99")
		continue

	if (int(user_input) == 42):
		print("The answer to the ultimate question of life the universe and everything is 42.")
	if (int(user_input) > number):
		print("Too high!")
		continue
	if (int(user_input) < number):
		print("Too low!")
		continue
	if (int(user_input) == number and i == 1):
		print("Congratuations! You got it on your first try!")
		quit()
	if (int(user_input) == number):
		print("Congratuation you've got it!")
		print(f"You won in {i} attempts!")
		quit()
print("Goodbye!")
