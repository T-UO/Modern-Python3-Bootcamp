'''

class BankAccount:


	def __init__(self, owner, balance = 0):

		self.owner = ""

	def deposit(self, amount = 0):

		old_balance = self.balance
		new_balance = old_balance + amount	
		return new_balance

	def withdraw(self, reduction_amount = 0):

		new_balance = self.balance - reduction_amount
		return new_balance

'''



# class User:

# 	active_users = 0 # to define a class attribute, don't user "self"

# 	@classmethod
# 	def display_active_users(cls):
# 		return f"There are currently {cls.active_users} active users"

# 	@classmethod
# 	def from_string(cls, data_str):
# 		first, last, age = data_str.split(",")
# 		return cls(first, last, age)

	

# 	def __init__(self, first, last , age):
# 		self.first = first # attribute
# 		self.last = last # attribute
# 		self.age = age # attribute
# 		User.active_users += 1

# 	def logout(self):
# 		User.active_users -= 1
# 		return f"{self.first} has logged out"

# 	def full_name(self): # becomes a mehtod because we are adding it to an object
# 		return f"{self.first} {self.last}"

# 	def initials(self):
# 		return f"{self.first[0]}.{self.last[0]}."

# 	def likes(self, thing):
# 		return f"{self.first} likes {thing}"

# 	def is_senior(self):
# 		return self.age >= 65

# 	def birthday(self):
# 		self.age += 1
# 		return f"Happy {self.age}th, {self.first}"

# class Moderator(User):
# 	def __init__(self, first, last, age, community):
# 		super().__init__(first, last, age)
# 		self.community = community

# 	def remove_post(self):
# 		return  f"{self.full_name} removed a post from the {self.community}"

# jasmine = Moderator("Jasmine", "O'conner", 61, "Piano")
# u1 = User("Tom", "Garcia", 35)
# print(jasmine.full_name())
# print(jasmine.community)


#	user1 = User("Joe", "Smith", 68)
#	user2 = User("Blanca", "Lopez", 41)
#	print(User.display_active_users)
#	user1 = User("Joe", "Smith", 68)
#	user2 = User("Blanca", "Lopez", 41)
#	print(User.display_active_users)

# tom = User.from_string("Tom, Jones, 89")
# print(tom.first)
# print(tom.full_name())
#	User("Sue, Prichet, 12")

'''


'''


# value = ['2','3','4','5','6','7','8','9','10','Jack','King','Queen','Aces']
# suit = ['Clubs', 'Hearts', 'Diamonds', 'Spades']
# Deck = []

# for i in value:
# 	for y in suit:
# 		Deck = [i,"of",suit]
# 		print(Deck)

		

'''
class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		if age >= 0:
			self._age = age
		else:
			self._age = 0

	# def get_age(self):
	# 	return self._age

	# def set_age(self, new_age):
	# 	if new_age >= 0:
	# 		self._age = new_age
	# 	else:
	# 		self._age = 0

	@property  # decorator that alters how function works
	def age(self): # method now allows us to use print(jane.age) as if it was an attribute
		return self._age

	@age.setter
	def age(self, value):
		if value >= 0:
			self._age = value
		else:
			raise ValueError("age can't be negative")

	@property
	def full_name(self):
		return f"{self.first} {self.last}"

	@full_name.setter
	def full_name(self, name):
		self.first, self.last = name.split(" ")
	
	

jane = Human("Jane", "Goodall", 34)
# print(jane.get_age())
# jane.set_age(45)
print(jane.age)
jane.age = 20
print(jane.age)
print(jane.full_name)
jane.full_name = "Tim Minchin"
print(jane.full_name)
'''




# def week():
#     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     for i in days:
#     	while i <= len(days):
#     		yield i


'''
from functools import wraps
from time import time

def speed_test(fn):
	def wrapper(*args, **kwargs):
		start_time = time()
		result = fn(*args, **kwargs)
		end_time = time()
		print(f"Time Elapsed: {end_time - start_time}")
		return result
	return wrapper

@speed_test
def sum_nums():
	return sum(x for x in range(1000000))

print(sum_nums())
'''


# a way to ensure no keyword arguments are inserted
from functools import wraps

def ensure_no_kwargs(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		if kwargs:
			raise ValueError("No kwargs allowed! sorry :( ")
		return fn(*args, **kwargs)
	return wrapper

@ensure_no_kwargs
def greet(name):
	print(f"hi there {name}")

greet("Tony")



a = 14
b = 4
print(b and a)
print(b & a)





