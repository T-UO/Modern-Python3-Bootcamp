# Generators are iterators
# Generators can be created with generator fucntions
# Generator functions use the yield keyword
# Generators can be created with generator expressions

# def count_up_to(max):
# 	count = 1
# 	while count <= max:
# 		yield count # yield will return the value of count and then pause
# 		count += 1


# counter = count_up_to(5)

# while True:
# 	print(counter)
# print(next(counter))
# print(next(counter))


def current_beat():
	max = 100
	nums = (1,2,3,4)
	i = 0
	result = []
	while len(result) < max:
		result.append(nums[i])
		i += 1










































