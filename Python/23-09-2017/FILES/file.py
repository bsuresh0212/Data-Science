'''
read a file from 

'''

''' data = open('text.txt','r')
for line in data:
    print(line)
data.close()    
 '''

'''
write in a file

'''    

tar = open('new_file.txt','w')
tar.write('Hey i m suresh ')
tar.write('Python')
tar.write('\n')
tar.write('finally i got')
tar.close()


tar = open('new_file.txt','a')
tar.write('\n')
tar.write('I added the line')
tar.close()