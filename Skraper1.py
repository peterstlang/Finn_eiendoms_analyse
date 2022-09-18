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

print(site.content, "html.parser")

#teste
bs = BeautifulSoup(site.content, "html.parser")

for offer in bs.find_all('article', class_="relative overflow-hidden transition-all outline-none sf-ad-outline sf-ad-card rounded-8 mt-24 mx-16 mb-16 sm:mb-24 relative"):
    print(offer)
    break

