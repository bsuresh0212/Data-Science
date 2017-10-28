import numpy as np
#data type metioned array
#S -> string 20 byte size
#i1 -> int 8 byte
#f4  -> float32 print(np.dtype('f4'))
student=np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
print (student)
#that decleared data type assign the array like this
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype=student)
print (a)

# C_CONTIGUOUS (C) === > The data is in a single, C-style contiguous segment
# F_CONTIGUOUS (F) ==== > The data is in a single, Fortran-style contiguous segment
# OWNDATA (O) ====>   The array owns the memory it uses or borrows it from another
#                     object
# WRITEABLE (W) ====> The data area can be written to. Setting this to False locks the
#                     data, making it read-only
# ALIGNED (A) =====>  The data and all elements are aligned appropriately for the
#                     hardware
# UPDATEIFCOPY (U) ==>This array is a copy of some other array. When this array is
#                     deallocated, the base array will be updated with the contents
#                     of this array
print(a.flags)


#create empty array for the following shape as well
'''
numpy.empty(shape,dtype=int,order=C)  //order C or F F means fortran
numpy.zeros(shape,dtype=int,order=C)  //order C or F F means fortran
'''
a = np.empty([3,2],dtype='int')
print (a)

#custom data type

x = np.zeros((5,2),dtype= [('x','f4'),('y','i8')])
print(x)


#convert list into a nd.array

x  = [1,2,3,4,5,6]
x = np.asarray(x,dtype="float")
print(x)


#Buffer concepts
#syntax numpy.frombuffer(buffer, dtype=float, count=-1, offset=0)
# buffer > Any object that exposes buffer interface
# dtype > Data type of returned ndarray. Defaults to float
# count > The number of items to read, default -1 means all data
# offset > The starting position to read from. Default is 0


s = "Hello world!"
print(s)
a = np.frombuffer(s,dtype='S1')
print(a)