# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 01:07:08 2022

@author: peter
"""
from bs4 import BeautifulSoup 
from requests import get

class FinnSkraper:
    
    area_dict = {
        'Agder':'0.22042',
        'Innlandet':'0.22034',
        'Møre og Romsdal':'0.20015',
        'Nordland':'0.20018',
        'Oslo':'0.20061',
        'Rogaland':'0.20012',
        'Troms og Finnmark':'0.22054',
        'Trøndelag':'0.20016',
        'Vestfold og Telemark':'0.22038',
        'Vestland':'0.22046',
        'Viken':'0.22030'
    }
    
    def __init__(self, area=None):
        try:
            self.area = self.area_dict[area]
        except:
            self.area = area
        
    def set_url(self):
        if self.area == None:
            return "https://www.finn.no/realestate/homes/search.html?sort=PUBLISHED_DESC"
        else:
            frag_1 = "https://www.finn.no/realestate/homes/search.html?location="
            frag_2 = "&sort=PUBLISHED_DESC"
            return frag_1 + str(self.area) + frag_2
        
        
if __name__ == "__main__":
    obj = FinnSkraper(area='Oslo')
    url = obj.set_url()
        