''' 
Syntax :: list 

list_name = []
    
'''
#start with index == 0 to end
#groceries = ['dall','Rice','Sambar masala',1,2.5,'100gms']
''' print(groceries)
print(groceries[0])
print(groceries[0:4]) #op : include 0 and exclude 4
print(groceries[:3]) #op : include 0 and exclude 3
 '''

# print the while statement

''' i = len(groceries) -1
while i>=0:
    print(groceries[i])
    i = i-1    
 '''


'''
for var_name in <some_collection_data>:
    do something
'''
''' 
for name in groceries:
    print(name) '''


## print # 1 to 50 using for loop
''' for i in range(1,51): #range will inside creates a list then rotate the untill the list is end
    print(i)
 '''
''' 
for idx,i in enumerate(range(1,51)):   #enumare return the index of the list added another value of idx
     print(idx,i) '''


#create the two list same size
# name the 1st list groceries 
# name of the second list weight
# finally print a and their associated weights together     

groceries = ['dall','Rice','Sambar masala']
weight = [1,2.5,'100gms']

'''
o/p 
Daal 1
Rice 2
Sambar masala 100gms
'''
''' 
for index,i in enumerate(weight):
    # print(groceries[index],' ',i)
    print(groceries[index]+' '+str(i))  # it shows error means weight hava a int part so we can explicitly convert into str '''


#compare the 2 lists
list1 = [1,2]
list2 = [1,-2,3,4,5]
res = []
for index,i in enumerate(list1):
    if i == list2[index]:
        res.append(True)
    else:
        res.append(False)
print(res)         

