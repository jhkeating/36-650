def transpose(m):
	# check matrix has at least one row
	if (len(m)==0): return "Invalid Input"
	# check matrix has at least one column
	elif (len(m[0])==0): return "Invalid Input"
	result = []
	# iterate through columns
	for c in range(len(m[0])):
		new_row = []
		# iterate through rows
		for r in range(len(m)):
			new_row.append(m[r][c])
		result.append(new_row)
	return result

X = [[10,8], [2,4], [1,7]]
print("transpose([[10,8],[2,4],[1,7]]):")
print(transpose(X))

print("\ntranspose([]):")
print(transpose([]))
			
