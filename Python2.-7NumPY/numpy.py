import numpy
a = "Hello world"
str  = numpy.frombuffer(a,dtype="S1")
print(str)