# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 20:56:48 2022

@author: peter
"""
from bs4 import BeautifulSoup 
from requests import get

#%% functions relating to areas
def full_area():
    """
    Generates a list of all the areas available in the finn.no webpage.

    Returns
    -------
    area_list : TYPE
        DESCRIPTION.
        list of all clickable areas on the webpage
        this function takes no input so no filtering is done here.
        Gives all link info (area, num_listings, and link)
    """
    # url of most areas
    url_nesten_alt = "https://www.finn.no/realestate/homes/search.html?location=1.22034.20081&location=1.22034.20086&location=1.22034.20069&location=1.22034.20073&location=1.22034.20078&location=1.22034.20105&location=1.22034.20096&location=1.22034.20085&location=1.22034.20101&location=1.22034.20070&location=1.22034.20063&location=1.22034.20062&location=1.22034.20087&location=1.22034.20084&location=1.22034.20089&location=1.22034.20065&location=1.22034.20106&location=1.22034.20091&location=1.22034.20067&location=1.22034.20103&location=1.22034.20083&location=1.22034.20077&location=1.22034.20094&location=1.22034.20064&location=1.22034.20092&location=1.22034.20088&location=1.22034.20066&location=1.22034.20076&location=1.22034.20102&location=1.22034.20104&location=1.22034.20093&location=1.22034.20068&location=1.22034.20079&location=1.22034.20074&location=1.22034.20080&location=1.22034.20109&location=1.22034.20107&location=1.22034.20098&location=1.22034.20090&location=1.22034.20072&location=1.22034.20075&location=1.22034.20071&location=1.22034.20097&location=1.22034.20095&location=1.22034.20108&location=1.22042.20166&location=1.22042.20172&location=1.22042.20176&location=1.22042.20178&location=1.22042.20175&location=1.22042.20181&location=1.22042.20182&location=1.22042.20170&location=1.22042.20167&location=1.22042.20165&location=1.22042.20191&location=1.22042.20174&location=2.22042.20179.20707&location=2.22042.20179.20536&location=2.22042.20179.20709&location=2.22042.20179.20708&location=2.22042.20179.20734&location=2.22042.20179.20735&location=1.22042.20192&location=1.22042.20171&location=1.22042.20189&location=1.22042.20190&location=1.22042.20164&location=1.22042.20193&location=1.22042.20169&location=1.22042.20177&location=1.22042.20168&location=1.22042.20183&location=1.22042.20173&location=1.22042.20187&location=1.20015.20304&location=1.20015.20314&location=1.20015.20307&location=1.20015.22101&location=1.20015.20297&location=1.20015.20309&location=1.20015.20287&location=1.20015.20285&location=1.20015.22102&location=1.20015.20281&location=1.20015.20280&location=1.20015.20300&location=1.20015.20284&location=1.20015.20317&location=1.20015.20292&location=1.20015.20296&location=1.20015.20311&location=1.20015.20312&location=1.20015.20294&location=1.20015.20310&location=1.20015.20286&location=1.20015.20283&location=1.20015.20299&location=1.20015.20288&location=2.20015.20282.23001&location=2.20015.20282.23004&location=2.20015.20282.23005&location=2.20015.20282.23003&location=2.20015.20282.23002&location=1.20015.20289&location=1.20018.20375&location=1.20018.20410&location=1.20018.20369&location=1.20018.20367&location=1.20018.20371&location=1.20018.20407&location=1.20018.20380&location=1.20018.20399&location=1.20018.20391&location=1.20018.20403&location=1.20018.20388&location=1.20018.20378&location=1.20018.20406&location=1.20018.20395&location=1.20018.20379&location=1.20018.20382&location=1.20018.20374&location=1.20018.20376&location=1.20018.20384&location=1.20018.20397&location=1.20018.20387&location=1.20018.20411&location=1.20018.20368&location=1.20018.20381&location=1.20018.20383&location=1.20018.20386&location=1.20018.20401&location=1.20018.20390&location=1.20018.20409&location=1.20018.20394&location=1.20018.20370&location=1.20018.20393&location=1.20018.20385&location=1.20018.20377&location=1.20018.20372&location=1.20018.20404&location=1.20018.20373&location=1.20018.20405&location=1.20018.20402&location=1.20018.20408&location=1.20061.20528&location=1.20061.20507&location=1.20061.20519&location=1.20061.20515&location=1.20061.20524&location=1.20061.20512&location=1.20061.20529&location=1.20061.20527&location=1.20061.20511&location=1.20061.20523&location=1.20061.20522&location=1.20061.20518&location=1.20061.20520&location=1.20061.20514&location=1.20061.20516&location=1.20061.20526&location=1.20061.20532&location=1.20061.20510&location=1.20061.20513&location=1.20061.20530&location=1.20061.20509&location=1.20061.20525&location=1.20061.20517&location=1.20061.20533&location=1.20061.20508&location=1.20061.20531&location=1.20061.20521&location=1.20012.20200&location=1.20012.20215&location=1.20012.20194&location=1.20012.20204&location=1.20012.20197&location=1.20012.20209&location=1.20012.20201&location=1.20012.20217&location=1.20012.20202&location=1.20012.20214&location=1.20012.20199&location=1.20012.20206&location=1.20012.20195&location=1.20012.20211&location=1.20012.20198&location=1.20012.20205&location=2.20012.20196.20714&location=2.20012.20196.20716&location=2.20012.20196.20733&location=2.20012.20196.20718&location=2.20012.20196.20719&location=2.20012.20196.20720&location=2.20012.20196.20721&location=2.20012.20196.20722&location=2.20012.20196.20723&location=2.20012.20196.20724&location=2.20012.20196.20732&location=2.20012.20196.20712&location=2.20012.20196.20713&location=2.20012.20196.20725&location=2.20012.20196.20726&location=2.20012.20196.20727&location=2.20012.20196.20728&location=2.20012.20196.20729&location=2.20012.20196.20730&location=1.20012.20208&location=1.20012.20210&location=1.20012.20203&location=1.20012.20216&location=1.20012.20218&location=1.20012.20219&location=1.22054.20441&location=1.22054.20429&location=1.22054.20420&location=1.22054.20424&location=1.22054.20450&location=1.22054.20418&location=1.22054.20439&location=1.22054.20412&location=1.22054.20443&location=1.22054.20417&location=1.22054.20448&location=1.22054.20430&location=1.22054.20440&location=1.22054.20414&location=1.22054.20436&location=1.22054.20433&location=1.22054.20419&location=1.22054.20449&location=1.22054.20442&location=1.22054.20431&location=1.22054.20422&location=1.22054.20445&location=1.22054.20453&location=1.22054.20446&location=1.22054.20435&location=1.22054.20447&location=1.22054.20421&location=1.22054.22115&location=1.22054.20434&location=1.22054.20432&location=1.22054.20455&location=1.22054.20423&location=1.22054.20452&location=1.22054.20398&location=2.22054.20413.20815&location=2.22054.20413.20814&location=2.22054.20413.20817&location=2.22054.20413.20816&location=2.22054.20413.20818&location=1.22054.20438&location=1.22054.20437&location=1.20016.20363&location=1.20016.20347&location=1.20016.20322&location=1.20016.20359&location=1.20016.22112&location=1.20016.20321&location=1.20016.20335&location=1.20016.20360&location=1.20016.20354&location=1.20016.20325&location=1.20016.20366&location=1.20016.20349&location=1.20016.20356&location=1.20016.20340&location=1.20016.20337&location=1.20016.20345&location=1.20016.20336&location=1.20016.20344&location=1.20016.20358&location=1.20016.22114&location=1.20016.20330&location=1.20016.22113&location=1.20016.20329&location=1.20016.20361&location=1.20016.20331&location=1.20016.20313&location=1.20016.20334&location=1.20016.20357&location=1.20016.20341&location=1.20016.20338&location=1.20016.20355&location=1.20016.20343&location=1.20016.20346&location=2.20016.20318.20731&location=2.20016.20318.20504&location=2.20016.20318.20501&location=2.20016.20318.20502&location=2.20016.20318.20505&location=1.20016.20342&location=1.20016.20350&location=1.20016.20327&location=1.20016.20323&location=1.22038.20150&location=1.22038.20152&location=1.22038.20161&location=1.22038.20143&location=1.22038.20157&location=1.22038.20132&location=1.22038.20131&location=1.22038.20151&location=1.22038.20135&location=1.22038.22106&location=1.22038.20160&location=1.22038.20153&location=1.22038.20148&location=1.22038.20146&location=1.22038.20134&location=1.22038.20158&location=1.22038.20149&location=1.22038.20147&location=1.22038.20156&location=1.22038.20162&location=1.22038.20133&location=1.22038.20163&sort=PUBLISHED_DESC" 
    #rest of areas
    url_resten = "https://www.finn.no/realestate/homes/search.html?location=2.22046.22109.23026&location=2.22046.22109.23024&location=2.22046.22109.23025&location=1.22046.20267&location=1.22046.20243&location=1.22046.20263&location=1.22046.20240&location=1.22046.20251&location=2.22046.20220.20537&location=2.22046.20220.20465&location=2.22046.20220.20479&location=2.22046.20220.20473&location=2.22046.20220.20475&location=2.22046.20220.20471&location=2.22046.20220.20470&location=1.22046.22108&location=1.22046.20273&location=1.22046.20224&location=1.22046.20232&location=1.22046.20221&location=1.22046.20252&location=1.22046.20226&location=1.22046.20268&location=1.22046.20278&location=1.22046.20255&location=1.22046.20257&location=1.22046.20258&location=2.22046.22107.23022&location=2.22046.22107.23023&location=1.22046.20236&location=1.22046.20228&location=1.22046.20266&location=1.22046.20264&location=1.22046.20253&location=1.22046.20245&location=1.22046.20246&location=1.22046.20238&location=1.22046.20262&location=1.22046.20256&location=1.22046.22111&location=1.22046.20225&location=1.22046.20279&location=1.22046.22110&location=1.22046.20223&location=1.22046.20227&location=1.22046.20231&location=1.22046.20233&location=1.22046.20244&location=1.22046.20259&location=1.22046.20235&location=1.22046.20265&location=1.22046.20248&location=1.22030.20026&location=2.22030.20046.23016&location=2.22030.20046.23018&location=2.22030.20046.23017&location=1.22030.20047&location=1.22030.20045&location=2.22030.20110.23006&location=2.22030.20110.23007&location=2.22030.20110.23008&location=1.22030.20058&location=1.22030.20051&location=1.22030.20128&location=1.22030.20114&location=1.22030.20024&location=1.22030.20042&location=1.22030.20055&location=1.22030.20116&location=1.22030.20021&location=1.22030.20117&location=1.22030.20119&location=1.22030.20113&location=1.22030.20060&location=1.22030.20025&location=2.22030.22103.23011&location=2.22030.22103.23012&location=2.22030.22103.23013&location=2.22030.22103.23010&location=2.22030.22103.23009&location=1.22030.20099&location=1.22030.20111&location=1.22030.20121&location=1.22030.20125&location=2.22030.22105.23020&location=2.22030.22105.23021&location=2.22030.22105.23019&location=1.22030.20100&location=1.22030.20052&location=1.22030.20027&location=1.22030.20122&location=1.22030.20022&location=1.22030.20059&location=1.22030.20057&location=1.22030.20115&location=1.22030.20043&location=1.22030.20054&location=2.22030.22104.23015&location=2.22030.22104.23014&location=1.22030.20130&location=1.22030.20034&location=1.22030.20112&location=1.22030.20129&location=1.22030.20035&location=1.22030.20050&location=1.22030.20023&location=1.22030.20120&location=1.22030.20033&location=1.22030.20056&location=1.22030.20039&location=1.22030.20037&location=1.22030.20118&location=1.22030.20041&location=1.22030.20123&sort=PUBLISHED_DESC"
    
    #getting the site and creating bs object
    site = get(url_nesten_alt)
    bs = BeautifulSoup(site.content, "html.parser")
    
    #init empty list
    area_list_1 = []
    
    #finding all areas
    for area in bs.find_all('div', class_="input-toggle"):
    
        key = area.text.split(" ")
        val = area.find('input').attrs['id']
        area_list_1.append([key, val])
        
    #cleaning up everything that is not a area    
    for i, area in enumerate(area_list_1):
        if area[0][0] == 'Nye':
            area_list_1[i] = False
        if area[0][0] == "Vestland":
            del area_list_1[i:]
            break
    
    #rest is same but for other url
    site = get(url_resten)
    bs = BeautifulSoup(site.content, "html.parser")
    
    area_list_2 = []
    
    for area in bs.find_all('div', class_="input-toggle"):
    
        key = area.text.split(" ")
        val = area.find('input').attrs['id']
        area_list_2.append([key, val])
    
    to_remove = ['Agder', 'Innlandet', 'Møre', 'Nordland', 'Oslo', 'Rogaland', 'Troms', 'Trøndelag', 'Vestfold']
    
    for i, area in enumerate(area_list_2):
    
        if area[0][0] == 'Nye':
            area_list_2[i] = False
        if area[0][0] in to_remove:
            area_list_2[i] = False
    
        if area[0][0] == "Til":
            del area_list_2[i:]
            break
    
    # adding the lists and removing false
    area_list = area_list_1 + area_list_2
    area_list = [x for x in area_list if x != False]
        
    #returns the list
    return area_list

def get_only_areas(area_list):
    """
    

    Parameters
    ----------
    area_list : TYPE
        DESCRIPTION.
        takes the information from full_area
    Returns
    -------
    TYPE
        DESCRIPTION.
        cleaned list of only areas

    """
    import itertools
    #cleaning up the list and returning only areas
    get_area_list = area_list.copy()
    for i, area in enumerate(get_area_list):
         get_area_list[i] = area[0][:-1]
         get_area_list[i] = ["".join(get_area_list[i])]
    return list(itertools.chain(*get_area_list))
         
def get_num_listings(area_list):
    """

    Parameters
    ----------
    area_list : TYPE
    list
        DESCRIPTION.
        list from full area

    Returns
    -------
    num_listing_list : TYPE
    list
        DESCRIPTION.
        number of listings

    """
    num_listing_list = area_list.copy()
    for i, area in enumerate(num_listing_list):
        num_listing_list[i] = area[0][-1]
        num_listing_list[i] = num_listing_list[i].replace("(", "").replace(")", "").replace("\xa0","")
        num_listing_list[i] = int(num_listing_list[i])
    return num_listing_list

def get_loc_code(area_list):
    """

    Parameters
    ----------
    area_list : TYPE
    full list
        DESCRIPTION.

    Returns
    -------
    loc_list : TYPE
    list
        DESCRIPTION.
        gets a list of all the location links

    """
    loc_list = area_list.copy()
    for i, area in enumerate(loc_list):
        loc_list[i] = area[1].replace("-", "=")
        
    return loc_list

def zipped_list(area_list):
    """

    Parameters
    ----------
    area_list : TYPE
    list
        DESCRIPTION.

    Returns
    -------
    full_list : TYPE
    list
        DESCRIPTION.
        returns a cleaner format

    """
    zip_copy = area_list.copy()
    full_list = []
    area = get_only_areas(zip_copy)
    num_listings = get_num_listings(zip_copy)
    loc_code = get_loc_code(zip_copy)
    for area_, listing, loc in zip(area, num_listings, loc_code):
        full_list.append([area_, listing, loc])

    return full_list

#%% functions relating to new/used



if __name__ == "__main__":
    area_list = full_area()
    only_areas = get_only_areas(area_list)
    loc_list = get_loc_code(area_list)
    num_list = get_num_listings(area_list)
    zl = zipped_list(area_list)



    


    
    