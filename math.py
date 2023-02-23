from math import sqrt

def absolute_value(n):
	if n > 0:
		return n
	else:
		return n * -1
		
def cubed(n):
	return n * n * n
	
def exponentiate(x,y):
	return x**y

def get_primes_below(limit):
	primes = []
	for number in range(2, limit + 1):
		isPrime = True
		for k in range(2, int(sqrt(number) + 1)):
			if number % k == 0:
				isPrime = False
		if isPrime:
			primes.append(number)
	return primes
	
print(get_primes_below(999))
	
'''	
base = 5
for i in range(-10,101):
	print(f"{base} ^ {i} = {exponentiate(base, i)}")
	
for i in range(1,87):
	print(f'{i}^3 = {cubed(i)}')
			
for i in range(-5,6):
	print(f"|{i}| = {absolute_value(i)}")
		
b = subtract_three(3)
print(f"The value of b is {b}")
	
a = add_seven(10)
print(f"The value of a is {a}")
'''
