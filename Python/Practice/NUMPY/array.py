#Arrays


import numpy as np
''' 
a = np.array([1,2,3]) #1d array
print(type(a))  #prints numpy.ndarray
print(a.shape)  #prints (3,)
print(a)
a[0] = 9 #replace the that idx value
print(a)  
print('--------------------- 2d array')
b = np.array([[2,3,4],[5,6,7]])
print(b)
print(b.shape) '''


''' 
#create a new arrays
c = np.zeros((2,2))  #create a array consist of all zeros
print(c)   # Prints "[[ 0.  0.]
           #          [ 0.  0.]]"
print('\n')
d = np.ones((1,2))    # Create an array of all ones
print(d)              # Prints "[[ 1.  1.]]"
print('\n')

d = np.full((3,4),8)  # Create an array of all 8
print(d)
print('\n')
 
b = np.eye(3) #print identity matrix means right diagonal only values other than that all are zeros 
print(b)

print('\n')

e = np.random.random((2,2)) * 1000 # Create an array filled with random values
print(e)    

 '''
####
'''
indexing and slicing the array using numpy
'''
###
''' 
#create a array rank 2 and shape(3,4)

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
print('\n')

#slicing the row as 1st 2 rows
    #columns like 1 and 2

b = a[:2,1:3]
print(b)
print('\n')
print(a)   

print(b[0,1]) #print the 0th row and 1st col of the value

print(a[0,2]) #in that b[0,1] same value in a(original array) is a[0,2]

b[0,1] = 11 #so i changed the value of b[0,1] but it will affact the value of equ. array value in array of  a[0,2]
print(b[0,1])
print(a[0,2])
 '''


''' #array return differnet ranks(dimentioal) of matrix 
# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

#splicing with row
row_r1 = a[1,:] #reutrn 1d array
row_r2 = a[1:2,:] #retrun 2d array
print(row_r1,row_r1.shape)
print(row_r2,row_r2.shape)

#splicing with column
col_c1 = a[:,1]
col_c2 = a[:,1:2]
print(col_c1,col_c1.shape)
print(col_c2,col_c2.shape)
 '''
''' 

#array print some index from another array as well

# Create a new array from which we will select elements
a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]]) 

print(a)

b = np.array([0,2,1,0])

print(a[np.arange(4),b])

a[np.arange(4),b] += 90

#added 90+a[x,x] in that index
print(a)

 '''

x = np.array([[1,2],[3,4]])

print(np.sum(x))  # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"


#TRANSPOSE the array
print(x.T)



# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)   # Create an empty matrix with the same shape as x

# Add the vector v to each row of the matrix x with an explicit loop
for i in range(4):
    y[i, :] = x[i, :] + v #x[0,:] returns 1d array of 0th row added v [2,2,4]

# Now y is the following
# [[ 2  2  4]
#  [ 5  5  7]
#  [ 8  8 10]
#  [11 11 13]]
print(y)