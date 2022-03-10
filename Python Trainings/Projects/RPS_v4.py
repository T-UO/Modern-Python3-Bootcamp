# This project is to create the game Rock, Papers, Scissors

# RPS using while loop and including scoreboard

from random import randint
print('Rock...\nPaper...\nScissors...\nShoot...')

player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
	print(f"Player score: {player_wins} Computer Score: {computer_wins}")
	player = input('Enter your choice Player : ').lower()
	if player == "quit" or player == "q":
		break
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
			player_wins += 1
		elif computer == 'paper':
			print(f'{computer} beats {player}!!!')
			print('computer wins!!!')
			computer_wins += 1
	elif player == 'paper':
		if computer == 'scissors':
			print(f'{computer} beats {player}!!!')
			print('Computer wins!!!')
			computer_wins += 1
		elif computer == 'rock':
			print(f'{player} beats {computer}!!!')
			print('Player wins!!!')
			player_wins += 1
	elif player == 'scissors':
		if computer == 'rock':
			print(f'{computer} beats {player}!!!')
			print('Computer wins!!!')
			computer_wins += 1
		if computer == 'paper':
			print(f'{player} beats {computer}!!!')
			print('Player wins!!!')
			player_wins += 1
	else:
		print('something went wrong')

	if player_wins > computer_wins:
		print('Congrats, you won!!!')
	else:
		print("Oh no :(  The computer won")

