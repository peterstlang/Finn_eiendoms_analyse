# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 20:22:42 2022

@author: peter
"""

#imports
from bs4 import BeautifulSoup 
from requests import get
#eget bibliotek hehe
from link_lager import createlink


# dict of areas
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

area_dict['Oslo']

#getting url
#IKKE FERDIG
def set_url(area=None, codes=area_dict):
    if area==None:
        site = "https://www.finn.no/realestate/homes/search.html?sort=PUBLISHED_DESC"
        return site
    else:
        frag_1 = "https://www.finn.no/realestate/homes/search.html?location="
        frag_2 = "&sort=PUBLISHED_DESC"
        site = frag_1 + str(codes[area]) + frag_2
    return site
    
    

url = set_url()


site = get(url)

#print(site.content, "html.parser")

#teste
bs = BeautifulSoup(site.content, "html.parser")

def get_rows(bs, check_skipped=False):
    ctr = 0
    
    for listing in bs.find_all('article', 
                               class_="relative isolate sf-search-ad cursor-pointer overflow-hidden relative transition-all outline-none f-card rounded-8 grid f-grid grid-cols-2 bg-white"):

        footer = listing.find('div', class_="col-span-2 mt-16 flex justify-between sm:mt-4 sm:block space-x-12 font-bold whitespace-nowrap")
        #hopper over de som ikke har korrekt informasjon
        if footer == None:
            ctr += 1
            continue
        location = listing.find('span', class_="text-14 text-gray-500")
        location = location.text
        location = location.split(',')
        address = location[0]
        addloc = location[1]
        
        tst = [t for t in footer.stripped_strings]
        tst[1].replace('\\xa', ' ')
        m_square = tst[0]
        price = tst[1]
        
        # Gir meg informasjon kvadratmeter, pris (en range), adresse, og sted
        print(m_square, price, address, addloc)
        print("\n")
        
    if check_skipped == True:
        print("Det var {} annonser som ble hoppet over:".format(ctr))
    

if __name__ == "__main__":
    #imports i guess
    #imports
    from bs4 import BeautifulSoup 
    from requests import get
    #eget bibliotek hehe
    from link_lager import createlink
    
    obj = createlink(areas=['Oslo'], is_new_property=True)
    obj.areas
    baseurl = obj.get_link()
    
    # test link
    site = get(baseurl)

    #print(site.content, "html.parser")

    #teste
    bs = BeautifulSoup(site.content, "html.parser")
    
    ctr = 1
    populated = True
    
    while populated:
        if ctr > 1:
            link = str(baseurl) + "&page={}".format(ctr)
            site = get(link)
            bs = BeautifulSoup(site.content, "html.parser")
        tester = bs.find("h2", class_="u-t3 u-pa16 u-text-center")
        if tester is None:
            get_rows(bs, check_skipped=True)
        elif tester.text == "Ingen treff akkurat nå":
            populated = False
        ctr += 1
        
        
    
    
    # for listing in bs.find_all('div', 
    #                            class_="u-hide-lt768"):
    #     #get link
    #     link = obj.get_link()
    #     site = get(link)
    #     bs = BeautifulSoup(site.content, "html.parser")
        
    #     if ctr > 1:
    #         link = str(link)+"page={}".format(ctr)
    #     tst = listing.find('a', attrs={"aria-label": "Side {}".format(ctr)})
    #     print(tst)
    #     ctr += 1
    
    
    
    get_rows(bs, check_skipped=True)
    
    # tellevariabler som hjelper meg med å se
    # hvor mange instanser som ikke inneholder infoen jeg ønsker
    
    tst_link = "https://www.finn.no/realestate/homes/search.html?is_new_property=true&location=0.20061&page=7&sort=PUBLISHED_DESC"
    site = get(tst_link)
    soup = BeautifulSoup(site.content, "html.parser")
    
    tester = soup.find("h2", class_="u-t3 u-pa16 u-text-center")
    print(tester.text) 




    
    

