# open a file 
# go to that file contain  dir
''' 
with open('file.txt','w') as openFile:
    openFile.write('Hey this added by me') '''


import requests
from bs4 import BeautifulSoup
 
base_url = 'http://www.nytimes.co'
r = requests.get(base_url)
print(r)
input('hey')
soup = BeautifulSoup(r.text,'html.parser')
print(soup)
filename = input("File to save to: ")

with open(filename, 'w') as f:
  for story_heading in soup.find_all(class_="story-heading"): 
      if story_heading.a: 
          f.write(story_heading.a.text.replace("\n", " ").strip())
      else: 
          f.write(story_heading.contents[0].strip())    