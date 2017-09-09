
name = input("Enter your name\n") #waiting for user input then it will print what user entered put it into next(new) line
# print("Hi %s ,Welcome" %name) 

age = float(input("What is your age\n")) #our input type caste str to float
gender = input("What is your Gender\n") #simple user input

# %s string
# %d decimal values
# %f float values
# but python3 it will flexible for data types so int it will print %s also
# %s is flexible other than that it will except exact data type 
print("Hi %s ,welcome.\n You are %s years old %s" %(name,age,gender))
