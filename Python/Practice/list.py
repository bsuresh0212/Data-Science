''' list = ['hi','hello','welcome','to']

print('Len of the string',len(list))

#print the all elements of the list

for li in list:
    print(li,end=' ')

print('\n')
#sort the list
list.sort()
print('sorted list is',list)

#append the list
list.append('Python')
print('Append the list ',list)

#del the list ele

del list[0]

print('After deleting the 1st index of the list is',list) '''


from operator import itemgetter
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
students = sorted(students,key=lambda x:x[1])
print(students)
names = []
for i,stu in enumerate(students):
    if (i == 0):
        num = students[0][1]
    elif (num <= students[i][1]):
        num = students[i][1]
        if(i <= len(students)-2 and num == students[i][1]):
            names.append(students[i][0])

print(names)