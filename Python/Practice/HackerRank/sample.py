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
    for _ in range(int(input())):
        samp = []
        name = input()
        score = float(input())
        samp.append(name)
        samp.append(score)
        students.append(samp)
    print(students)
    print(sorted(students, key=lambda x: x[1]))