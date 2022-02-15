# a function is a process for executing a task
# it can accept input and return output
# a useful way for executing similar procedures over and over

# stay Dry - Don't Repeat Yourself

# defining functions

# def name_of_function():
	# block of runnable code

def sing_happy_birthday(name):
	print("Happy Birthday To You")
	print("Happy Birthday To You")
	print(f"Happy Birthday Dear You{name}")
	print("Happy Birthday To You")
sing_happy_birthday('Tagbo')

#	sing_happy_birthday()
#	sing_happy_birthday()
#	sing_happy_birthday()

#	def print_square_of_7():
#		print(7**2)

#	print_square_of_7()

#	def square_of_7():
#		return 7**2
#	result = square_of_7() # return exits the function
#	print(result)

def exponent(num, power=2):
	return num ** power
print(exponent(2,3))
print(exponent(3))
print(exponent(7))

# Parameters vs. Arguments
# Parameters refer to the variable in a method definition
# When a method is called, the arguments are the data you pass into the method's parameters
# Parameter is variable in the declaration of function
# Default parameter should go at the end

# parameters can be other functions

#########

def add(a,b):
 	return a+b

def math(a,b, fn = add):
	return fn(a,b)

def subtract(a,b):
	a-b

math(2,2)

math(2,2,subtract)

#########


# Keyword Arguments
# You can use Keyword arguments to directly specify within the function call

def full_name(first,last):
	return "Your name is {first} {last}"

full_name(first = 'Colt', last = 'Steele') # Your name is Colt Steele

full_name(last = 'Steele', first = 'Colt') # Your name is Colt Steele


def exponent(num, power=2):
	return num ** power

print(exponent(2,3))
print(exponent(3))
print(exponent(7))

print(exponent(power = 3, num = 4))



# Documenting Functions
# Use triple-double quotes

def say_hello():
	""" A simple function that returns the string hello:"""
	return "Hello!"
say_hello.__doc__

