import sys
import os

print('The command line arguments are: ')
for i in sys.argv:
    print(i)

print('\n\n The PYTHON PATH is',sys.path,'\n')


#Get current working directory from  'OS' module
print(os.getcwd())


#import only one module from math module like this
from math import sqrt

print('The Sqrt of the 16 is ',sqrt(16))