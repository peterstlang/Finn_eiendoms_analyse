# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 19:59:06 2022

@author: peter
"""
# plan is to use a link from "link_lager" in order to scrape

# Objective of this script
# needs functionality to get link from link_lager
# creates a function to get desired link
# needs to scrape said link and retrieve some information
# information should be prisantydning, kvadratmeter, adresse and 
# probably from which area it is, also unique code

# The scraper should be able scrape all listings and stop when its done
# possibly by if test?

# areas should maybe even be divided into a loop?

# Will begin by focusing on listings, as going in and checking for
# each apartment might be tricky
# Stop if you get no hits or page exceeds 50

# add results in to a database
# Creating and appending results to a db should probably be its own file
# or function
# Also needs a check to make sure its not already in db

#

# main function to run the script

# imports
from link_lager import createlink
from bs4 import BeautifulSoup 
from requests import get

def get_link():
    obj = createlink(areas=['Bøler', 'GAMLEOslo',
                            'Grorud', 'Røa', 'sentrum'], 
                     is_new_property=True)
    link = obj.get_link()
    return link
    
def scrape_link(url):
    site = get(url)
    

if __name__ == "__main__":
    link = get_link()