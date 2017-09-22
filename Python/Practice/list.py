list = ['hi','hello','welcome','to']

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

print('After deleting the 1st index of the list is',list)