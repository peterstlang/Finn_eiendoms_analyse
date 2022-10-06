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
    
    sub_area_dict = {
        'Agder': {
            'Arendal':'.20166',
            'Birkenes':'.20172',
            'Bygland':'.20176',
            'Bykle':'.20178',
            'Evje og Hornnes':'.20175',
            'Farsund':'.20181',
            'Flekkefjord':'.20182',
            'Froland':'.20170',
            'Gjerstad':'.20167',
            'Grimstad':'.20165',
            'Hægebostad':'.20191',
            'Iveland':'.20174',
            'Kristiansand':'.20179', #her er det mer nøsting se på senere
            'Kvinesdal':'.20192',
            'Lillesand':'.20171',
            'Lindesnes':'.20189',
            'Lyngdal':'.20190',
            'Risør':'.20164',
            'Sirdal':'.20193',
            'Tvedestrand':'.20169',
            'Valle':'.20177',
            'Vegårshei':'.20168',
            'Vennesla':'.20183',
            'Åmli':'.20173',
            'Åseral':'.20187'
            }}
    
    #https://thispointer.com/python-how-to-iterate-over-nested-dictionary-dict-of-dicts/
    #Dette er en nice link for problemet hehe
    def __init__(self, area=[]):
        if not isinstance(area, list):
            raise TypeError('area must be in a list')
        self.area = area
        
    def set_url(self):
        """Creating url based on options chosen by the user (only area as 
        of now), these selections alter the link. Based on what areas 
        the user wants the link is altered thereafter"""
        
        if self.area == []:
            return "https://www.finn.no/realestate/homes/search.html?sort=PUBLISHED_DESC"
        
        link_1 = "https://www.finn.no/realestate/homes/search.html?"
        link_2 = "sort=PUBLISHED_DESC"

        for area in self.area:
            if area not in self.area_dict:
                raise ValueError('must be a valid area')
            link_1 += "location=" + self.area_dict[area] + "&"
        return link_1 + link_2
            
            
        
        
if __name__ == "__main__":
    obj = FinnSkraper(area=['Oslo', 'Innlandet'])
    url = obj.set_url()
        