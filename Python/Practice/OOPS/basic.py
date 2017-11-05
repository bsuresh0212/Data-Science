'''
Basic declaration of a class and Objects 

''' 
class define:
    color = "red"
    num = 3
    def fun(self):
        return 'self function is executed'
print(define)
extractClass = define()
print(extractClass.color)
print(extractClass.num)
print(extractClass.fun())



class className:
    def createName(self,name):
        self.name = name
    def displayName(self):
        return self.name
    def sayHello(self):
        print("Hello this is {}".format(self.name))

first = className()
second = className()
first.createName('Suresh') #self assigned as first so we can send into 2nd paramer
print(first.displayName())
first.sayHello()
#name changed
first.createName('Ramesh') #self assigned as first so we can send into 2nd paramer
first.sayHello()
#same as second object get all methods have in class