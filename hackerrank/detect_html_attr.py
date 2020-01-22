# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
import sys
#sys.stdin.read()
N = raw_input()
result =[]
for i in range(int(N)):
    #res = re.findall(r'(<\w+>|<\w+\s+\w+|\w+=)',inp)
    res = re.findall(r'<(\w+)(|\s+[^>]*)>',raw_input())
    #<(\w+)(|\s+[^>]*)>  (\w+)=[\'\"]
    #print(res)
    #res1 = map(lambda x:re.sub(r'[^\s\w]','',x),res)
    #res1 = map(lambda x:x.replace(" ",":").replace("<","").replace(">",":"),res)
    #print(res1)
    #r1 = list(set(res1))
    #print(r1)
    #res2 = map(lambda x:re.sub(r'\s',':',x),res1)
    #print(res2)
    res1 = map(lambda x:[x[0],",".join(sorted(re.findall(r'(\w+)=[\'\"]',x[1])))],res)
    #print(res1)
    res2 = map(lambda x:':'.join(x),res1)
    #print(res2)
    
    result.extend(res2)
print(result)
r1 = list(set(result))
print(r1)
rs = sorted(r1)
print("\n".join(rs))
