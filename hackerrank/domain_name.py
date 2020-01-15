# code : utf-8

import re
import sys

mystr = sys.stdin.read()

http = r"http[s]*?:\/\/(?:www\.|(?!www))*((?:[\-a-zA-Z0-9]+\.)*[\-a-zA-Z0-9]+\.[a-zA-Z0-9]+(?:[a-zA-Z0-9]+)?)"

res = re.findall(http,mystr)
names = list(set(res))
names = sorted(names)
out = ';'.join(names)
print out
