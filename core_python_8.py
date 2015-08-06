#!/usr/bin/env python

import re
from operator import itemgetter

# Exercise 8-2

def looping1(f, t, i):
    result = [f]
    if (t-f)%i == 0:
        while f < t:
            f += i
            result.append(f)
    else:
        result = range(f, t, i)
    return result

def looping2(f, t, i):
    result = range(f, t, i)
    if (t-f)%i == 0:
        result.append(t)
    return sorted(result)

def looping3(f, t, i):
    result = []
    while f < t:
        f += i
        result.append(f)
    return result


# Exercise 8-4

def isprime(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            print num, ' is not prime'
            break
        count -= 1
    else:
        print num, 'is prime'


# Exercise 8-5

def getfactors(num):
    factors, i = [num], 1
    while i <= num/2:
        if num % i == 0:
            factors.append(i)
        i +=1
    return factors


# Exercise 8-6

def isprime(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            break
        count -= 1
    else:
        return num

def prime_list(limit):
    result = []
    for i in range(2, limit):
        if isprime(i):
            result.append(i)
    return result


def twin_prime(limit):
    i, result = 0, []
    l = prime_list(limit)
    while i < len(l)-1:
        if l[i+1] - l[i] == 2:
            result.append((l[i], l[i+1]))
        i+=1
    return result


def prime_factor(num):
    result, final = [], []
    primes = prime_list(num)
    for p in primes:
        while num % p == 0:
            result.append(p)
            num = num / p
    return result


def prime_factor2(num):
    result = []
    d = 2
    while d*d <= num:
        while (num % d) == 0:
            result.append(d)
            num //= d
        d += 1
    if num > 1:
       result.append(num)
    return result


# Exercise 8-7

def perfect_number(num):
    factors, i, result = [], 1, 0
    while i <= num/2:
        if num % i == 0:
            factors.append(i)
        i +=1
    for f in factors:
        result += f
    return 1 if result == num else 0

def get_perfect(limit):
    result = []
    for i in range(1, limit):
        if perfect_number(i) == 1:
            result.append(i)
    return result

# Exercise 8-8

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

# Exercise 8-9

def fibonacci1(num):
    if num == 1 or num == 2:
        return 1
    elif num > 2:
        return fibonacci(num-1) + fibonacci(num-2)


def fibonacci2(num):
    a, b = 1, 1
    for i in range(num-1):
        a, b = b, a+b
    return a

# Exercise 8-10

volw = ['a', 'e', 'i', 'o', 'u']
cons = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z']
special = ['h', 'y', 'qu']

def vowel_cons(input):
    i, j, m, n = 0, 0, 0, 0
    input = list(input.lower())
    for char in input:
        if char in volw:
            i+=1
        elif char in cons:
            j+=1
    while m < len(input)-1:
        if input[m] == 'h' or input[m] == 'y' or input[m] + input[m+1] == 'qu':
            n+=1
        m+=1
    return i, j, n


# Exercise 8-11

def record_name(time=5):
    i, j, result = 0, 1, []
    print 'Enter total number of names: %s' %time
    while i < time:
        input = raw_input('Please enter name %s: ' %i)
        if ',' in input:
            result.append(input)
            i += 1
        else:
            print 'Wrong format... should be Last, First.'
            print 'You have done this %s time(s) already. Fixing input...' %j
            j += 1
    print 'The sorted list (by last name) is:'
    return sorted(result)


# Exercise 8-12

def print_values(begin, end):
    print '---------------'
    print 'Enter begin value: %s' %begin
    print 'Enter end value: %s' %end
    print 'DEC    BIN    OCT    HEX    ASCII'
    print '-------------------------------'
    for i in range(begin, end +1):
        if unichr(i):
            print str(i) + '   ' + str(bin(i)[2:]) + '   ' + str(oct(i)[1:]) + '   ' + str(hex(i)[2:]) + '   ' + str(unichr(i))
        else: 
            print str(i) + '   ' + str(bin(i)[2:]) + '   ' + str(oct(i)[1:]) + '   ' + str(hex(i)[2:])
