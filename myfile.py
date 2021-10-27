from typing import Text
import requests
from requests.api import get


tl_url = "https://jujutsu-kaisen.online"

#get source text and split by link beginning
def get_source(_tl_url):
    r = requests.get(_tl_url)
    r_source = r.text
    return r_source.split('"><a href="h') #remove first h in https://... for sorting purposes
    


#put items in array
links = []
for row in get_source(tl_url):
        links.append("h" + row) #adds back that h to the url
        
        
    
def trim(_urls, chapter=False):
    _list = _urls
    if chapter:
        for i in range(1, len(_list)):
            jpgs = []
            for row in get_source(_list[i]):
                jpgs.append("h" + row)
            #download jpgs
            
        pass
    else:
        for i in range(1, len(_list)):
            _list[i] = _list[i].split('/">')[0] # everything before ">
            
            if "chapter-1" in _urls[i]:
                _list[i] = _list[i].split("</li>")[0]
            
            
            for j in range(0, i):
                if _list[i] == _list[j]:
                    _list[i] = _list[i] + "$"
    x = 1                       
    for i in range(1, len(_urls)):
        if "$" in _list[i]:
            x = x + 1

    for k in range(len(_list) - 1, (len(_list) - x), -1):
        _urls.remove(_list[k])
        

    return _list
                    
 
                    
    
        
    
                    

print(trim(trim(links), chapter=False)[])
