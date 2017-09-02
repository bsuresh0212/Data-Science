print("Hi,Enter the temp in degree celsius")
celsius = int(input()) # 1.input ==> deceimal values shows error
                        # reason .(dot) is a char. will convert as a int so it will shows error like a string "sureshb"
#print(type(celsius));
#print(type(float(celsius)));

#convert celsius to Fahrenheit
# Fa = (celsius)(9/5)+32
fah = (32+((9/5)*celsius))
print(fah)




