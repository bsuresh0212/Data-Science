def calYr(age):
    return 2017+(100-age)
    
while True:
    try:
        user_input = input("Enter your name and age \t")
        name_age = user_input.split()
        if len(name_age) == 0:
            print("Please provide an input you dummy")
            continue
        name = name_age[:-1]
        name = ' '.join(name)
        age = int(name_age[-1])
        # name = input("Enter the Name \t")
        # age = int(input("Enter Your Age\t"))
        if (age<0):
            print("Hi %s you entered negative value"%(name))
        elif (age > 100):
            print("Hi %s you crossed 100 years"%(name))
        elif (age == 100):
            print("Hi %s you are in 100th years"%(name))
        else:
            print("Hi %s you will be 100 age in this year %d"%(name,calYr(age)))
    except ValueError:
        print("Allowed only integer")


















