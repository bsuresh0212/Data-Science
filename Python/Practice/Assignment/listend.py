if __name__ == '__main__':
    def listArrange(getList):
        return [getList[0],getList[-1]]
    try:
        nList = int(input('Enter the range of the list  '))
        list1 = []
        for i in range(0,nList):
            ele = int(input('Enter the {} index list value is   '.format(i)))
            list1.append(ele)
        print('The first and last idx values are {}'.format(listArrange(list1)))    
    except ValueError:
        print('Integer only allowed')