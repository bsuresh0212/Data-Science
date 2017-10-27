#list search

if __name__ == '__main__':
    def find(getList,ele_to_find):
        for ele in getList:
            if(ele == ele_to_find):
                return True
        return False
    try:
        nList = int(input('Enter the range of the list  '))
        list1 = []
        for i in range(0,nList):
            ele = int(input('Enter the {} index list value is   '.format(i)))
            list1.append(ele)
        find_ele = int(input('Enter the number to search the list  '))    
        print('{} present in the list is ---> {}'.format(find_ele,find(list1,find_ele)))    
    except ValueError:
        print('Integer only allowed')