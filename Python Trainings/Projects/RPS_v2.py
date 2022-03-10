# This project is to create the game Rock, Papers, Scissors
print('Rock...\nPaper...\nScissors...\nShoot...')


P1_Choice = input('Enter your choice Player 1: ')

print("*** NO Cheating ***\n" *40)

P2_Choice = input('Enter your choice Player 2: ')

# rock vs. scissors scenarios

# This is a more concise version of RPS game without all of the "and" statements
if P1_Choice == P2_Choice:
	print(" It's a tie!!! ")
elif P1_Choice == 'rock':
	if P2_Choice == 'scissors':
		print(f'{P1_Choice} beats {P2_Choice}!!!')
		print('Player 1 wins!!!')
	elif P2_Choice == 'paper':
		print(f'{P2_Choice} beats {P1_Choice}!!!')
		print('Player 2 wins!!!')
elif P1_Choice == 'paper':
	if P2_Choice == 'scissors':
		print(f'{P2_Choice} beats {P1_Choice}!!!')
		print('Player 2 wins!!!')
	elif P2_Choice == 'rock':
		print(f'{P1_Choice} beats {P2_Choice}!!!')
		print('Player 1 wins!!!')
elif P1_Choice == 'scissors':
	if P2_Choice == 'rock':
		print(f'{P2_Choice} beats {P1_Choice}!!!')
		print('Player 2 wins!!!')
	if P2_Choice == 'paper':
		print(f'{P1_Choice} beats {P2_Choice}!!!')
		print('Player 1 wins!!!')
else:
	print('something went wrong')

