 #This project is to create the game Rock, Papers, Scissors
from random import randint
print('Rock...\nPaper...\nScissors...\nShoot...')


player = input('Enter your choice Player : ').lower()
rand_num = randint(0,2)
if rand_num == 0:
	computer = 'rock'
elif rand_num == 1:
	computer = 'paper'
else:
	computer = 'scissors'
print(f'Computer plays {computer}')
print("*** NO Cheating ***\n" *10)

# rock vs. scissors scenarios

# This is RPS version against the computer

if player == computer:
	print(" It's a tie!!! ")
elif player == 'rock':
	if computer == 'scissors':
		print(f'{player} beats {computer}!!!')
		print('Player wins!!!')
	elif computer == 'paper':
		print(f'{computer} beats {player}!!!')
		print('computer wins!!!')
elif player == 'paper':
	if computer == 'scissors':
		print(f'{computer} beats {player}!!!')
		print('Computer wins!!!')
	elif computer == 'rock':
		print(f'{player} beats {computer}!!!')
		print('Player wins!!!')
elif player == 'scissors':
	if computer == 'rock':
		print(f'{computer} beats {player}!!!')
		print('Computer wins!!!')
	if computer == 'paper':
		print(f'{player} beats {computer}!!!')
		print('Player wins!!!')
else:
	print('something went wrong')

