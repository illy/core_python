

import re
import os
from datetime import datetime
from operator import add, sub, mul, floordiv
from random import randint, choice

# Exercise 11-3

def product(a, b):
	return a+b, a*b

# Exercise 11-3

def max2(n1, n2):
	return n1 if n1 > n2 else n2


def min2(n1, n2):
	return n1 if n1 < n2 else n2


def my_max(l):
	return reduce(lambda x, y: max2(x, y), l)


def my_min(l):
	return reduce(lambda x, y: min2(x, y), l)


# Exercise 11-4

time = re.compile('(\d*)(?:min(s))')

def min_hour(mins):
	mins = time.search(mins).group(1)
	hours, mins = divmod(int(mins), 60)
	return '%shour(s) and %smin(s)' %(hours, mins)

# Exercise 11-5

def tax(base, rate=0.2):
	return base*rate

# Exercise 11-6

def printf(value, *values):
	print '%s %s' %(value, values)


# Exercise 11-7

nums = [1, 2, 3]
alphas = ['abc', 'def', 'ghi']

def mapping1(x, y):
	return zip(x, y)


# Exercise 11-8

def leapyear(year):
	if year % 4 == 0 and year % 100 != 0:
		return True
	elif year % 400 == 0:
		return True
	else:
		return False


def filter_leap1(years):
	return filter(leapyear, years)


def filter_leap2(years):
	return [y for y in years if leapyear(y)]


# Exercise 11-9

def average(x):
	return reduce((lambda m, n: m+n), x)/float(len(x))


# Exercise 11-11

def clean1(f_name, new_file=True):
	result = []
	with open(f_name, 'r') as f:
		for line in f.readlines():
			result.append(line.strip())
	if new_file = True:
		with open('new_file', 'w') as new:
			new.write(result)
	else:
		with open(f_name, 'w') as old:
			old.write(result)


def map_remove(x):
	return map(lambda x: x.strip(), x)


def clean2(f_name, new_file=True):
	result = []
	with open(f_name, 'r') as f:
		for line in f.readlines():
			result.append(map_remove(line))
	if new_file = True:
		with open('new_file', 'w') as new:
			new.write(result)
	else:
		with open(f_name, 'w') as old:
			old.write(result)


# Exercise 11-12

def testit(func, *nkwargs, **kwargs):
	try:
		retval = func(*nkwargs, **kwargs) 
		result = (True, retval)
	except Exception, diag:
		result = (False, str(diag))
	return result


def test():
	funcs = (int, long, float)
	vals = (1234, 12.34, '1234', '12.34')
	for eachFunc in funcs: 
		print '-' * 20
	
		for eachVal in vals:
			retval = testit(eachFunc, eachVal)
			
			if retval[0]:
				print '%s(%s) =' % (eachFunc.__name__, `eachVal`), retval[1] 
			else:
				print '%s(%s) = FAILED:' % (eachFunc.__name__, `eachVal`), retval[1]


def timeit(func, *nkwargs, **kwargs):
	try:
		begin = datetime.now()
		retval = func(*nkwargs, **kwargs)
		end = datetime.now()
		duration = end - begin
		result = (True, retval, duration.total_seconds())
	except Exception, diag:
		result = (False, str(diag))
	return result


def timethem():
	funcs = (int, long, float)
	vals = (1234, 12.34, '1234', '12.34')
	for eachFunc in funcs: 
		print '-' * 20
	
		for eachVal in vals:
			retval = timeit(eachFunc, eachVal)
			
			if retval[0]:
				print '%s(%s) =' % (eachFunc.__name__, `eachVal`), retval[1], '%sseconds' %retval[2]
			else:
				print '%s(%s) = FAILED:' % (eachFunc.__name__, `eachVal`), retval[1]


# Exercise 11-13

def mult(x, y):
	return x*y

def factorial1(m):
	return 1 if m == 1 else reduce(lambda x, y: mult(x,y), range(2, m+1))

def factorial2(m):
	return 1 if m == 1 else reduce(lambda x, y: x*y, range(2, m+1))

# Exercise 11-14

def fibonacci1(n):
	if n == 1 or n == 2:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

## Exercise 11-15

def print_char1(input_):
	result1, result2 = [], []
	for char in input_:
		result1.append(char)
	for char in input_[::-1]:
		result2.append(char)
	return 'forward: %s, backward: %s'  %(''.join(result1), ''.join(result2))


# Exercise 11-16

ops = {'+': add, '-': sub, '*': mul, '/': floordiv}
MAXTRIES = 2

def doprob():
	op = choice('+-*/')
	nums = [randint(1,10) for i in range(2)] 
	nums.sort(reverse=True)
	ans = ops[op](*nums)
	pr = '%d %s %d = ' % (nums[0], op, nums[1]) 
	oops = 0
	while True:
		try:
			if int(raw_input(pr)) == ans:
				print 'correct'
				break
			if oops == MAXTRIES:
				print 'answer\n%s%d'%(pr, ans) 
			else:
				print 'incorrect... try again'
				oops += 1
		except (KeyboardInterrupt, EOFError, ValueError):
			print 'invalid input... try again'

def main(): 
	while True:
		doprob()
		try:
			opt = raw_input('Again? [y]').lower() 
			if opt and opt[0] == 'n':
				break
		except (KeyboardInterrupt, EOFError):
			break

def counter(start_at=0): 
	count = [start_at]
	def incr(): 
		count[0] += 1
		return count[0] 
	return incr


# Exercise 11-19

j,k=1,2

def proc1():
	j,k=3,4
	print "j == %d and k == %d" % (j, k) 
	k=5

def proc2():
	global j
	j=6
	proc1()
	print "j == %d and k == %d" % (j, k)

k = 7
proc1()
print "j == %d and k == %d" % (j, k)

j = 8
proc2()
print "j == %d and k == %d" % (j, k)