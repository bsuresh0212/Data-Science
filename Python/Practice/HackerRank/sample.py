''' n = int(input())
integer_list = map(int, input().split())
print(hash(tuple(integer_list)))
 '''

# x = int ( input())
# y = int ( input())
# n = int ( input())
# ar = []
# p = 0
# for i in range ( x + 1 ) :
#     for j in range( y + 1):
#         if i+j != n:
#             ar.append([])
#             ar[p] = [ i , j ]
#             p+=1
# print(ar)

''' 
n = int(input())
arr = map(int, input().split())
print(list(arr)) '''
from operator import itemgetter
if __name__ == '__main__':
    students = []
    smallest = []
    sm1,sm2 = float('inf'),float('inf')
    for _ in range(int(input())):
        samp = []
        # name = input()
        score = float(input())
        # samp.append(name)
        samp.append(score)
        students.append(samp)
    print(students)
    # sm1 = students[0][0]
    # sm2 = students[0][0]
    for idx,stu in enumerate(students):
        x = stu[0]
        if  x < sm1:
            sm1 = x
            if(idx == 0):
                sm2 = sm1
        if  (x > sm1 and sm2 >= x):
            print(idx)
            sm2 = x
            print('sm2 ',sm2)
            # smallest.append(students[idx])
    print(smallest)
    # students = sorted(students, key=lambda x: x[1])
