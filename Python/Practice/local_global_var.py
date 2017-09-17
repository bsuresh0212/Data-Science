# local variable changes only locally

x = 50

def fun(x):
    print("x is",x)
    x=2
    print("change local x to ",x)

print('x value ',x)
fun(x)
print('x is still',x)

# global variable change globally
#using global variable

