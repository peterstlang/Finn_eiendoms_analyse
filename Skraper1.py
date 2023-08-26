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


lst = []
for listing in bs.find_all('article', 
                           class_="relative overflow-hidden transition-all outline-none sf-ad-outline sf-ad-card rounded-8 mt-24 mx-16 mb-16 sm:mb-24 relative"):
    #print(offer.stripped_strings)
    #print(listing.prettify())
    #print("\n")
    #print("\n")
    
    #tst = [text for text in listing.stripped_strings]
    #lst.append(tst)
    
    footer = listing.find('div', class_="col-span-2 mt-16 sm:mt-4 flex justify-between sm:block space-x-12 font-bold")
    location = listing.find('span', class_="text-14 text-gray-500")
    location = location.text
    location = location.split(',')
    address = location[0]
    addloc = location[1]

    tst = [t for t in footer.stripped_strings]
    tst[1].replace('\\xa', ' ')
    m_square = tst[0]
    price = tst[1]
    print(m_square, price, address, addloc)
    
    break

if __name__ == "__main__":
    #imports i guess
    #imports
    from bs4 import BeautifulSoup 
    from requests import get
    #eget bibliotek hehe
    from link_lager import createlink
    
    obj = createlink(areas=['Bøler', 'GAMLEOslo', 'Grorud', 'Røa', 'sentrum'], is_new_property=True)
    obj.areas
    link = obj.get_link()
    #print(link)
    
    # test link
    site = get(link)

    #print(site.content, "html.parser")

    #teste
    bs = BeautifulSoup(site.content, "html.parser")
    
    # tellevariabler som hjelper meg med å se
    # hvor mange instanser som ikke inneholder infoen jeg ønsker
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
    print("Det var {} annonser som ble hoppet over:".format(ctr))
    # lst = []
    # for listing in bs.find_all('article', 
    #                            class_="relative overflow-hidden transition-all outline-none sf-ad-outline sf-ad-card rounded-8 mt-24 mx-16 mb-16 sm:mb-24 relative"):
    #     #print(offer.stripped_strings)
    #     #print(listing.prettify())
    #     #print("\n")
    #     #print("\n")
        
    #     #tst = [text for text in listing.stripped_strings]
    #     #lst.append(tst)
        
    #     footer = listing.find('div', class_="col-span-2 mt-16 sm:mt-4 flex justify-between sm:block space-x-12 font-bold")
        # location = listing.find('span', class_="text-14 text-gray-500")
        # location = location.text
        # location = location.split(',')
        # address = location[0]
        # addloc = location[1]

        # tst = [t for t in footer.stripped_strings]
        # tst[1].replace('\\xa', ' ')
        # m_square = tst[0]
        # price = tst[1]
        # print(m_square, price, address, addloc)
        




    
    

