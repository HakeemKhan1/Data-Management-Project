#Hakeem Khan ID:101233039
import string
from typing import List
from T099_P2_fun import get_books_by_publisher
from T099_P1_load_data import book_catagory_dictionary
from T099_P2_add_remove_search_dataset import get_books_by_category
from T099_P2_add_remove_search_dataset import get_all_categories_for_book

def options()->str:
    ''' The funciton displays a string of the available commands for the user
    interface.
    >>>options()
    The available options are:
    1- L)oad data
    2- A)dd book
    3- R)emove book
    4- G)et books
             T)itle	R)ate  A)uthor	P)ublisher  C)ategory
    5 -GCT)Get all Categories for book Title
    6-S)ort books
            T)itle	R)ate  A)uthor	P)ublisher  C)ategory
    7-Q)uit
    '''
    print('The available options are:\n1- L)oad data\n2- A)dd book\n3- R)emove book\n4- G)et books\n\t T)itle\tR)ate  A)uthor\tP)ublisher  C)ategory\n5 -GCT)Get all Categories for book Title\n6-S)ort books\n\tT)itle\tR)ate  A)uthor\tP)ublisher  C)ategory\n7-Q)uit')
def ui()->None:
    ''' This function creates a text-based user interface, calling the data analysis functions that my team
    developed for Milestone 1 and Milestone 2.
    >>> def ui()
    The available options are:
    1- L)oad data
    2- A)dd book
    3- R)emove book
    4- G)et books
             T)itle	R)ate  A)uthor	P)ublisher  C)ategory
    5 -GCT)Get all Categories for book Title
    6-S)ort books
            T)itle	R)ate  A)uthor	P)ublisher  C)ategory
    7-Q)uit
    Please type your command (Q to quit) : y
    No such command
    Please type your command (Q to quit) : g
    File not loaded
    Please type your command (Q to quit) : yeasdklfaskjdf
    No such command
    Please type your command (Q to quit) : l
    Enter a dataset google_books_dataset.csv
    Please type your commandd (Q to quit) : g
    How would you like to get books? p
    Enter a publisher Kensington Publishing Corp.
    The publisher Kensington Publishing Corp. has published the following books:
    Book  1 Antiques Knock-Off by Barbara Allan
    Book  2 Antiques Roadkill: A Trash 'n' Treasures Mystery by Barbara Allan
    2
    The available options are: 
    1- L)oad data
    2- A)dd book
    3- R)emove book
    4- G)et books
             T)itle	R)ate  A)uthor	P)ublisher  C)ategory
    5 -GCT)Get all Categories for book Title
    6-S)ort books
            T)itle	R)ate  A)uthor	P)ublisher  C)ategory
    7-Q)uit
    Please type your commandd (Q to quit) : Q 
    >>>
    
    '''
    command_list = ['A', 'a', 'R', 'r', 'G', 'g', 'T', 't', 'P', 'p', 'C', 'c', 'S', 's','GCT','gct']
    get_list = ['T', 't', 'P', 'p', 'C', 'c','A', 'a', 'R', 'r',]
    primary_command = ['G', 'g','A', 'a', 'R', 'r','S', 's','GCT','gct']
    load_quit = ['Q','L','l']
    command = ''
    load_data = ''
    sub_command = ''  
    sort = ''
    category = ''
    title = ''
    options()
    while command!='Q' and command!='q' and sub_command!='Q' and sub_command!='q':
        command = input('Please type your command (Q to quit) : ''')
        if command == 'Q' or command == 'q':
            print('Goodbye! -> Press run to restart or load a new dictionary')
            break
        elif command in command_list:
            print('File not loaded')
        elif command not in command_list and command not in load_quit:
            print('No such command')
        elif command == 'L' or command == 'l':
            load_data = input('Enter a dataset'' ')
            while True:
                sub_command = input('Please type your commandd (Q to quit) : ''')
                if sub_command == 'Q' or sub_command == 'q':
                    print('Goodbye! -> Press run to restart or load a new dictionary ')
                    break 
                elif sub_command == 'G' or sub_command == 'g':
                    sort = input('How would you like to get books?'' ')
                    while sort not in get_list:
                        print('invalid way to get books')
                        sort = input('How would you like to get books?'' ')
                        if sort in get_list:
                            break
                    if sort == 'P' or sort == 'p':
                        publisher = input('Enter a publisher'' ')
                        print(get_books_by_publisher(publisher,book_catagory_dictionary(load_data)))
                        options()
                    elif sort == 'C' or sort == 'c':
                        category = input('Enter a category'' ')
                        print(get_books_by_category(category, book_catagory_dictionary(load_data)))
                        options()
                elif sub_command == 'GCT' or sub_command == 'gct':
                    title = input('Enter a title'' ')
                    print(get_all_categories_for_book_title(title,book_catagory_dictionary(load_data)))
                    options()                  
                elif sub_command == 'l' or sub_command == 'L':
                    print('dataset already entered')                
                elif sub_command not in primary_command:
                    print('No such command') 
        
ui()
              
            
            
          
        
            
        
