def fizzbuzz(number):
	for i in range(1,number+1):
		if i%3 == 0 and i%5 == 0:
			print(str(i)+" FizzBuzz")
		else:
			if i%3 == 0:
				print(str(i)+" Fizz")
			if i%5 == 0:
				print(str(i)+" buzz")
fizzbuzz(20)
