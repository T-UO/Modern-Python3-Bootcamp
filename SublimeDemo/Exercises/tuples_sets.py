# tuples and sets
# tuple is an ordered collection or grouping of items; syntax is different from lists
# tuples are immutable; it cannot be changed
# i.e., numbers = 1,2,3,4
# tuples are faster than lists

months = ('January', 'Feburary', ' March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

locations = { (35.54, 84.28): 'Tokyo Office',
			( 40.73, 92.72): 'Nashville Office',
			(35.22, 28.84): 'New York Office'
			}

# you can use tuples as keys in a dictionary, but you can't use list as a key in a dcitionary

i = len(months) - 1

while i == 0:
	print(months(i))
	i -= 1

# count returns the # of times a value appears in a tuple
# index method returns the index at which a value is found
# you can have nested tuples
# you can use slices


# Sets
	# sets do not have duplicate values
	# Elements in sets aren't ordered
	# you cannot access items in a set by index

# Creating a set
s = {1,4,5} # doesn't include colon syntax like we would for creatinga dictionary

# you can access all items in a set using a for loop

cities = {'los angeles', 'boulder', 'tokyo', 'florence', 'santiago'}

print(set(cities))

# add items to a set

s = {1,2,3,4,}

# Set Math

math_students = {'Matthew', 'Helen', 'Prashant', 'James', 'Aparna'}
biology_students = {'Jane', 'Matthew', 'Charlotte' , 'Mesut', 'Oliver', 'James'}

# take the union of the sets

math_students | biology_students

# take the intersection of sets

math_students & biology_students






























