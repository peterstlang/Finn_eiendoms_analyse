# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 21:33:26 2022

@author: peter
"""
class createlink:
    
    @staticmethod
    def clean_list(area_list):
        for i, area in enumerate(area_list):
            area_list[i] = area_list[i].lower().replace(" ", "")
            area_list[i] = area_list[i].replace("/", "").replace("(", "").replace(")", "")
            area_list[i] = area_list[i].replace("-", "").replace(".", "").replace(",", "")
        return area_list
    
    @staticmethod
    def clean_string(string):
        string = string.lower().replace(" ", "")
        string = string.replace("/", "").replace("(", "").replace(")", "")
        string = string.replace("-", "").replace(".", "").replace(",", "")
        return string
    
        
    
    def __init__(self, areas=[], is_new_property=None):
        """
        initialize the link class. need areas in list form

        Parameters
        ----------
        areas : TYPE, list
            DESCRIPTION. The default is [].

        Raises
        ------
        TypeError
            raises typeerror if areas != a list
        ValueError
            if area is not a valid area

        Returns
        -------
        None.

        """
        # import a library I created hehe
        import getting_areas as gt
        # using library to make variables
        self.full_list = gt.full_area()
        self.area_list = self.clean_list(gt.get_only_areas(self.full_list))
        self.loc_list = gt.get_loc_code(self.full_list)
        self.areas = areas
        
        
        # is new property var
        self.is_new_property = is_new_property
        
        # url variables for links
        self.url_1 = "https://www.finn.no/realestate/homes/search.html?"
        self.is_new_property_link = ""
        self.url_2 = "sort=PUBLISHED_DESC"
                
        # checking if input is list
        if not isinstance(areas, list):
            raise TypeError("areas must be a list!")
            
        # if list is not empty, checking whether the areas are valid
        # cleaning functions should catch most, as long as its spelled correctly
        if len(areas) > 0:
            for i, area in enumerate(self.areas):
                self.areas[i] = self.clean_string(area)
                if self.areas[i] not in self.area_list:
                   raise ValueError("{} is not a valid area!".format(area))
        
        
        if self.is_new_property is not None:
            if not isinstance(is_new_property, bool):
                raise TypeError("if not None then Bool!")
            self.is_new_property_link = "is_new_property="
            if self.is_new_property == True:
                self.is_new_property_link += "true&"
            else:
                self.is_new_property_link += "false&"
                
            
        

    def get_link(self):
        #gets link based on areas chosen
        for area in self.areas:
            idx = self.area_list.index(area)
            loc = self.loc_list[idx] + "&"
            self.url_1 += loc
        return self.url_1 + self.is_new_property_link + self.url_2
                    
    
                    
    
        

        
if __name__ == "__main__":
    obj = createlink(areas=['Bøler', 'gamle Oslo', 'Grorud', 'Røa', 'sentrum'],is_new_property=True)
    obj.areas
    link = obj.get_link()





    
    
