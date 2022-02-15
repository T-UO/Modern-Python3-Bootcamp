# nested_list = [[1,2,3], [4,5,6],[7,8,9]]

# nested_list[0][1]

# nested_list[1][-1]

# for 1 in nested_list:
#	for val in 1:
#		print(val)


# coords = [[10.423,9.132],[37.212,-14.092],[21.367,32.572]]
# for loc in coords:
#	for coord in loc:
#		print(coord)

# Nested List Comprehension

# nested_list = [[1,2,3], [4,5,6],[7,8,9]]

# board = [[num for num in range(1,4)] for val in range(1,4)]

# print(board)

[["X" if num%2 != 0 else "O" for num in range(1,4)] for val in range(1,4)]