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
        ('Agder','0.22042'): {
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
            ('Kristiansand','.20179'):{
                'Kristiansand Nord':'.20707',
                'Kristiansand Sentrum':'.20536',
                'Kristiansand Vest':'.20709',
                'Kristiansand Øst':'.20708',
                'Sogndalen':'.20734',
                'Søgne':'.20735'}, #her er det mer nøsting se på senere
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
    
    def add_1_area_code(self):
        for k in self.sub_area_dict.keys():
            code = list(k[1])
            num = int(code[0])
            num += 1
            code[0] = str(num)
            code = ''.join(code)
        return code

################################################################################
# Hele den biten her burde kaaaanskje være et eget bibliotek, ettersom det
# bare er prepross idk
################################################
    # steg 1
    def give_dict(self):
        return self.sub_area_dict
            
    # steg 2
    # tatt fra denne linken:
    # https://thispointer.com/python-how-to-iterate-over-nested-dictionary-dict-of-dicts/
    def ndi(self, dict_obj):
        for k, v in dict_obj.items():
            if isinstance(v, dict):
                for pair in  self.ndi(v):
                    yield (k, *pair)
            else:
                yield (k, v)
                
    # steg 3
    def create_lst(self, generator_obj):
        pair_list = []
        for pair in all_pairs:
            pair_list.append(list(pair))
        
        main_lst = []
        for lst in pair_list:
            x = []
            for ele in lst:
                if isinstance(ele, tuple):
                    x.extend(ele)
                else:
                    x.append(ele)
            main_lst.append(x)
        return main_lst
        
    
    
    
        
        
if __name__ == "__main__":
    obj = FinnSkraper(area=['Oslo', 'Innlandet'])
    url = obj.set_url()
    obj.add_1_area_code()
    dict_obj = obj.give_dict()
    all_pairs = list(obj.ndi(dict_obj))
    main_l = obj.create_lst(all_pairs)