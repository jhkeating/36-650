def one_away(s1,s2):
	# check s1 and s2 are both strings
	if (not isinstance(s1,str)): return "Invalid Input"
	if (not isinstance(s2,str)): return "Invalid Input"
	# zero edits
	if (s1==s2): return True
	n1 = len(s1)
	n2 = len(s2)
	# replace character
	if (n1==n2): 
		return replaced(s1,s2)
	if (abs(n1-n2)!=1): return False
	if (n1<n2): 
		return removed(s2,s1)
	return removed(s1,s2)
	
def replaced(s1,s2):	
	# checks if replacing one character in s1 makes it equal s2
	num_diffs = 0
	for i in range(len(s1)):
		if (s1[i]!=s2[i]):
			num_diffs += 1
	if (num_diffs==1): return True
	return False

def removed(s1,s2):
	# checks if removing one character in s1 makes it equal s2
	for i in range(len(s1)):
		remove_i = s1[0:i]+s1[i+1:len(s1)]
		if (remove_i==s2): return True
	return False

print('''one_away("pale","ple"):''')
print(one_away("pale","ple"))

print('''\none_away("pales","pale"):''')
print(one_away("pales","pale"))

print('''\none_away("pale","bale"):''')
print(one_away("pale","bale"))

print('''\none_away("pale","bake"):''')
print(one_away("pale","bake"))





