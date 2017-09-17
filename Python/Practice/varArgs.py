def total(a=0,*number,**phonebook):
    print('a ',a)

    for n in number:
        print('Items -> ',n)

    for first_param,sencond_param in phonebook.items():
        print(first_param,sencond_param)

#pass it exactly *number in tubles and  **phonebook in dictionary
#Other than that shows error
total(10,1,2,4,5,sur=98,esh=94,aaa=60,bbb=33,ccc=33,ddd=7)


