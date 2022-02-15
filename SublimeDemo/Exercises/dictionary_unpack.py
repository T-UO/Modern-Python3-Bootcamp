def display_names(first, second):
	print(f"{first} says hello to {second}")

names = {"first": "Colt", "second": "Rusty"}

# display_names(first = "Charlie", second = "Sue")
display_names(**names)

def add_and_multiply_numbers(a,b,c):
	print(a+b+c)

data = dict(a=1, b=2, c=3)

add_and_multiply_numbers(**data)