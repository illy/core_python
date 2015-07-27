#!/usr/bin/env python

import keyword
import string
import datetime

# Exercise 6-2

alphas = string.ascii_letters + '_'
nums = string.digits

def id_checker(myInput):
	if myInput[0] not in alphas:
		print '''invalid: first symbol must be alphabetic'''
	elif len(myInput) > 1:
		if myInput in keyword.kwlist:
			print '''invalid: the identifier is a keyword'''
		else:
			for otherChar in myInput[1:]:
				if otherChar not in alphas + 		nums: 
					print '''invalid: remaining symbols must be alphanumeric'''
					break 
			else:
				print "okay as an identifier"

# Exercise 6-3

def reversed_sort1(num_list):
	return sorted(num_list)[::-1]

def reversed_sort2(num_list):
	return [i for i in reversed(sorted(num_list))]

# Exercise 6-4

def grade(score_list):
	results, i, scores = [], 0, 0
	for num in score_list:
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
		results.append(result)
		scores += num
		i += 1
	average = scores / i
	return results, average

# Exercise 6-5

def print_char(input):
	for char in input:
		print 'forward', char
	for char in input[::-1]:
		print 'backwrad', char

def compare_str(str1, str2):
	str1, str2 = str1.lower(), str2.lower()
	i = 0
	if str1 == str2:
		print 'the same'
	elif len(str1) != len(str2):
		print 'not the same'
	else:
		while i < len(str1):
			if str1[i] != str2[i]:
				print 'not the same'
				break
			i +=1
			
def is_palindromic(string):
	i = 0
	while i < len(string):
		if string[i] == string[::-1][i]:
			print 'palindromic'
		i += 1

def make_palindromic1(string):
	return string + string[::-1]

def make_palindromic2(string):
	return ''.join((string, string[::-1]))

# Exercise 6-6

def string_strip(input):
	output = []
	for i in input:
		if i not in string.whitespace:
			output.append(i)
	return ''.join(output)

def string_strip2(input):
	output = []
	for i in input:
		if i.isspace() == False:
			output.append(i)
	return ''.join(output)

def string_strip3(input):
	white = string.whitespace
	return input.translate(None, white)

# Exercise 6-7

def buggy():	
	num_str = raw_input('Enter a number: ') # Take the input as num_str	
	num_num = int(num_str) # convert num_str to integer
	non_fac_list = range(1, num_num+1) 
	print "BEFORE:", repr(non_fac_list)
	i, output = 0, []
	while i < len(non_fac_list):
		if num_num % non_fac_list[i] != 0:
			output.append(non_fac_list[i])
		i += 1
	print "AFTER:", output

# Exercise 6-8

def translate(num):
	num = str(num)
	result, result1, result2, result3 = '', '', '', ''
	l0 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	l1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	l2 = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninty']
	if 0 < int(num) < 1000:
		if len(num)==1:
			num = '000' + num
		elif len(num)==2:
			num = '00' + num
		elif len(num)==3:
			num = '0' + num

	for i in zip(l0, l1):
		if int(num[1]) == i[0]:
			result1 = i[1] + ' hundred and '
		if int(num[3]) == i[0]:
			result3 = i[1]
	for i in zip(l0, l2):
		if int(num[2]) == i[0]:
			result2 = i[1] + ' '
	result = result1 + result2 + result3
	print result

# Exercise 6-9

time = re.compile('(\d*)hour(s)?(\d*)min(s)?')

def time_in_min(input):
	result = time.search(input).groups()
	return str(int(result[0]) * 60 + int(result[2])) + 'mins'

time2 = re.compile('(\d*)min(s)?')

def time_in_hour(input):
	result = int(time2.search(input).group(1))
	hour, mins = divmod(result, 60)
	if hour == 0:
		return mins + 'mins'
	elif hour == 1:
		return '1 hour and %s mins' %mins
	else:
		return '%s hour and %s mins' %(hour, mins) 


# Exercise 6-10

def convert(input):
	i, result = 0, []
	while i < len(input):
		if input[i].isalpha():
			if input[i].islower():
				result.append(input[i].upper())
			else:
				result.append(input[i].lower())
		else:
			result.append(input[i])
		i += 1
	return ''.join(result)


# Exercise 6-12

def findchr(string,  char):
	i, result = 0, -1
	while i < len(string):
		if char == string[i]:
			result = i
			break
		i+=1
	return result
		
def rfindchr(string,  char):
	i, result = -1, -1
	while i >= -len(string):
		if char == string[i]:
			result = i + len(string)
			break
		i-=1
	return result

def subchr1(string, origchar, newchar):
	result = []
	for i in string:
		if i == origchar:
			i = newchar
		result.append(i)
	return ''.join(result)

def subchr2(string, origchar, newchar):
	result = ''
	for i in string:
		if i == origchar:
			i = newchar
		result += i
	return result


# Exercise 6-14

def rochambeau():
	input_ = raw_input()
	if input_ == 'rock' or input_ == 'paper' or input_ == 'scissors':
		if input_ == 'rock':
			input_ = 1
		elif input_ == 'paper':
			input_ = 2
		else:
			input_ = 3
		
		guess =	random.randint(1,3)
		print input_, guess
		result = input_ - guess

		if result == 2 or result == -2:
			result = -result

		if result > 0:
			print 'win'
		elif result == 0:
			print 'draw'
		else:
			print 'lose'
	else:
		input = raw_input()
		print 'please reinput'


# Exercise 6-15

format1 = '%d/%m/%y'
format2 = '%m/%d/%y'

def calculate_date(end, start):
	if datetime.datetime.strptime(start, format1) and datetime.datetime.strptime(end, format1):
		start, end = datetime.datetime.strptime(start, format1), datetime.datetime.strptime(end, format1)
	elif datetime.datetime.strptime(start, format2) and datetime.datetime.strptime(end, format2):
		start, end = datetime.datetime.strptime(start, format2), datetime.datetime.strptime(end, format2)
	return (end - start).days

def calculate_birth(birth):
	today = datetime.datetime.today()
	today = '/'.join((str(today.day), str(today.month), str(today.year)[2:4]))
	print today
	return calculate_date(today, birth)

def predict_birth(birth):
	if datetime.datetime.strptime(birth, format1):
		day, month, year = birth.split('/')
	elif datetime.datetime.strptime(birth, format2):
		month, day, year = birth.split('/')
	today = datetime.datetime.today()
	this_birth = '/'.join((str(day), str(month), str(today.year)[2:4]))
	next_birth = '/'.join((str(day), str(month), str(today.year+1)[2:4]))
	today = '/'.join((str(today.day), str(today.month), str(today.year)[2:4]))
	return calculate_date(this_birth, today) if calculate_date(this_birth, today) >= 0 else calculate_date(next_birth, today) 


# Exercise 6-16

def make_matrics(m, n):
	i, matrics = 0, []
	while i+1 <= n:
		matrics.append(tuple(random.sample(range(1, 100), m)))
		i += 1
	return matrics

def add_matrics(m , n):
	p, result = 0, []
	m1, m2 = make_matrics(m, n), make_matrics(m, n)
	l1 = (i for j in m1 for i in j)
	l2 = (i for j in m2 for i in j)
	l3 = [k[0] + k[1] for k in zip(l1, l2)]

	while p + m <= m*n:
		result.append(tuple(l3[p: p+m]))
		p += m
	return result

def multiple_matrics(m, n, p):
	k, result = 0, []
	m1 = make_matrics(m, n)
	l1 = [i*p for j in m1 for i in j]
	while k + m <= m*n:
		result.append(tuple(l1[k:k+m]))
		k += m
	return result


# Exercise 6-17:

def my_pop(input_list):
	return input_list[:-1]

# Exercise 6-19

def multi_output(input, col=3):
	i = 0
	while i + col <= len(input):
		print input[i:i+col]

		i += col


