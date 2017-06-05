def is_palindrome(string):
	string = string.casefold();
	for i,char in enumerate(string):
		if char !=string[-i-1]:
			return False
	return True

if(is_palindrome('Racaecar')):
	print("palindrome")
else:
	print("Not palindrome")
