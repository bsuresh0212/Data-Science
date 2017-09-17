while True:
    try:
        num = int(input("Enter the number \n"))
        factorial = 1
        if (num == 0):
            factorial = 1
        else:    
            while num>0:
                factorial = num*factorial
                num = num-1
        print("The factorial of given num is %d \t"%(factorial))
    except ValueError:
        print("Allowed only integer")    