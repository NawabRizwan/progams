def numberOfVowels(string):
	a = 0
	e = 0
	i = 0
	u = 0
	o = 0
	num = 0
	for char in string:
		if char == 'a' or char == 'A':
			num += 1
			a += 1
		elif char == 'e' or char == 'E':
			num += 1
			e += 1
		elif char == 'i' or char == 'I':
			num += 1
			i += 1
		elif char == 'o' or char == 'O':
			num += 1
			o += 1
		elif char == 'u' or char == 'U':
			num += 1
			u += 1
	print("number of vowels = "+str(num))
	print("a = "+str(a)+" e = "+str(e)+" i = "+str(i)+" o = "+str(o)+" u = "+str(u))
numberOfVowels("My name is Rizwan Nawab")
