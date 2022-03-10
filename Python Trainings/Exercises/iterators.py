# iterator
# an iterator is an object that can be iterated upon
# An object which returns data, one element at a time when next() is called on it

# iterable is an object will return an iterator when iter() is called on it
# For example, "Hello" is an iterable, but it is not an iterator

# When next() is called on an iterator, the iterator returns the next item. It keeps doing so until it raises a StopIteration error

# Defining a custom for loop

# for num in [1,2,3]
# for char in "hi there"

def my_for_(iterable, func):
	iterator = iter(iterable)
	while True:
		try:
			thing = next(iterator)
		except StopIteration:
			break
		else:
			func(thing)

my_for_("lol", print)

# Defining custom iterators

class Counter:
	def __init__(self, low, high):
		self.current = low
		self.high = high

	def __iter__(self):
		return self

	def __next__(self):
		if self.current < self.high:
			num = self.current
			self.current += 1
			return num
		raise StopIteration



for x in Counter(50,70):
	print(x)








































