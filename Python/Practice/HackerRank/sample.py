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
        name = input()
        score = float(input())
        samp.append(name)
        samp.append(score)
        students.append(samp)
    students = sorted(students, key=lambda x: x[1])
    sm1 = students[0][1]
    sm2 = students[1][1]
    if sm1 == sm2:
        for idx,stu in enumerate(students):
            if sm1 < stu[1]:
                sm2 = stu[1]
                break;
    if sm1 < sm2: 
        for idx,stu in enumerate(students):
            if sm2 == stu[1]:
                smallest.append(stu)
    smallest = sorted(smallest, key=lambda x: x[0])
    for small in smallest:
        print(small[0])
