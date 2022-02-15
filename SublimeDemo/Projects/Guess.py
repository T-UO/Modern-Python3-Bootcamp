# This game is created for users to guess a number b/t 1 and 10, inclusive

from random import randint

number = randint(1,10) # generates random #
attempt = input("Guess a number between 1 and 10: ")

while True:
	attempt = int(attempt) # converts string to #
	if attempt < number:
		print("Too low, try again!")
		attempt = input("Guess a number between 1 and 10: ")
	elif attempt > number:
		print("Too high, try again!")
		attempt = input("Guess a number between 1 and 10: ")
	elif attempt == number:
		print("You guessed it! You won!")
		ask = input("Do you want to keep playing? (y/n) ")
		if ask == "y":
			number = randint(1,10) # generates random #
		else:
			break
	else:
		print("Something went wrong!")

