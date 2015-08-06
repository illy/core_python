__author__ = 'acepor'

from urllib import urlopen

douban = urlopen('http://www.douban.com/feed/people/casa_nova/interests')
for line in douban:
    print line