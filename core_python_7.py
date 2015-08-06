#!/usr/bin/env python

import random
import timedate
import operator
from string import maketrans


# Exercise 7-3

def make_dict():
	return dict(enumerate(random.sample(range(1,100), random.randint(1, 10)), start=1))

def sorted_key1():
	return sorted(make_dict)

def sorted_key2():
	return sorted(make_dict.keys())

def sorted_dict():
	return sorted(make_dict.items())

def sorted_value1():
	d = make_dict()
	return sorted(d.items(), key=lambda d:d[1])

def sorted_value2():
	d = make_dict()
	return sorted(d.items(), key=operator.itemgetter(1))

# Exercise 7-4

l1 = [1, 2, 5, 6, 0]

l2 = ['a', 'g', 'c', 'f', 'f']

def twolist_dict(l1, l2):
	return dict(zip(l1, l2))


# Exercise 7-6

def crude_oil():
	i, result, oil_dict = 0, {}, {}
	while i < 10:
		ticker, share, purchase, current = raw_input('Please input a four-item list: ').split(',')
		ticker, share = ticker.translate(None, "'[] "), share.translate(None, "'[] ")
		purchase, current = purchase.translate(None, "'[] "), current.translate(None, "'[] ")
		oil_dict['ticker%s' %i] = (ticker, share, purchase, current)
		result.update(oil_dict)
		i +=1
	return result

# Exercise 7-7

def reverse_dict1(input_dict):
	return dict(zip(d.values(), d.keys()))

def reverse_dict2(input_dict):
	return dict(zip(d.itervalues(), d.iterkeys()))

# Exercise 7-8

def hr():
	i, result, name_dict = 0, {}, {}
	while i < 5:
		name, number = raw_input('Please input: ').split(',')
		name_dict = {}
		name_dict['name%s' %i] = (name, number)
		result.update(name_dict)
		i +=1
	return sorted(result.items(), key=itemgetter(1))


# Exercise 7-9

def tr1(srcstr, dststr, string):
	table = maketrans(srcstr, dststr)
	return string.translate(table)


def tr2(srcstr, dststr, string, case=True):
	i, result, temp = 0, '', []
	
	if case==True:
		table = maketrans(srcstr, dststr)
		result = string.translate(table)
	
	elif case == False:
		string1, srcstr1 = string.lower(), srcstr.lower()
		table = maketrans(srcstr1, dststr)
		string2 = list(string1.translate(table))
		
		while i < len(string2):
			if string2[i].upper() == string[i]:
				string2[i] = string2[i].upper()
			else:
			 	string2[i] = string2[i]
			temp.append(string2[i])
			i +=1
		result = ''.join(temp)
	
	return result


def tr3(srcstr, dststr, string):
	return string.replace(srcstr, dststr)

# Exercise 7-10

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
beta = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']

def rot13(input):
	alpha_upper, beta_upper = [i.upper() for i in alpha], [i.upper() for i in beta]
	alpha.extend(alpha_upper), beta.extend(beta_upper)
	code = dict(zip(alpha, beta))
	i, result, input1 = 0, [], list(input1)
	while i < len(input1):
		if input1[i].isalpha():
			input1[i] = code.get(input1[i])
		else:
			input1[i] = input1[i]
		result.append(input1[i])
		i +=1
	return ''.join(result)


# Exercise 7-13

def randrandrand():
	rand_list, result = [], []
	i, j = 0, 0
	time1, time2 = random.randint(1, 10), random.randint(1, 10)
	while i <= time1:
		rand_list.append(random.randrange(0, 10))
		i += 1
	while j <= time2:
		result.append(random.choice(rand_list))
		j += 1
	return result

def show_2sets():
	setA, setB = set(randrandrand()), set(randrandrand())
	return setA, setB, setA.union(setB), setA.intersection(setB)

# Exercise 7-14

def validate_2sets():
	setA, setB = set(randrandrand()), set(randrandrand())
	print 'set A: ', setA
	print 'set B: ', setB
	
	i, state = 0, ''
	while i < 3:
		union = raw_input('Please input the union of the above two sets: ')
		if union == setA.union(setB):
			print 'The union is correction.'
			state = 'c'
		else:
			state = 'w'
		intersection = raw_input('Please input the intersection of the above two sets: ')
		if intersection == setA.intersection(setB):
			print 'The intersection is correct.'
			state = 'c'
		else:
			state = 'w'		
		i += 1
	if state == 'w':
		print 'The correct answer is: ', setA.union(setB), setA.intersection(setB)


# Exercise 7-15

def calculate_set():
	input = raw_input('Please input two sets and the operater: ')
	print input
	setA, setB, oper = input.rsplit()
	if type(setA) is set and type(setB) is set:
		if oper == '==':
			return setA == setB


