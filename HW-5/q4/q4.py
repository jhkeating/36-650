def triangle(r):
	if (not isinstance(r, int)): return "Invalid Input"
	if (r<0): return "Invalid Input" 
	current_row = 0
	current_val = 0
	result = ""
	while (current_row < r):
		current_row += 1
		for i in range(current_row):
			current_val += 1
			result += str(current_val) + " "
		result += "\n"
	return result[:-1]

print("triangle(-3)")
print(triangle(-3))

print("\ntriangle(2.5)")
print(triangle(2.5))

print("\ntriangle(1):")
print(triangle(1))

print("\ntriangle(3):")
print(triangle(3))

print("\ntriangle(6):")
print(triangle(6))
