#Team identifier: T099, Members: Hakeem Khan, Art Galaites, Gianluca Fazio, Zachary Goddard
#Art Galaites 101224188 
#Hakeem Khan 101233039
import string
from typing import List
from T099_P5_load_data import book_catagory_dictionary

#The four functions from P3 – Task 1 (and extra function that arise from refactoring)

def dictionary_to_list(dictionary:dict):
    dictlist = []
    for books in dictionary:
        for key in dictionary[books]:
            key_added = True
            for index in dictlist:
                if index['title'] == key['title']:
                    key_added = False
                    index['category'].append(books)
            if key_added == True:
                    category = key
                    category['category'] = [books]
                    dictlist.append(category)    
    return dictlist
#Function 1: Art Galaites 101224188
def sort_books_title(x: list)-> list:
    """
    Returns all books sorted by title in alphabetical order
    >>>[{"title" : "The Essentials of Finance and Accounting for Nonfinancial Managers","author" : "Edward Fields", "language": "English", "rating" : "N/A","publisher": "AMACOM", "category" : "Business", "pages": 320},{"title" : "Watching (The Making of Riley Paige Book 1)","author": "Blake Pierce","rating" : 4.6,"language": "English","publisher": "Blake Pierce","category" : "Detective","pages": 250},{"title" : "Sunshine","author" : "Zimmy Smith","language": "English","rating" : 5.0,"publisher": " Publish Co.","category" : "Fiction","pages": 288},{"title": "We","author": "Yevgeny Zamyatin","language": "English","rating": 4.3,"publisher": "Pan","category": "Fiction","pages": 226}],[{"title" : "Young Justice Vol. 1","author" : "Art Baltazar","language": "English","rating" : 4.1,"publisher": "DC","category" : "Superhero","pages": 164}], [{"title" : "And Then There Were None","author" : "Agatha Christie","language": "English","rating" : 4.6,"publisher": "HarperCollins UK","category" : "Detective","pages": 115}]
    
    [{"title" : "And Then There Were None","author" : "Agatha Christie","language": "English","rating" : 4.6,"publisher": "HarperCollins UK","category" : "Detective","pages": 115}],{"title" : "Sunshine","author" : "Zimmy Smith","language": "English","rating" : 5.0,"publisher": " Publish Co.","category" : "Fiction","pages": 288},[{"title" : "The Essentials of Finance and Accounting for Nonfinancial Managers","author" : "Edward Fields", "language": "English", "rating" : "N/A","publisher": "AMACOM", "category" : "Business", "pages": 320},{"title" : "Watching (The Making of Riley Paige Book 1)","author": "Blake Pierce","rating" : 4.6,"language": "English","publisher": "Blake Pierce","category" : "Detective","pages": 250},{"title": "We","author": "Yevgeny Zamyatin","language": "English","rating": 4.3,"publisher": "Pan","category": "Fiction","pages": 226}],[{"title" : "Young Justice Vol. 1","author" : "Art Baltazar","language": "English","rating" : 4.1,"publisher": "DC","category" : "Superhero","pages": 164}]
    
    """
    for y in range(1, len(x)):  
        unit=x[y]
        z=y-1
        while z >= 0 and (x[z]["title"] > unit["title"] or (x[z]["title"] == unit["title"] and x[z]["title"] > unit["title"] )): 
            x[z+1]=x[z]
            z = z - 1
            x[z+1]=unit
    return x
print(sort_books_title(dictionary_to_list(book_catagory_dictionary('google_books_dataset.csv'))))

#Function 2: Gianluca Fazio 101225417
def sort_books_publisher(J:dict) ->list :  
    """ the funtion returns the books sorted alphabetically based on publisher.
>>>return j 
>>>'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': 'N/A', 'publisher': 'AMACOM', 'pages': '112', 'language\n': 'English\n', 'category': 'Economics'
>>>'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': '4.8', 'publisher': 'Hachette UK', 'pages': '400', 'language\n': 'English\n', 'category': 'Fiction'
>>>'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'rating': 'N/A', 'publisher': 'Hachette UK', 'pages': '384', 'language\n': 'English\n', 'category': 'Fiction'
"""
    for r  in range(1, len(J)): 
            Jo=J[r]
            k=r-1
            while k >= 0 and (J[k]['publisher'] > Jo['publisher'] or (J[k]['publisher'] == Jo['publisher'] and J[k]['publisher']> Jo['publisher'])): 
                J[k+1]=J[k]
                k = k - 1
                J[k+1]=Jo                 
        
    return J
#print(sort_books_publisher(dictionary_to_list(book_catagory_dictionary('google_books_dataset.csv'))))

#Function 3 : Zach Goddard 101221539
import string
from typing import List

def sort_books_author(book_list: dict) -> list:
    """
    This function will return a dictionary of books that are sorted by the author alphabetically and those with the same author are then sorted by their title alphabetically.
    sort_books_author(google_books_dataset.csv)
    >>> 
    "title": "Antiques Roadkill: A Trash 'n' Treasures Mystery", "author": " Barbara Allan",  "language ": "English", "rating": 3.3, "publisher": " Kensington Publishing Corp.", " category": [" Fiction", "Comedy"] "pages": 288}
    """  
#sorting
    n = len(book_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if book_list[j]['author'] > book_list[j+1]['author']:
                book_list[j], book_list[j+1] = book_list[j+1], book_list[j]
    return book_list
#print(sort_books_author(dictionary_to_list(book_catagory_dictionary('google_books_dataset.csv'))))

#Function 4: Hakeem Khan 101233039
def sort_books_ascending_rate(dictlist:dict):
    """ 
    >>> sort_books_ascending_rate(book_catagory_dictionary("google_books_test.txt"))
    [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': '288', 'language\n': 'English\n', 'category': ['Fiction']}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': '544', 'language\n': 'English\n', 'category': ['Fiction']}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': '226', 'language\n': 'English', 'category': ['Fiction']}]
		"""
    n=len(dictlist)
    for i in range(n):
        for j in range(n-i-1):
            if dictlist[j]['rating']!='N/A':
                if dictlist[j+1]['rating']=='N/A':
                    dictlist[j],dictlist[j+1]=dictlist[j+1],dictlist[j]
                elif dictlist[j]['rating']>dictlist[j+1]['rating']:
                    dictlist[j],dictlist[j+1]=dictlist[j+1],dictlist[j]
                elif dictlist[j]['rating']==dictlist[j+1]['rating']:
                    if dictlist[j]['title']>dictlist[j+1]['title']:
                        dictlist[j],dictlist[j+1]=dictlist[j+1],dictlist[j]
                else:
                    None
    return dictlist
#print(sort_books_ascending_rate(dictionary_to_list(book_catagory_dictionary('google_books_dataset.csv'))))
