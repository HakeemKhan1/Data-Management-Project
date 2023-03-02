#Hakeem Khan ID:101233039
import string
from typing import List
#Function 6
def get_books_by_author(author:str,dictionary:dict)->int:
    """>>>get_books_by_author("Agatha Christie",dictionary)
    The author Agatha Christie has published the following books:
    Book  1 : The Mysterious Affair at Styles rating: 4.4
    Book  2 : And Then There Were None rating: 4.6
    Book  3 : The Red Signal: An Agatha Christie Short Story rating: 5
    3"""
    author_list = []
    for key in dictionary: #iterates through the catagories
        for val in dictionary[key]: #iterates through the values inside the list assigned to the catagories of the dictionaries
            if author == val['author']:
                author_list.append((val['title'],val['rating']))
                author_list=list(set(author_list))
    print("The author",author,"has published the following books:")
    for i in range(len(author_list)):
        print("Book ",str(i+1),":",author_list[i][0], "rating:",author_list[i][1])
    return print('the author has published:',len(author_list),'Books' ) 
#Function 7
def get_books_by_publisher(publisher:str,dictionary:dict)->int:
    """get_books_by_publisher('Kensington Publishing Corp.',dictionary)
    The publisher Kensington Publishing Corp. has published the following books:
    Book  1 Antiques Knock-Off by Barbara Allan
    Book  2 Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan
    2"""    
    publisher_list=[]
    for key in dictionary:
        for value in dictionary[key]: 
            if publisher == value['publisher']:
                publisher_list.append((value['title'],value['author']))
                publisher_list=list(set(publisher_list))
    print("The publisher", publisher, "has published the following books:")
    for i in range(len(publisher_list)):
        print("Book ",str(i+1), publisher_list[i][0],"by", publisher_list[i][1])
    return print('the author has published:',len(publisher_list),'Books' ) 
