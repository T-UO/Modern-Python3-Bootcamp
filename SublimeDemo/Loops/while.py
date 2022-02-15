# while loops

# while loops continue to execute while a certain condition is true

# user_repsone = None
# while user_repsone != "please":
#	user_repsone = input(" Ah ah ah, you didn't say the magic words: ")

# msg = input("What's the secret password? ")
# while msg != "bananas":
#	print("WRONG!")
#	msg = input("What's the secret password?")
# print("Correct!")


# for num in range(1,11):
#	print(num)

# num = 1
# while num < 11:
#	print(num)
#	num +=2


#for x in range(1,10):
#	print("\U0001f600" *x)

# times = 1
# while times < 11:
#	print("\U0001f600" * times)
#	times +=1	


# msg = input("Hey how's it going? ")

# while msg != 'stop copying me':
#	print(msg)
#	msg = input()


# Quiz 14, Question 3

#x = 0
#while x < 11:
#	x += 2
#	print(x)


# condition =1

# while condition < 10:
#	print(condition)
#	condition += 1


# Coding Exercise # 14

from random import randint

number = 0
i = 0 

while i != 5:
	number = randint(1,10)
	i += 1
	print(number)