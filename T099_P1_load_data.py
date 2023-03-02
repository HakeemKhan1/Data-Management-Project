import string 
from typing import List 
#Function Definition 
def book_catagory_dictionary(files: str):
    
    """
    Returns the books in each catagory 
    >>> book_catagory_dictionary("google_books_dataset.csv") 
    Fiction
{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': '3.3', 'publisher': 'Kensington Publishing Corp.', 'pages': '288', 'language\n': 'English\n'}
    
    """
    file = open(files, "r")
    count = 0
    dictionary = {}
    temp = []
    res = dict()
    
    for line in file:
        row = line.split(",")
        
    
        if count == 0:
            header = row
            
        else:
            if not (row[5] in dictionary) :
                dictionary[row[5]] = []
            
            book = {}
            book[header[0]] = row[0]
            book[header[1]] = row[1]
            if row[2] != 'N/A':
                book[header[2]] = float(row[2])
            else:
                book[header[2]] = row[2]
            book[header[3]] = row[3]
            book[header[4]] = row[4]
            book[header[6]] = row[6]
            added=False
            for key in dictionary[row[5]]:
                if book[header[0]] == key['title']:
                    added=True
            if added == False:
                dictionary[row[5]].append(book)
        count += 1
        
   
    file.close()
    return dictionary  

