#!/usr/bin/env python

import re
from random import randrange, choice
from string import ascii_lowercase as lc
from time import ctime


# Exercise 15-1


str1 = ["bat", "bit", "but", "hat", "hit", "hut"]

def re1(i):
    matched = re.match('[bh][aiu]t', i)
    return 'Exercise 15-1:', matched.group(0)


# Exercise 15-2


str2= ['Adam Smith', 'Betty Clare']

def re2(i):
    matched = re.match('[A-Z]\w+ [A-Z]\w+', i)
    return matched.group()


# Exercise 15-3


str3= ['A, Smith', 'B, Clare']

def re3(i):
    matched = re.match('[A-Z], [A-Z]\w+', i)
    return matched.group()


# Exercise 15-4


str4 = ['_As', 'a0', 'b_90']

def re4(i):
    matched = re.match('[_A-Za-z][A-Za-z0-9_]*', i)
    return matched.group()


# Exercise 15-5


str5 = ['1180 Bordeaux Drive', '3120 De la Cruz Boulevard']

def re5(i):
    matched = re.match('\d*( \w*)+', i)
    return matched.group()


# Exercise 15-6


str6 = ['www.foothill.edu', 'www.yahoo.com']

def re6(i):
    matched = re.match('www.[a-z]*.(com|net|edu)', i)
    return matched.group()


# Exercise 15-7, 15-8


str7 = ['340282366920938463463374607431768211456L', '-17168822186190360200L', '64']

def re7(i):
    matched = re.match('(-)?(\d)*(L)?', i)
    return matched.group()


# Exercise 15-9


str9 = ['3.14', '10.', '.001', '1e100', '3.14e-10', '0e0']

def re9(i):
    matched = re.match('(\d*)?.(\d*)?(e)?(-)?(\d*)?', i)
    return matched.group()


# Exercise 15-10


str10 = ['3.14j', '10.j', '10j', '.001j', '1e100j', '3.14e-10j']

def re10(i):
    matched = re.match('(\d*)?.(\d*)?(e)?(-)?(\d*)?j', i)
    return matched.group()


# Exercise 15-11


str11 = ['niceandsimple@example.com', 'very.common@example.com', 'a.little.lengthy.but.fine@dept.example.com',
         'disposable.style.email.with+symbol@example.com', 'other.email-with-dash@example.com',
         '"much.more unusual"@example.com', '"very.unusual.@.unusual.com"@example.com']

def re11(i):
    matched = re.match('([a-zA-Z0-9.-@"+ ])*@([a-zA-Z.])*com', i)
    if matched is not None:
        return matched.group()

# Exercise 15-12


str12 = ['www.google.com', 'http://app.google.com', 'https://en.wikipedia.org/wiki/Luhn_algorithm',
         'https://docs.python.org/2/reference/lexical_analysis.html?highlight=floats#floating-point-literals']

def re12(i):
    matched = re.match('(http(s)?://)?([a-z.]*)/?([a-z0-9.=?\-_/#]*)?', i)
    if matched is not None:
        return matched.group()


# Exercise 15-13


str13 = ["<type 'int'>", "<type 'float'>", "<type 'builtin_function_or_method'>"]

def re13(i):
    matched = re.match("<type '([a-z_]*)'>", i)
    return matched.group(1)


# Exercise 15-14


str14 = ['01', '1', '12']

def re14(i):
    matched = re.match('[01]?[0-9]', i)
    return matched.group()


# Exercise 15-15

# Luhn algorithm:

# From the rightmost digit, which is the check digit, moving left, double the value of every second digit;
# if the product of this doubling operation is greater than 9, then sum the digits of the products.
# Take the sum of all the digits.
# If the total modulo 10 is equal to 0 (if the total ends in zero) then the number is valid according to the Luhn formula; else it is not valid.


str15 = ['1234-8902-2134-1234', '1234-723445-23445', '8888-8888-8888-8888']

def re15(i):
    matched = re.match('([0-9]{4})-([0-9]{4,6})-([0-9]{4,5})((-[0-9]{4})?)', i)
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

    return 'valid' if result % 10 == 0 else 'invalid'



##########################################################################



tlds = ('com', 'edu', 'net', 'org', 'gov')

def re16():
    for i in xrange(randrange(5, 11)):
        dtint = randrange(2**32)
        dtstr = ctime(dtint)
        llen = randrange(4, 8)
        login = ''.join(choice(lc) for j in range(llen))
        dlen = randrange(llen, 13) # domain is longer
        dom = ''.join(choice(lc) for j in xrange(dlen))
        result = '%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, choice(tlds), dtint, llen, dlen)
        return result


##########################################################################


redata = ['Tue Jan 12 11:47:36 2049::hibes@ugrpxhm.gov::2494036056-5-7',
         'Fri Aug  4 01:17:44 2017::jyliil@vcxfyscz.org::1501780664-6-8',
         'Wed Feb 29 17:18:35 2068::gkpog@djdqiuashsih.org::3097732715-5-12',
         'Fri Jul 23 15:11:06 2066::atrks@yqgeoeky.net::3047094666-5-8',
         'Sat Jan  5 15:18:08 2104::tisrw@cjfbwvh.org::4228960688-5-7',
         'Tue Aug  3 06:33:18 2049::enbzzl@wwrrklt.org::2511556398-6-7',
         'Wed Jan 13 01:48:53 2010::scjnju@bdrdaqygdbav.net::1263318533-6-12',
         'Tue Feb 11 09:54:04 1975::ghywao@rqsqdbslop.com::161315644-6-10',
         'Sun Jun 22 03:59:12 2003::fyadf@bqjubqo.net::1056225552-5-7',
         'Wed Jun 10 01:06:58 2009::khwio@ozthnifvj.net::1244567218-5-9']


##########################################################################


# Exercise 15-19


def re19(line):
    matched = re.search('(\w{3} \w{3} [0-9 :]*)::', line)
    return matched.group(1)


# Exercise 15-20


def re20(line):
    matched = re.search('::([a-z@.]*)::', line)
    return matched.group(1)


# Exercise 15-21


def re21(line):
    matched = re.search('\w{3} (\w{3}) [0-9 :]*::', line)
    return matched.group(1)


# Exercise 15-22


def re22(line):
    matched = re.search('\w{3} \w{3} [0-9 :]* (\d{4})::', line)
    return matched.group(1)


# Exercise 15-23


def re23(line):
    matched = re.search('(\d{2}:\d{2}:\d{2})', line)
    return matched.group(1)


# Exercise 15-24


def re24(line):
    matched = re.search('::([a-z.]*)@([a-z.]*)::', line)
    return matched.group(1), matched.group(2)


# Exercise 15-25


def re25(line):
    matched = re.search('::([a-z.]*)@([a-z]*).([a-z]*)::', line)
    return matched.group(1), matched.group(2), matched.group(3)


# Exercise 15-26


def re26(line):
    matched = re.sub('(::[a-z.]*@[a-z.]*::)', ' :: abc@123.com ::  ', line)
    return matched


# Exercise 15-27


def re27(line):
    matched = re.search('\w{3} (\w{3}) +([0-9]+) [0-9:]* ([0-9]{4})::', line)
    return matched.group(1), matched.group(2), matched.group(3)


# Exercise 15-28


str28 = ['800-555-1212', '555-1212']

def re28(i):
    matched = re.match('(\d{3}-)?\d{3}-\d{4}', i)
    return matched.group()


# Exercise 15-29


str29 = ['800-555-1212', '555-1212', '(800) 555-1212']

def re29(i):
    matched = re.match('(\d{3}-|\(\d{3}\) )?\d{3}-\d{4}', i)
    return matched.group()


# Exercise 15-31


def scrub_tweet(tweet, meta=False):
    matched = re.sub('#\w* ', '', tweet)
    re_matched = re.sub('RT@\w* ', '', matched)

    if meta is False:
        print re_matched
    else:
        meta_dict = {}
        hashtag = {'ht': re.findall('(#\w*) ', tweet)}
        retweet = {'rt': re.findall('RT(@\w*) ', tweet)}
        meta_dict.update(hashtag)
        meta_dict.update(retweet)

        print re_matched
        print 'meta info:', meta_dict



def range_(start, end, step):
    result = [start]
    while start < end:
        start += step
        result.append(start)
    return result

def xrange_(start, end, step):
    while start < end:
        yield start
        start += step


