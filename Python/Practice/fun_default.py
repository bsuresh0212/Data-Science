#it wil take default arguments as when user missed the parameter otherwise it will take what user entered
def say(message,time=1):
    print(message * time)

say('Suresh')
say('Harshika_sai ',5)



# def fun(a=5,b): #wrong syntax of default argumnt
#     print(a+b)
#
# fun(3,4)
# fun(b=9) #we never pass value like this


def fun(a,b=10,c=20):
    print("a is ",a,"b is ",b,"c is ",c)
fun(1,2)
fun(4,c=100)
fun(a=200,b=100)




