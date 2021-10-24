def remove_punct(s):
	# check that s is a string
	if (not isinstance(s, str)): return("Invalid Input")
	punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
	result = ""
	# iterate through characters in string
	for char in s:
		if not (char in punctuations):
			result += char
	return result


input = "Hello in 36-650,& other MSP courses."
print('''remove_punct("Hello in 36-650,& other MSP courses."):''')
print(remove_punct(input))	

print('''\nremove_punct(""):''')
print(remove_punct(""))

print("\nremove_punct(650):")
print(remove_punct(650))
