# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 20:56:48 2022

@author: peter
"""
from bs4 import BeautifulSoup 
from requests import get

url_innlandet = "https://www.finn.no/realestate/homes/search.html?location=1.22034.20081&location=1.22034.20086&location=1.22034.20069&location=1.22034.20073&location=1.22034.20078&location=1.22034.20105&location=1.22034.20096&location=1.22034.20085&location=1.22034.20101&location=1.22034.20070&location=1.22034.20063&location=1.22034.20062&location=1.22034.20087&location=1.22034.20084&location=1.22034.20089&location=1.22034.20065&location=1.22034.20106&location=1.22034.20091&location=1.22034.20067&location=1.22034.20103&location=1.22034.20083&location=1.22034.20077&location=1.22034.20094&location=1.22034.20064&location=1.22034.20092&location=1.22034.20088&location=1.22034.20066&location=1.22034.20076&location=1.22034.20102&location=1.22034.20104&location=1.22034.20093&location=1.22034.20068&location=1.22034.20079&location=1.22034.20074&location=1.22034.20080&location=1.22034.20109&location=1.22034.20107&location=1.22034.20098&location=1.22034.20090&location=1.22034.20072&location=1.22034.20075&location=1.22034.20071&location=1.22034.20097&location=1.22034.20095&location=1.22034.20108&sort=PUBLISHED_DESC"

site = get(url_innlandet)

bs = BeautifulSoup(site.content, "html.parser")

for area in bs.find_all()