#constructor

''' 
class new:
    def call(self):
        print('the call func is called')

newObj = new()  #the class is assigned to obj
newObj.call()
 '''
class new :
    def __init__(self):
        print('The init func is invoked')
        print('This is how to work on the init fuc') 
newObj = new() #when class assigned to object that time automatically invoked by __init__ function                      without explicity called
