def get_row(c,w):
	# returns row of width w containing c stars
	result = ""
	row_width = 2*c-1
	side_space = (w-row_width)//2
	# add spaces to left
	for i in range(side_space):
		result += " "
	# add stars
	for i in range(c-1):
		result += "* "
	result += "*"
	# add spaces to right
	for i in range(side_space):
		result += " "
	result += "\n"
	return result

def pyramid(r):
	if (not isinstance(r, int)): return "Invalid Input"
	if (r < 0): return "Invalid Input"
	width = 2*r-1
	current_row = 0
	result = ""
	while current_row < r:
		current_row += 1
		result += get_row(current_row,width)
	return result

print("pyramid(-3):")
print(pyramid(-3))

print("\npyramid(2):")
print(pyramid(2))

print("\npyramid(5):")
print(pyramid(5))

print("\npyramid(6):")
print(pyramid(6))
