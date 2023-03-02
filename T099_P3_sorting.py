#Art Galaites 101188224 
import string
from typing import List
from T099_P1_load_data import book_catagory_dictionary

#Function def
def sort_books_title(dictionary: dict)-> list:
    """
    Returns all books sorted by title in alphabetical order
    >>>[{"title" : "The Essentials of Finance and Accounting for Nonfinancial Managers","author" : "Edward Fields", "language": "English", "rating" : "N/A","publisher": "AMACOM", "category" : "Business", "pages": 320},{"title" : "Watching (The Making of Riley Paige Book 1)","author": "Blake Pierce","rating" : 4.6,"language": "English","publisher": "Blake Pierce","category" : "Detective","pages": 250},{"title" : "Sunshine","author" : "Zimmy Smith","language": "English","rating" : 5.0,"publisher": " Publish Co.","category" : "Fiction","pages": 288},{"title": "We","author": "Yevgeny Zamyatin","language": "English","rating": 4.3,"publisher": "Pan","category": "Fiction","pages": 226}],[{"title" : "Young Justice Vol. 1","author" : "Art Baltazar","language": "English","rating" : 4.1,"publisher": "DC","category" : "Superhero","pages": 164}], [{"title" : "And Then There Were None","author" : "Agatha Christie","language": "English","rating" : 4.6,"publisher": "HarperCollins UK","category" : "Detective","pages": 115}]
    
    [{"title" : "And Then There Were None","author" : "Agatha Christie","language": "English","rating" : 4.6,"publisher": "HarperCollins UK","category" : "Detective","pages": 115}],{"title" : "Sunshine","author" : "Zimmy Smith","language": "English","rating" : 5.0,"publisher": " Publish Co.","category" : "Fiction","pages": 288},[{"title" : "The Essentials of Finance and Accounting for Nonfinancial Managers","author" : "Edward Fields", "language": "English", "rating" : "N/A","publisher": "AMACOM", "category" : "Business", "pages": 320},{"title" : "Watching (The Making of Riley Paige Book 1)","author": "Blake Pierce","rating" : 4.6,"language": "English","publisher": "Blake Pierce","category" : "Detective","pages": 250},{"title": "We","author": "Yevgeny Zamyatin","language": "English","rating": 4.3,"publisher": "Pan","category": "Fiction","pages": 226}],[{"title" : "Young Justice Vol. 1","author" : "Art Baltazar","language": "English","rating" : 4.1,"publisher": "DC","category" : "Superhero","pages": 164}]
    
    """
    books_by_title = list(dictionary.items())
    different_books = []
    
    try:
        for (category, books) in books_by_title:
            for book in books:
                book_title = book["title"]
                
                book_is_found = False
                for live_books in different_books:
                    if book_title == live_books["title"]:
                        book_is_found = True
                        break
                    
                if book_is_found == False:
                    book_data = {"title": book["title"],"author": book["author"],"language ": book["language"],"rating": book["rating"],"publisher": book["publisher"],"categories": [category],"pages": book["pages"]}
                    different_books.append(book_data)
                else:
                    live_books["categories"].append(category)
        
        x = different_books
        for y in range(1, len(x)): 
            unit=x[y]
            z=y-1
            while z >= 0 and (x[z]["title"] > unit["title"] or (x[z]["title"] == unit["title"] and x[z]["title"] > unit["title"] )): 
                x[z+1]=x[z]
                z = z - 1
                x[z+1]=unit
        return x     
    except: 
        return 'Dictionary was not found'
   




