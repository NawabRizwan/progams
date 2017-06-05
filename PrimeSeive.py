def PrimeSeive(n):
	primes = []
	for i in range(2,n+1):
		if i not in primes:
			print(i)
			for j in range(i*i,n+1,i):
				primes.append(j)

PrimeSeive(100)
		
