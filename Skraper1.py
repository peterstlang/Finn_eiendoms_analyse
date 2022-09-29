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
for listing in bs.find_all('article', 
                           class_="relative overflow-hidden transition-all outline-none sf-ad-outline sf-ad-card rounded-8 mt-24 mx-16 mb-16 sm:mb-24 relative"):
    #print(offer.stripped_strings)
    print(listing.prettify())
    #print("\n")
    #print("\n")
    
    #tst = [text for text in listing.stripped_strings]
    #lst.append(tst)
    
    footer = listing.find('div', class_="col-span-2 mt-16 sm:mt-4 flex justify-between sm:block space-x-12 font-bold")
    location = listing.find('span', class_="text-14 text-gray-500")
    location = location.text
    print(type(location))

    tst = [t for t in footer.stripped_strings]
    tst[1].replace('\\xa', ' ')
    m_square = tst[0]
    price = tst[1]
    print(m_square, price)
    

    


    
    

