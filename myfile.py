from typing import Text
import requests
from requests.api import get


tl_url = "https://jujutsu-kaisen.online/"

#get source text
def get_source(_tl_url):
    r = requests.get(_tl_url)
    return r.text

#split by link beginning
def split_src(_src, _split):
    return _src.split(_split)
    

#put items in array
chapter_links = []
for row in split_src(get_source(tl_url), '"><a href="h'): #inadvertadley removes the first h in https://
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
        src = get_source(_urls_list[i])
        if "wp-block-image" in src:
            src = split_src(src, '"wp-block-image"><img src="')
            for j in len(src):
                pass
        
        # for i in range(1, len(_img_links)):
        #     _img_links[i] = _img_links[i].split('" alt=')[0] # everything before " alt=
        #     print(i)
        
    
print(trim(chapter_links))
get_imgs(trim(chapter_links))
                       
    
    
                    

