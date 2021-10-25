from typing import Text
import requests


tl_url = "https://jujutsu-kaisen.online"


def get_source(_tl_url):
    r = requests.get(_tl_url)
    r_source = r.text
    return r_source.split('<a href=')

urls = []
for row in get_source(tl_url):
        urls.append(row)
        

def trim(_urls, _start, _end, chapter=False):
    for i in range(1, len(_urls)):
        if chapter:
            
            
            
        _urls[i] = _urls[i].split(_start)[1]
        _urls[i] = _urls[i].split(_end)[0]
        if(i == len(_urls)):
            
                
                
  
  
  
  
            
for i in range(1, len(urls)):
    urls[i] = urls[i].split('href="')[1] #everything after href
    urls[i] = urls[i].split('">')[0] # everything before ">
    if "Chapter 1" in urls[i]:
        urls[i] = urls[i].split("</li>")[0]
    for j in range(0, i):
        if urls[i] in urls[j]:
            urls[i] = urls[i] + "$"
x = 1                       
for i in range(1, len(urls)):
    if "$" in urls[i]:
        x = x + 1

for k in range(len(urls) - 1, (len(urls) - x), -1):
    urls.remove(urls[k])


for i in range(1, len(urls)):
     source = get_source(urls[i]) 
        

    
    

        

 


