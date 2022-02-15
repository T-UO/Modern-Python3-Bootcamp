# Scope
# Variables created in functions are scoped in that function
# Variables outside of a function are callled global functions
# Not a good idea to use global variables


# If i want to manipulate a variable that is not defined inside the function, but is inside the scope I have to tell python what I'm referring to when i declare thee variable

total = 0

def increment():
	global total
	total +=1
	return total
print(increment())

# nonlocal
# nonlocal lets us modify a parent's variables in a child (aka nested) function

def outer():
	count =- 0
	def inner():
		nonlocal count
		count += 1
		return count
	return inner()
