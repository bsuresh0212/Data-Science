def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return(a*b)
def div(a,b):
    return a/b
def user_input():
    a = int(input("Enter a First number"))
    b = int(input("Enter a Second number"))
    return a,b

while True:
    user_choice = int(input("Please select an option\n1.Add\n2.sub\n3.mul\n4.Div\n"))
    if user_choice == 1:
        a,b = user_input()
        print(add(a,b))
    elif user_choice == 2:
        a,b = user_input()
        print(sub(a,b))
    elif user_choice == 3:
        a,b = user_input()
        print(mul(a,b))
    elif user_choice == 4:
        a,b = user_input()
        print(div(a,b))
    else:
        print("Give a corrct input option")
        
    
        

