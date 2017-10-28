def swap(x,y):
    ''' print("Before swap x = %d , y = %d" %(x,y))
    x = x + y  
    y = x - y
    x = x - y
    print("Before swap x = %d , y = %d" %(x,y)) '''
    #simply in python
    
    print("Before swap x = %d , y = %d" %(x,y))
try:
    user_int = input('Enter a two nuber a swap \t')
    num = user_int.split()
    if len(num) == 2:
        swap(int(num[0]),int(num[1]))
    else:
        print('Please provide a enough number of inputs') 
except ValueError:
    print('Allowed a integer')    