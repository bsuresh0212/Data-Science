def fib(count):
    a = 0
    b = 1
    print(a,end = ' ')
    for i in range(1,count):
        fibS = a+b
        print(fibS,end = ' ')
        a = b
        b = fibS
    print('\n')
while True:
    try:
        count = int(input("Please enter the range of fib. series \t"))
        if (count<0):
            print("Enter the positive number")
        elif count == 0:
            pass 
        else:
            fib(count)    
    except ValueError:
        print('Please Enter the integer')