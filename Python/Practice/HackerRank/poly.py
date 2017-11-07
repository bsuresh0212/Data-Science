''' x,k = map ( int , input().split())
tot = 0
for a in range(1,k+1):
    print(a)
    tot += x ** k
if tot == k:
    print('True')
else:
    print('False')

    2 15
x**4 - x + 1 '''

x,k = map ( int , input().split())
s= input()
print(eval(s) == k)