class User:

	active_users = 0 # to define a class attribute, don't user "self"

	def __init__(self, first, last , age):
		self.first = first # attribute
		self.last = last # attribute
		self.age = age # attribute
		User.active_users += 1

	def logout(self):
		User.active_users -= 1
		return f"{self.first} has logged out"

	def full_name(self): # becomes a mehtod because we are adding it to an object
		return f"{self.first} {self.last}"

	def initials(self):
		return f"{self.first[0]}.{self.last[0]}."

	def likes(self, thing):
		return f"{self.first} likes {thing}"

	def is_senior(self):
		return self.age >= 65

	def birthday(self):
		self.age += 1
		return f"Happy {self.age}th, {self.first}"

	def say_hi(self):
		print("Hello!!!")

print(User.active_users)
user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(User.active_users) # refer to the class name by using the class name as the prefix
print(user2.logout())
print(User.active_users)
