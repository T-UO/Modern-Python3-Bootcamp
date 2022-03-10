# instance methods

class User:
	def __init__(self, first, last , age):
		self.first = first # attribute
		self.last = last # attribute
		self.age = age # attribute

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

user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)

print(user1.first, user1.last, user1.age)
print(user2.first, user2.last, user2.age)

print(user2.full_name())
print(user1.likes("Ice Cream"))
print(user2.likes("Chips"))

print(user1.initials())
print(user2.initials())

print(user2.is_senior())
print(user1.birthday())

user1.say_hi()