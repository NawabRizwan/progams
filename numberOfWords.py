def numberOfWords(string):
	ls = string.split(" ");
	return len(ls)
f = open("textfile.txt","r")
contents = f.read()

print(""+str(numberOfWords(contents)))