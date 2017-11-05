import re
''' 
def Main():
    str = "Hey i m looking on it"
    searchStr = re.search('look',str,re.M|re.I) #search the string is there in a string
    if searchStr:
        print('Search Found: '+searchStr.group()) 
    matchStr = re.match('looking',str,re.M|re.I) #math checks the entire string is match
    if matchStr:
        print('Match Found: '+matchStr.group())


if __name__ == '__main__':
    Main()  '''



'''
Task to search the file in a specific word is there with line number all are in command line
'''

import argparse

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('word',help='Enter word to search')
    parser.add_argument('FileName',help='Enter File name to search')
    args = parser.parse_args()
    searchFile = open(args.FileName)
    lineNo = 0;
    for line in searchFile.readlines():
        line =line.strip('\n\r')
        lineNo += 1
        searchres = re.search(args.word,line,re.M|re.I)
        if searchres:
            print(str(lineNo) +' : '+line)

if __name__ == '__main__':
    Main()

    
