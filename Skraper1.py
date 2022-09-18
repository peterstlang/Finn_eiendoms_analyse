# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 20:22:42 2022

@author: peter
"""

#imports
from bs4 import BeautifulSoup 
from requests import get

#getting url
url = "https://www.finn.no/realestate/homes/search.html?sort=PUBLISHED_DESC"

site = get(url)

#print(site.content, "html.parser")

#teste
bs = BeautifulSoup(site.content, "html.parser")


lst = []
for offer in bs.find_all('div', class_='col-span-2 mt-16 sm:mt-4 flex justify-between sm:block space-x-12 font-bold'):
    #print(offer.stripped_strings)
    #print(offer)
    tst = [text for text in offer.stripped_strings]
    lst.append(tst)

    
    



    
    

