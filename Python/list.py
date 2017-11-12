#this is one way
a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
res = []
for li in a:
    if li not in res:
        res.append(li)
for li in b:
    if li not in res:
        res.append(li)
print(res)
res = []
res = [i for i in a if i in b]
print(res)
''' 
import random
list(set([random.randlint(0,100) for r in xrange(10)]).intersection([random.randlint(0,100) for r in xrange(20)]))
 '''

for i in range(5):
    if i == 5:
        break
    else:
        print(i)
else:
    print('here')