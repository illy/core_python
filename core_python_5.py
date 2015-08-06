#!/usr/bin/env python

import re
import random

# Exercise 5-2

def product(a, b):
	result = a*b
	print result
	return result


# Exercise 5-3

def grade1(num):
	if 90 <= num <= 100:
		return 'A'
	elif 80 <= num <= 89:
		return 'B'
	elif 70 <= num <= 79:
		return 'C'
	elif 60 <= num <= 69:
		return 'D'
	else:
		return 'F'


def grade2(score):
	g_dic = {'A': range(90, 101), 'B': range(80, 90), 'C': range(70, 80), 'D':range(60, 70), 'F':range(0, 60)}
	for grade, scores in g_dic.items():
		if score in scores:
			print grade


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


def convert_coin2(input):
	if input < 5:
		return str(input) + 'cents'
	elif 5 <= input < 10:
		nickel, cent = divmod(input, 5)
		return '%s nickel %s cents' %(nickel, cent)
	elif 10 <= input < 25:
		dime, remain = divmod(input, 10)
		nickel, cent = divmod(remain, 5)
		return ' %s dimes %s nickel %s cents' %(dime, nickel, cent)
	elif 25 <= input < 100:
		quater, remain = divmod(input, 25)
		dime, remain2 = divmod(remain, 10)
		nickel, cent = divmod(remain2, 5)
		return '%s quaters %s dimes %s nickel %s cents' %(quater, dime, nickel, cent)
	

def convert_coin3(input_):
	quater, remain1 = divmod(input_, 25)
	dime, remain2 = divmod(remain1, 10)
	nickel, cent = divmod(remain2, 5)
	if quater > 0: 
		return '%s quaters %s dimes %s nickel %s cents' %(quater, dime, nickel, cent)
	elif quater == 0 and dime > 0:
		return ' %s dimes %s nickel %s cents' %(dime, nickel, cent)
	elif quater == 0 and dime == 0 and nickel > 0:
		return '%s nickel %s cents' %(nickel, cent)
	elif quater == 0 and dime == 0 and nickel == 0:
		return '%s cents' %(cent)


# Exercise 5-6

def calculate1(input):
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

def calculate2(input):
	N1, OP, N2 = input.split(' ')
	N1, N2 = float(N1), float(N2)

	cal_dict = {'add': ('addition: ' + str(N1 + N2)), 'substract': ('substraction: ' + str(N1-N2)), 
				'multiply': ('multiplication: ' + str(N1 * N2)), 'divide': ('division: ' + str(N1/N2)), 
				'module': ('moduls: ' + str(N1%N2)), 'exponentiate': ('exponentiation: ' + str(N1**N2))}
	return cal_dict[OP] if cal_dict.has_key(OP) else "can't calculate."



# Exercise 5-7

def sales_tax(raw):
	return raw * 0.2

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
	for i in range(0, 21):
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

def


# Exercise 5-13

time = re.compile('((\d*)hour(s)?)?((\d*)min(s)?)?')

def time_in_min1(input):
	result = list(time.search(input).groups())
	if result[1] == None:
		result[1] = 0
	elif result[4] == None:
		result[4] = 0
	return str(int(result[1]) * 60 + int(result[4])) + 'mins'


def time_in_min2(input):
	_, hours, _, _, mins, _ = list(time.search(input).groups())
	if hours == None:
		hours = 0
	elif mins == None:
		mins = 0
	return '%smins' %(int(hours) * 60 + int(mins))


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
		max_common = min(n1, n2) if diff % min(n1, n2) == 0
	return max_common


def cal_gcd6(n1, n2):
	n1, n2, diff = max(n1, n2), min(n1, n2), abs(n1-n2)
	if n1%n2==0:
		return n2
	else:
		while diff > 0:
			if n1 % diff == 0:
				return diff
			else:
				n1, n2 = n1-diff, divmod(n1, diff)[1]
			diff = n1 - n2


def cal_gcd7(n1, n2):
	n1, n2 = max(n1, n2), min(n1, n2)
	while n2 > 0:
		if n1 % n2 == 0:
			return n2
		else:
			n1, n2 = n2, n1%n2


def cal_gcd8(n1, n2):
	n1, n2 = max(n1, n2), min(n1, n2)
	return n2 if n1%n2 == 0 else cal_gcd8(n2, n1%n2)


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
	return '%s   $%s   $%s' %(i, payment, balance)


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


#############################################################

def cal_lcm(n1, n2):
	p, n1, n2 = n1*n2, max(n1, n2), min(n1, n2)
	while n2 > 0:
		if n1 % n2 == 0:
			return p/n2
		else:
			n1, n2 = n2, n1%n2


def cal_point(p_dict, j=0):
	result = []
	initial = p_dict.keys()[j]
	for k in p_dict[initial]:
		if k not in result:
			result.append(k)
			for m in result:
				initial = m
	return p_dict.keys()[j], result

def cal_point(p_dict, j=0):
	result, initial, i = [], p_dict.keys()[j], 0
	while i < len(p_dict.keys()):
		result.extend(list(p_dict[initial]))
		for k in result:
			initial = k
		i += 1
	return p_dict.keys()[j], set(result)


def cal_points(p_dict):
	result = []
	for m in range(len(p_dict.keys())):
		result.append(cal_point(p_dict, m))
	return result


def cal_point(p_dict, j=0):
    i, result = 0, []
    while i < len(p_dict.keys()):
        initial = p_dict.keys()[i]
        for k in p_dict[initial]:
            if k != p_dict.keys()[j] and k not in result:
                    result.append(k)
        for m in result:
                initial = m
        i += 1
    return p_dict.keys()[j], result


	