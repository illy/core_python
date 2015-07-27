#!/usr/bin/env python

import re
import random

# Exercise 5-2

def product(a, b):
	result = a*b
	print result
	return result


# Exercise 5-3

def grade(num):
	if 90 <= num <= 100:
		result = 'A'
	elif 80 <= num <= 89:
		result = 'B'
	elif 70 <= num <= 79:
		result = 'C'
	elif 60 <= num <= 69:
		result = 'D'
	else:
		result = 'F'
	return result


# Exercise 5-4

def leapyear(year):
	if year % 4 == 0 and year % 100 != 0:
		return True
	elif year % 400 == 0:
		return True
	else:
		return False


# Exercise 5-5

def convert_coin(input):
	if input < 5:
		return str(input) + 'cents'
	elif 5 <= input < 10:
		return str(divmod(input, 5)[0]) + 'nickel ' + str(divmod(input, 5)[1]) + 'cents'
	elif 10 <= input < 25:
		return str(divmod(input, 10)[0]) + 'dimes ' + str(divmod(divmod(input, 10)[1], 5)[0]) + 'nickel '  + str(divmod(divmod(input, 10)[1], 5)[1]) + 'cents'
	elif 25 <= input < 100:
		return str(divmod(input, 25)[0]) + 'quaters ' + str(divmod(divmod(input, 25)[1], 10)[0]) + 'dimes ' + str(divmod(divmod(divmod(input, 25)[1], 10)[1], 5)[0]) \
		+ 'nickel ' + str(divmod(divmod(divmod(input, 25)[1], 10)[1], 5)[1]) + 'cents'
	

# Exercise 5-6

def calculate(input):
	N1, OP, N2 = input.split(' ')
	N1, N2 = float(N1), float(N2)
	if OP == 'add':
		return 'addition: ' + str(N1 + N2)
	elif OP == 'substract':
		return 'substraction: ' + str(N1-N2)
	elif OP == 'multiply':
		return 'multiplication: ' + str(N1 * N2)
	elif OP == 'divide':
		return 'division: ' + str(N1/N2)
	elif OP == 'module':
		return 'moduls: ' + str(N1%N2)
	elif OP == 'exponentiate':
		return 'exponentiation: ' + str(N1**N2)
	else:
		return "can't calculate"


# Exercise 5-8

def square_cube(input):
	return input ** 2, input ** 3

def circle_sphere(input):
	return input * 3.14, round(3.14 * (4.0/3) * (input**3), 2)

# Exercise 5-10

def f2c(input):
	return round((input-32) * (5/9.0), 1)

def c2f(input):
	return round(input * (9.0/5) + 32, 1)

# Exercise 5-11

def evens_in_20():
	result = []
	for i in range(0, 20):
		if i%2 == 0:
			result.append(i)
	return result

def odds_in_20():
	result = []
	for i in range(0, 20):
		if i%2 != 0:
			result.append(i)
	return result

def evaluate(n1, n2):
	return True if n1%n2 == 0 else False


# Exercise 5-13

time = re.compile('(\d*)hour(s)?(\d*)min(s)?')

def time_in_min(input):
	result = time.search(input).groups()
	return str(int(result[0]) * 60 + int(result[2])) + 'mins'


# Exercise 5-14

def cal_interest(CD, APY):
	return CD * (1+APY)**365

# Exercise 5-15

def cal_gcd1(n1, n2):
	divisor1, common_divisors = [], []
	i = 1
	while i <= n1:
		if n1 % i == 0:
			divisor1.append(i)
		i += 1

	for j in divisor1:
		if n2 % j == 0:
			common_divisors.append(j)
			
	return max(common_divisors)

def cal_gcd2(n1, n2):
	common_divisors = []
	i = 1
	while i <= min(n1, n2):
		if n1 % i == 0 and n2 % i == 0:
			common_divisors.append(i)
		i += 1
	return max(common_divisors)

def cal_gcd3(n1, n2):
	up_limit = min(n1, n2)
	for i in range(up_limit, 0, -1):
		if n1 % i == 0 and n2 % i == 0:
			break
	return i

def cal_gcd4(n1, n2):
	up_limit = min(n1, n2)
	while up_limit > 0:
		if n1 % up_limit == 0 and n2 % up_limit == 0:
			break
		up_limit -= 1
	return up_limit

def cal_gcd5(n1, n2):
	diff = abs(n1-n2)
	if diff > min(n1, n2):
		max_common = diff if min(n1, n2) % diff == 0 else divmod(min(n1,n2), diff)[1]
	else:
		max_common = min(n1, n2) if diff % min(n1, n2) == 0 else

def cal_lcm1(n1, n2):
	mltp1, lcm = [], 0
	for i in range(1, n2+1):
		mltp1.append(n1*i)
	for j in mltp1:
		if j % n2 == 0:
			lcm = j
			break
	return lcm

def cal_lcm2(n1, n2):
    n1, n2 = min(n1, n2), max(n1, n2)
    c = n2
    while c <= n1*n2:
        if c%n1 ==0: 
        	break
        c += n2
    return c

# Exercise 5-16

def cal_payment(balance):
	payment, i = int(raw_input()), 0
	while balance > 0:
		balance = balance - payment
		i += 1

	print '%s   $%s   $%s' %(i, payment, balance)


# Exercise 5-17

def randrandrand():
	rand_list, result = [], []
	i, j = 0, 0
	time1, time2 = random.randint(1, 100), random.randint(1, 100)
	while i <= time1:
		rand_list.append(random.randrange(0, 2**31-1))
		i += 1
	while j <= time2:
		result.append(random.choice(rand_list))
		j += 1
	return result

