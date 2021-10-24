def palindrome(s):
	if (not isinstance(s,str)): return "Invalid Input"
	if (len(s)==0): return True
	if (len(s)==1): return True
	if (s[0]!=s[-1]): return False
	return palindrome(s[1:-1])

print("palindrome(650):")
print(palindrome(650))

print('''\npalindrome("kayak"):''')
print(palindrome("kayak"))

print('''\npalindrome("hello"):''')
print(palindrome("hello"))
