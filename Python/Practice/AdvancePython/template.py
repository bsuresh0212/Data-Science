from string import Template

class MyTemplate(Template):
    delimiter = '#'

def main():
    cart = []
    cart.append(dict(item='a',price='5',qty=3))
    cart.append(dict(item='b',price='1',qty=1))
    cart.append(dict(item='c',price='2',qty1=2))
    print(cart)
    # t = Template('$item($qty) = $price')  #default key parameter is $ we want change it use use Template class
    t = MyTemplate('#item(#qty) = #price')  # In these we can use the # instead of $
    total = 0
    for data in cart:
        # print(t.substitute(data))   #expect same key parameter for all dict keys shows error
        print(t.safe_substitute(data))   #expect no need given same key parameter for all dict keys suppose not there means shows $qty instead the substitution

        total += int(data['price'])
    print("Total = "+str(total))

if __name__ == '__main__':
    main()