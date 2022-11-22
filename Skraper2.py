# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 19:59:06 2022

@author: peter
"""
# plan is to use a link from "link_lager" in order to scrape

# Objective of this script

# main function to run the script

#importing "link_lager"
from link_lager import createlink

def link_to_scrape():
    obj = createlink(areas=['Bøler', 'GAMLEOslo',
                            'Grorud', 'Røa', 'sentrum'], 
                     is_new_property=True)
    return obj.get_link()

def main():
    link = link_to_scrape()
    return link
    

if __name__ == "__main__":
    link = main()