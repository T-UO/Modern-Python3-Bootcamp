''' 1. parameters 2. *args 3. default parameters 4. **kwargs '''

def display_info(a,b, *args, instructor = "Colt", **kwargs):
	return [a, b, args, instructor, kwargs]

print(display_info(1,2,3, last_name = "Steele", job = "instructor"))

# a - 1
# b - 2
# args (3)
# instructor - "Colt"
# kwargs - {"last_name": "Steele": "job", "instructor"}


def sum_all_values(*args):
	total = 0
	for num in args:
		total += num
	print(total)
# sum_all_values(1,30,2,5,6)

nums = [1,2,3,4,5,6]
sum_all_values(nums)