# Common Python Errors

# Syntax Error
# occurs when python encounters invalid syntax
# def first: # no parentheses after the name

# Name Error
# Occurs when a variable has not been defined or assigned

# TypeError
# An operation or function is applied to the wrong type
# 3 + s

# IndexError
# When you try to access an element in a list using an invalid index

# ValueError
# Occurs when a built-in operation or function receives an argument that has the right type but an inappropriate value
# int('f')

# KeyError
# When a dictionary doesn't have a specific key

# Raising our own errors


# raise ValueError('invalid value')

'''def colorize(text, color):
	colors = ('cyan', 'yellow','blue', 'green', 'magenta')
	if type(text) is not str:
		raise TypeError('text must be a string or instance of string')
	if color not in colors:
		raise ValueError('color is invalid color')
	print(f"Printed {text} in {color}")

colorize('hello', 'red')
colorize(35, 'hello')
'''

# Handle Errors

while True:
	try:
		num = int(input('please enter a number: '))
	except ValueError:
		print("that's not a number!")
	else:
		print("Good job! You entered a number!")
		break
	finally:
		print('Runs no matter what')
print("Rest of game logic")














































































