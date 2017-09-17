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
#using global keyword
def global_fun():
    global x
    print('Global x value ,',x)
    x = 2
    print("Global value is changed ",x)

global_fun()
print("After changed the global value x is",x)

