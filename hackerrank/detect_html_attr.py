#https://www.hackerrank.com/challenges/html-attributes/problem
re
import sys
#sys.stdin.read()
N = raw_input()
result =[]
d={}
for i in range(int(N)):
    #res = re.findall(r'(<\w+>|<\w+\s+\w+|\w+=)',inp)
    res = re.findall(r'<(\w+)(|\s+[^>]*)>',raw_input())
    res1 = map(lambda x:[x[0],sorted(re.findall(r'(\w+)=[\'\"]',x[1]))],res)
    res2 = list(res1)
    #print(res2)
    ikeys = list(map(lambda x:x[0],res))
    for i in list(res2):
        if i[0] not in d.keys():
            d[i[0]]=i[1]
        else:
            d[i[0]]+=i[1]

#print(d)

for k, v in d.items():
    result.append(k+':'+",".join(sorted(list(set(v)))))
print("\n".join(sorted(result)))
