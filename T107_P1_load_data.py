
#Created by: Matt Turner: 101169414
#Reviewed by: Pietro Adamvoski: (101238885) - Arnie Nambiar: (101183154) - Richard Ofordile: (101190357)


#Functions
import string
from typing import List

def book_dictionary_category_list(filename: str) -> dict: #Case 1
    """Returns a dictionary of a data set containing google books and sorts them 
    by author
    
    book_dictionary_category_list()
    >>>"Fiction":[ {"title": "Antiques Roadkill: A Trash 'n' Treasures Mystery",
    "author": " Barbara Allan",
    "language ": "English",
    "rating": 3.3,
    "publisher": " Kensington Publishing Corp.",
    "pages": 288
    
    
    """
    infile = open(filename, "r")
    
    count=0
    book_dic={}
    for line in infile:
        
        category=line.split(",")
        if count==0:
            category1=category
        else:     
            lst=[]
            if not(category[5] in book_dic):
                book_dic[category[5]]=lst
   
            dic={}
            dic[category1[0]] = category[0]
            dic[category1[1]] = category[1]
            if category[2]!='N/A':
                dic[category1[2]]=float(category[2])
            else:
                dic[category1[2]]=category[2]
            dic[category1[3]] = category[3]
            dic[category1[4]] = category[4]
            dic[category1[6]] = category[6].strip("\n")
            book_dic[category[5]].append(dic)
                                       
        count+=1
        
    infile.close()
    
    return book_dic



