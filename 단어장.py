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
        
    baseUrl_1 = 'https://dic.daum.net/search.do?q='
    baseUrl_2 = 'https://www.merriam-webster.com/dictionary/'
    plusUrl = input('검색어를 입력하세요: ')
    url_1 = baseUrl_1 +urllib.parse.quote_plus(plusUrl)
    url_2 = baseUrl_2 +urllib.parse.quote_plus(plusUrl) 
    html_1 = urllib.request.urlopen(url_1).read()
    html_2 = urllib.request.urlopen(url_2).read()
    soup_1 = BeautifulSoup(html_1, 'html.parser')
    soup_2 = BeautifulSoup(html_2, 'html.parser')

    #try:
    if (plusUrl == "1"):
        break
            
    z = str(soup_2.select_one("span.dtText").get_text()).split(':')
    a = str(soup_1.select("span.txt_search"))
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
            
    print("영영풀이 :",str(z[1]).lstrip())
    t.append(z[1])    
    x.append(t)
    k = y + '.xlsx'
    wb.save(k)

    #except:
     #   continue



#a = soup.select_one("span.txt_search").get_text()


  

    
    
        
    
        
   

    





