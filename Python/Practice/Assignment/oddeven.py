#odd or even number
if __name__ == '__main__':
    try:
        getNum = int(input('Enter the number \t'))
        if (getNum %2 == 0):
            print('{}  is even'.format(getNum))
        else:
            print(' {}  is odd'.format(getNum))
    except ValueError:
        print('Allow only integer') 

