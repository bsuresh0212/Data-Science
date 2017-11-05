class parentClass:  #super class
    name = "suresh"
    num = 10
class childClass(parentClass): #subclass it was inherited by parentClass so this class have all access of parent class
    age = 12

parentObj = parentClass()
print(parentObj.name)
print(parentObj.num)
# print(parentObj.age) #it gives error coz parentClass has no member called age
childObj = childClass()
print(childObj.name)
print(childObj.num)
print(childObj.age)  #but childClass have a age member


print("Multiple super/parent classes ------------>")

class MOM:
    m = "This is mom"
    com = "Same variable in MOM parent class"
class DAD :
    d = "This is dad"
    com = "Same variable in DAD parent class"
#inherited both dad and mom parent class into child class
#in these we have common variabled called com
#so in child class obj get access cobj.com it will print the 1st inherited obj
#class child(DAD,MOM):  -- > DAD class com wil print
#class child(MOM,DAD):  -- > MOM class com wil print
class child(DAD,MOM):
    c = "This is child"

cobj = child()
print(cobj.m)
print(cobj.d)
print(cobj.c)
print(cobj.com)