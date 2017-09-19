#just run pythnon3 module_using_name.py
#Every python module has its __name__ defined.if this is __main__ 
#this is program stroed as a 
    #import sys
    #sys.path  -->stores as shows the following path as well
#now import this file as import module_using_name
    #run as another module


if __name__ == '__main__':
    print("This program is being run by itself")
else:
    print("I am imported from anthoer program")
