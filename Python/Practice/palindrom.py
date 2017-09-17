str = input("Enter the string")
len = len(str)
i = 0 
print(len//2)
length = len//2
while length:
    if(str[i] == str[length+1]):
        print(i)
        continue
    else:
        print('Not a palindrom')
        break
    i = i+1

if(i == length):
    print('String is palindrom') 
else:    
    print('String not a palindrom') 
