from typing import Text
import requests


tl_url = "https://jujutsu-kaisen.online"


def get_source(_tl_url):
    r = requests.get(_tl_url)
    r_source = r.text
    return r_source.split('<li id="su-post')

urls = []
for row in get_source(tl_url):
        urls.append(row)
        

for i in range(1, len(urls)):
    urls[i] = urls[i].split('href="')[1]
    urls[i] = urls[i].split('">')[0]
    if "Chapter 1" in urls[i]:
        urls[i] = urls[i].split("</li>")[0]
        

        
    print(urls[i])
        

 


