def print_max(x, y):
    '''Prints the max. of two numbers.
    The two variable must be a integer
    '''
    x = int(x)
    y = int(y)

    if x > y:
        print(x ,'The max value')
    else:
        print(y ,'The max value')

print_max(2,3)
print(print_max.__doc__)
