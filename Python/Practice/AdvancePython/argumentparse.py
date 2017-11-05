import argparse

def fact(n):
    fact = 1
    for i in range(n):
        fact += fact*i
    return fact

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('num',help="To find factorail of a given number",type=int) #given input is string so we mentioned that it is a integer so (type=int) usage : python3 filename.py 23

    #added another argument like verbosity(we expect more and clean output)
    #action="store_true" is automatically true when the character is entered .
    #not using action="store_true" in these option we given exact option into this

    #in these more option is there when we use it then we will learn about more options on it
    parser.add_argument('-v',"--verbose",action="store_true",help="Increase the verbosits")

    #output(optional argument is - actuval value is --)
    parser.add_argument('-o','--output',help='The result is stored in a file',action='store_true')
    args = parser.parse_args()
    result = fact(args.num)

    if args.output:
        f = open('fact.txt','a')
        f.write('The fact of {} number is {}'.format(args.num,result)+ '\n' )
        f.close()
    if args.verbose:
        print('The fact of given number is {}'.format(result))
    else:
        print(result)
if __name__ == '__main__':
    Main()