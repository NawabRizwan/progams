'''python program that takes a number FROM the fibonacci series as 
input and prints the sum of fibonacci sequence  upto that number''' 
n = int(input("Enter a number from the fibonacci series"))
t1 = 0
t2 = 1
sum = 1;
nextNum = 0;
if n == 0 or n == 1:
	print(str(n))
else:
	while nextNum < n:
		nextNum = t1+t2;
		sum += nextNum;
		t1 = t2;
		t2 = nextNum
	print(str(sum))
