# This project is to create the game Rock, Papers, Scissors
print('Rock...\nPaper...\nScissors...')


P1_Choice = input('Enter your choice Player 1: ')

print("*** NO Cheating ***")

print("*** NO Cheating ***")

print("*** NO Cheating ***")

print("*** NO Cheating ***")

print("*** NO Cheating ***")

print("*** NO Cheating ***")

print("*** NO Cheating ***")

print("*** NO Cheating ***")

print("*** NO Cheating ***")

print("*** NO Cheating ***")

print("*** NO Cheating ***")

print("*** NO Cheating ***")

P2_Choice = input('Enter your choice Player 2: ')

print('SHOOT!')

# rock vs. scissors scenarios

if P1_Choice == 'rock' and P2_Choice == 'scissors':
	print(f'{P1_Choice} beats {P2_Choice}!!!')
	print('Player 1 wins!!!')
elif P1_Choice == 'scissors' and P2_Choice == 'rock':
	print(f'{P2_Choice} beats {P1_Choice}!!!')
	print('Player 2 wins!!!')

# rock vs. paper scenarios

elif P1_Choice == 'rock' and P2_Choice == 'paper':
	print(f'{P2_Choice} beats {P1_Choice}!!!')
	print('Player 2 wins!!!')
elif P1_Choice == 'paper' and P2_Choice == 'rock':
	print(f'{P1_Choice} beats {P2_Choice}!!!')
	print('Player 1 wins!!!')

# scissors vs. paper scenarios

elif P1_Choice == 'scissors' and P2_Choice == 'paper':
	print(f'{P1_Choice} beats {P2_Choice}!!!')
	print('Player 1 wins!!!')
elif P1_Choice == 'paper' and P2_Choice == 'scissors':
	print(f'{P2_Choice} beats {P1_Choice}!!!')
	print('Player 2 wins!!!')
elif P1_Choice == P2_Choice:
	print('its a tie!')
else:
	print('Selection not valid \n Enter rock, paper, or scissors')
