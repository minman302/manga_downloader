from typing import Text
import requests
from requests.api import get


tl_url = "https://jujutsu-kaisen.online/"

#get source text and split by link beginning
def get_source(_tl_url, _split):
    r = requests.get(_tl_url)
    r_source = r.text
    return r_source.split(_split) #split the source at the specified string
    


#put items in array
chapter_links = []
for row in get_source(tl_url, '"><a href="h'): #inadvertadley removes the first h in https://
        chapter_links.append("h" + row) #adds back that h to the url
        
        
    
def trim(_urls):
    del _urls[0]

    for i in range(0, len(_urls)):
        _urls[i] = _urls[i].split('/">')[0] # everything before ">
            
        if "chapter-1" in _urls[i]:
            _urls[i] = _urls[i].split("</li>")[0]
            
            
        for j in range(0, i):
            if _urls[i] == _urls[j]:
                _urls[i] = _urls[i] + "$"
    x = 1                       
    for i in range(0, len(_urls)):
        if "$" in _urls[i]:
            x = x + 1

    for k in range(len(_urls) - 1, (len(_urls) - x), -1):
        _urls.remove(_urls[k])
        

    return _urls
                    
 
def get_imgs(_urls_list):
    for i in range(0, len(_urls_list)):
        _img_links = []
        if "wp-block-image" in 
        for row in get_source(_urls_list[i], 'class="aligncenter" src="'):
            _img_links.append(row)
            
        print(len(_img_links))
        # for i in range(1, len(_img_links)):
        #     _img_links[i] = _img_links[i].split('" alt=')[0] # everything before " alt=
        #     print(i)
        
    
print(type(trim(chapter_links)))   
get_imgs(trim(chapter_links))    
                       
    
    
                    

