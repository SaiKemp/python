#https://www.hackerrank.com/challenges/detect-the-email-addresses/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
# coding: utf-8
import re
# read a line from STDIN
#my_string = raw_input()
import sys
my_string = sys.stdin.read()
#res=re.findall(r'[a-zA-Z0-9._]+@[a-zA-Z0-9.]+',my_string)
res=re.findall(r'\b[\w+.]{1,}@[\w+.]{1,}\b',my_string)
r1 = list(set(res))

output = ";".join(sorted(r1))
print(output)
