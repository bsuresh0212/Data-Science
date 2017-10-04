def swap(a,b):
    print("Before swap a = %d , b = %d" %(a,b))
    print("After swap a = %d , b = %d" %(a+b-a,a+b-b))
try:
    user_int = input('Enter a two nuber a swap \t')
    num = user_int.split()
    if len(num) == 2:
        swap(int(num[0]),int(num[1]))
    else:
        print('Please provide a enough number of inputs') 
except ValueError:
    print('Allowed a integer')    