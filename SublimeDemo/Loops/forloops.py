#for number in range(1,8):
#	print(number)

#for letter in "coffe":
#	print(letter)

#for num in range(10,20,2):
#	print(num)

#x = input('How many times do i have to tell you? ')
#x = int(x)
#for y in range(x):
#	print('clean up your room!')

for x in range(1,21):
	if x == 4 or x == 13:
		state = ' unlucky'
	elif x%2 == 0:
		state = 'even'
	else:
		state = 'odd'
	print(f'{x} is {state}')