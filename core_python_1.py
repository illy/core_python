#!/usr/bin/env python

import re


# Exercise 1-1


str1 = ["bat", "bit", "but", "hat", "hit", "hut"]

for i in str1:
    matched = re.match('[bh][aiu]t', i)
    print 'Exercise 1-1:', matched.group(0)


# Exercise 1-2


str2= ['Adam Smith', 'Betty Clare']

for i in str2:
    matched = re.match('[A-Z]\w+ [A-Z]\w+', i)
    print 'Exercise 1-2:', matched.group()


# Exercise 1-3


str3= ['A, Smith', 'B, Clare']

for i in str3:
    matched = re.match('[A-Z], [A-Z]\w+', i)
    print 'Exercise 1-3:', matched.group()


# Exercise 1-4


str4 = ['_As', 'a0', 'b_90']

for i in str4:
    matched = re.match('[_A-Za-z][A-Za-z0-9_]*', i)
    print 'Exercise 1-4:', matched.group()


# Exercise 1-5


str5 = ['1180 Bordeaux Drive', '3120 De la Cruz Boulevard']

for i in str5:
    matched = re.match('\d*( \w*)+', i)
    print 'Exercise 1-5:', matched.group()


# Exercise 1-6


str6 = ['www.foothill.edu', 'www.yahoo.com']

for i in str6:
    matched = re.match('www.[a-z]*.(com|net|edu)', i)
    print 'Exercise 1-6:', matched.group()


# Exercise 1-7, 1-8


str7 = ['340282366920938463463374607431768211456L', '-17168822186190360200L', '64']

for i in str7:
    matched = re.match('(-)?(\d)*(L)?', i)
    print 'Exercise 1-7, 1-8:', matched.group()


# Exercise 1-9


str9 = ['3.14', '10.', '.001', '1e100', '3.14e-10', '0e0']

for i in str9:
    matched = re.match('(\d*)?.(\d*)?(e)?(-)?(\d*)?', i)
    print 'Exercise 1-9:', matched.group()


# Exercise 1-10


str10 = ['3.14j', '10.j', '10j', '.001j', '1e100j', '3.14e-10j']

for i in str10:
    matched = re.match('(\d*)?.(\d*)?(e)?(-)?(\d*)?j', i)
    print 'Exercise 1-10:', matched.group()


# Exercise 1-11


str11 = ['niceandsimple@example.com', 'very.common@example.com', 'a.little.lengthy.but.fine@dept.example.com',
         'disposable.style.email.with+symbol@example.com', 'other.email-with-dash@example.com',
         '"much.more unusual"@example.com', '"very.unusual.@.unusual.com"@example.com']

for i in str11:
    matched = re.match('([a-zA-Z0-9.-@"+ ])*@([a-zA-Z.])*com', i)
    if matched is not None:
        print 'Exercise 1-11:', matched.group()

# Exercise 1-12


str12 = ['www.google.com', 'http://app.google.com', 'https://en.wikipedia.org/wiki/Luhn_algorithm',
         'https://docs.python.org/2/reference/lexical_analysis.html?highlight=floats#floating-point-literals']

for i in str12:
    matched = re.match('(http(s)?://)?([a-z.]*)/?([a-z0-9.=?\-_/#]*)?', i)
    if matched is not None:
        print 'Exercise 1-12:', matched.group()


# Exercise 1-13


str13 = ["<type 'int'>", "<type 'float'>", "<type 'builtin_function_or_method'>"]

for i in str13:
    matched = re.match("<type '([a-z_]*)'>", i)
    print 'Exercise 1-13:', matched.group(1)


# Exercise 1-14


str14 = ['01', '1', '12']

for i in str14:
    matched = re.match('[01]?[0-9]', i)
    print 'Exercise 1-14:', matched.group()


# Exercise 1-15

# Luhn algorithm:

# From the rightmost digit, which is the check digit, moving left, double the value of every second digit;
# if the product of this doubling operation is greater than 9, then sum the digits of the products.
# Take the sum of all the digits.
# If the total modulo 10 is equal to 0 (if the total ends in zero) then the number is valid according to the Luhn formula; else it is not valid.


str15 = ['1234-8902-2134-1234', '1234-723445-23445', '8888-8888-8888-8888']

for i in str15:
    matched = re.match('([0-9]{4})-([0-9]{4,6})-([0-9]{4,5})((-[0-9]{4})?)', i)

    print 'Exercise 1-15:', matched.group()
    matched_cc = matched.group(1) + matched.group(2) + matched.group(3) + matched.group(4).strip('-')
    result, temp_r = 0, 0
    if len(matched_cc) == 15:
        for i in range(0, 13):
            if i % 2 == 0:
                temp = int(str(matched_cc)[i]) * 2
                if temp > 9:
                    temp = int(str(temp)[0]) + int(str(temp)[1])
                else:
                    temp = temp
                result += temp
            else:
                result += int(str(matched_cc)[i])

    elif len(matched_cc) == 16:
        for i in range(0, 14):
            if i % 2 == 1:
                temp = int(str(matched_cc)[i]) * 2
                temp1 = temp
                temp_r += temp1
                if temp > 9:
                    temp = int(str(temp)[0]) + int(str(temp)[1])
                else:
                    temp = temp
                result += temp
            else:
                result += int(str(matched_cc)[i])
    print result
    if result % 10 == 0:
        print 'valid'
    else:
        print 'invalid'


##########################################################################


from random import randrange, choice
from string import ascii_lowercase as lc
from time import ctime

tlds = ('com', 'edu', 'net', 'org', 'gov')

for i in xrange(randrange(5, 11)):
    dtint = randrange(2**32)
    dtstr = ctime(dtint)
    llen = randrange(4, 8)
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13) # domain is longer
    dom = ''.join(choice(lc) for j in xrange(dlen))
    result = '%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, choice(tlds), dtint, llen, dlen)
    print result

# Exercise 1-





# Exercise 1-





# Exercise 1-




# Exercise 1-




# Exercise 1-




# Exercise 1-




# Exercise 1-




# Exercise 1-




# Exercise 1-




# Exercise 1-




# Exercise 1-




# Exercise 1-




# Exercise 1-




# Exercise 1-




# Exercise 1-








def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    print checksum
    return checksum % 10

def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0

############################################

if __name__ == '__main__':
    print is_luhn_valid('8888888888888888')