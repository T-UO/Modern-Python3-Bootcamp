from random import random

def flip_coin():
	# generate random number from 0-1
	if random():
		return "Heads"
	else:
		return "Tails"
print(flip_coin())

def generate_evens():
   x = [num for num in range(1,50) if num % 2 ==0]
   print(x)
generate_evens()