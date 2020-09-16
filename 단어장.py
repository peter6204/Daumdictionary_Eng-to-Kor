import urllib.request
import urllib.parse
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import openpyxl
import random
import numpy as np
import re

x = str(random.random())
y = str(random.randrange(1,1000))
wb = openpyxl.Workbook()
x = wb.active


while (1): 
        
    baseUrl = 'https://dic.daum.net/search.do?q='
    plusUrl = input('검색어를 입력하세요: ')
    url = baseUrl +urllib.parse.quote_plus(plusUrl) 
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    try:
        if (plusUrl == "1"):
            break

        a = str(soup.select("span.txt_search"))
        b = a.split(',')
        t = []
        t.append(plusUrl)
       

        for i in range(0,4,1):
            c = b[i]
            hangul = re.compile('[^ \u3131-\u3163\uac00-\ud7a3]+')
            result = hangul.sub('',c).replace(" ", "")  
            print("%d." % (i+1),result )            
            t.append(result)

            if result == '':
                continue
            
            
        x.append(t)
        k = y + '.xlsx'
        wb.save(k)

    except:
        continue



#a = soup.select_one("span.txt_search").get_text()


  

    
    
        
    
        
   

    





