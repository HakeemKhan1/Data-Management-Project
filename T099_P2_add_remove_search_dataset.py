#T107 - P2 Task 3: Milestone 1's Final Team code
#Created by: (Arnie Nambiar, 101183154),(Matt Turner, 101169414),(Pietro Adamvoski, 101238885),(Richard Ofordile, 101190357)

#imports
from T107_P1_load_data import book_dictionary_category_list

#The eight functions - P2 – Task 1

#Function 1 - Arnie Nambiar, 101183154
def add_book(dictionary: dict, book: tuple) -> dict:
    """
    Adds a new book to the dictionary and prints a message stating, “The book has been added correctly” or “There was an error adding the book”.
   
   
    >>> add_book(book_dictionary_category_list("Google_Books_Dataset.csv"), ("The Art of Basketball", "Arnie Nambiar", 5.0, "HarperCollins", 500, "Fiction", "English"))
    The book has been added correctly
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': '3.3', 'publisher': 'Kensington Publishing Corp.', 'pages': '288', 'language\n': 'English'},... {'title': 'The Art of Basketball', 'author': 'Arnie Nambiar', 'rating': '5.0', 'publisher': 'HarperCollins', 'pages': '500', 'language\n': 'English'},...
   
    """

    category_1 = book[5]
    keys_1 = dictionary.keys()
    books = dictionary.get(category_1)

    for key in keys_1:
        if category_1 == key:
            new_book = {'title': book[0], 'author': book[1], 'rating': book[2], 'publisher': book[3], 'pages': book[4], 'language': book[6]}
   
    if new_book in books:
        print('There is an error adding the book')
   
    else:
        books.append(new_book)
        print('The book has been added correctly.')
       
    return dictionary

#Function 2 - Arnie Nambiar, 101183154
def remove_book(title_1: str, category_1: str, dictionary: dict) -> dict:
    """ 
    Returns the the updated dictionary after removing a book and prints a message saying "The book has been removed correctly" or "There was an error removing the book. Book not found". 
    
    >>> result2 = remove_book("Antiques Roadkill: A Trash 'n' Treasures Mystery", "Fiction", book_dictionary_category_list("google_books_dataset.csv")
    for book in result2["Fiction"]:
       print(book)
    
    The book has been removed correctly.
    {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': '4.5', 'publisher': 'HarperCollins UK', 'pages': '544', 'language\n': 'English'}
    {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': '4.8', 'publisher': 'Tor Books', 'pages': '226', 'language\n': 'English'}
    {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': '4.8', 'publisher': 'Hachette UK', 'pages': '400', 'language\n': 'English'}
    ...
    
    """

    books = dictionary.get(category_1)

    for book in books:
        if title_1 == book.get("title"):
            dictionary[category_1].remove(book)
            print("The book has been removed correctly.")
            return dictionary
        
    else:
        print("There is an error removing the book. Book is not found.")
        
    return dictionary


#Function 3 - Matt Turner, 101169414
def get_books_by_category(category: str, dictionary:dict) ->list:
   
    """
    This function will return all the books in a specific category with their
    corresponding books number
   
    books_by_category = book_dictionary_category_list('google_books_dataset.csv')
    get_books_by_category("Business", books_by_category)
    >>>Category: Business, has the following books:
    Book 1 - Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth by T. Harv Eker
    Book 2 - How to Understand Business Finance: Edition 2 by Bob Cinnamon
    Book 3 - Principles: Life and Work by Ray Dalio
    Book 4 - Platform Revolution: How Networked Markets Are Transforming the Economy and How to Make Them Work for You by Geoffrey G. Parker
    Book 5 - The Infinite Game by Simon Sinek
    Book 6 - Platform Revolution: How Networked Markets Are Transforming the Economy and How to Make Them Work for You by Geoffrey G. Parker
    Book 7 - Eat That Frog!: 21 Great Ways to Stop Procrastinating and Get More Done in Less Time. Edition 3 by Brian Tracy
    Book 8 - Platform Revolution: How Networked Markets Are Transforming the Economy and How to Make Them Work for You by Geoffrey G. Parker
    Book 9 - Business Strategy (The Brian Tracy Success Library) by Brian Tracy
    Book 10 - Selling 101: What Every Successful Sales Professional Needs to Know by Zig Ziglar
    Book 11 - The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further by Alvin Hall
    Book 12 - The Magic of Thinking Big by David J. Schwartz
    Book 13 - Predictably Irrational: The Hidden Forces that Shape Our Decisions by Dan Ariely
    Book 14 - Think Like a Freak: The Authors of Freakonomics Offer to Retrain Your Brain by Steven D. Levitt
    Book 15 - Personal Success (The Brian Tracy Success Library) by Brian Tracy
    Book 16 - Summary: Think and Grow Rich by Nine99 Innovation Lab
    Book 17 - Start Day Trading Now: A Quick and Easy Introduction to Making Money While Managing Your Risk by Michael Sincere
    Book 18 - Rework by Jason Fried
    Book 19 - Platform: Get Noticed in a Noisy World by Michael Hyatt
    Book 20 - The Essentials of Finance and Accounting for Nonfinancial Managers by Edward Fields

    """
    counter=0
    book_titles = []
    book_authors = []
   
   
    if category in dictionary:
        books = dictionary[category]
        for i in range(len(books)):
            counter+=1
            book = books[i]
            book_titles.append(book["title"])
            book_authors.append(book["author"])
        print("Category: " +  category + ", has the following books: ")
        for i in range(len(book_titles)):
            print("Book " f"{i+1} - {book_titles[i]}", "by " + book_authors[i])
   
                 
   
    return "There are" + " " + str(counter) + " " + "books under this category"

#Function 4 - Matt Turner, 101169414
def get_books_by_rate(dictionary:dict, rating: str) ->list:
   
    """
    This function returns all the books that are associated with a rating and
    gives the number of books that have that same rating.
   
    get_books_by_rate(books_by_category, "4.4" )
    >>>Book  14 : 'Salem's Lot by Stephen King
    Book  25 : The Mysterious Affair at Styles by Agatha Christie
    Book  34 : The Weight of Honor (Kings and Sorcerers Book 3) by Morgan Rice
    Book  43 : Immortal Hulk Vol. 1: Or Is He Both? by Al Ewing
    Book  45 : The Joker by Brian Azzarello
    Book  94 : The Mysterious Affair at Styles by Agatha Christie
    Book  99 : Once Missed (A Riley Paige Mystery Book 16) by Blake Pierce
    Book  115 : The Weight of Honor (Kings and Sorcerers Book 3) by Morgan Rice
    Book  130 : The Mysterious Affair at Styles by Agatha Christie
    Book  134 : Once Missed (A Riley Paige Mystery Book 16) by Blake Pierce
    Book  143 : 'Salem's Lot by Stephen King
    Book  155 : Once Missed (A Riley Paige Mystery Book 16) by Blake Pierce
    Book  165 : The Mysterious Affair at Styles by Agatha Christie
    Book  175 : Spider-Verse: Volume 1 by Dan Slott
    Book  177 : Immortal Hulk Vol. 1: Or Is He Both? by Al Ewing
    Book  193 : The Mysterious Affair at Styles by Agatha Christie
    There are 16 books whose rate is 4.4 . This is the list of books
    """
   
    count=0
    counter=0
    book_by_rate = []
    dictionary_book_list = dictionary.values()
    for i in dictionary_book_list:
        for j in i:
            count+=1
            if j.get('rating')  ==  rating:
                book_by_rate.append(j)
                counter+= 1
                print("Book ", count, ":", j.get('title'), "by", j.get('author'))
    print("There are", counter, "books whose rate is", rating,". This is the list of books")
    print(book_by_rate)
    return counter
    

#Function 5 - Coded by: Pietro Adamvoski, 101238885
def get_books_by_title(dic:dict, title:str)->str:
    """Returns True if title exists in dictionary. If title does not exists 
    in dictionary, returns False.

    >>>get_books_by_title('After Anna')
    True
    The book has been found

    >>>get_books_by_title('Ater Anna')
    False
    The book has NOT been found
    """

    counter=0
    dictionary_book_list = dic.values()
    for row in dictionary_book_list:
        for column in row:
            if column.get("title") == title:
                counter=1
                return "{i} and The book has been found".format(i=bool(column.get("title") == title))
    if counter==0:
        print("{i} and The book has NOT been found".format(i=bool(column.get("title") == title)))


#Function 6 - Richard Ofordile, 101190357
def get_books_by_author(author: str, dictionary: dict)->list:
    """
    Returns a list of all the books in the given data set written by the given
    author

    get_books_by_author("Stephen King",dictionary)
    >>>["'Salem's Lot"]

    get_books_by_author("Agatha Christie",dictionary)
    >>>["The Red Signal: An Agatha Christie Short Story", "The Mysterious Affair at Styles",
    "And Then There Were None"]

    get_books_by_author("Richard Ofordile", dictionary)
    >>>[]
    """
    print('The Author "'+ author +'" has published the following books:')
    dictionary_book_list=dictionary.values()
    lst=[]
    for i in  dictionary_book_list:
        for j in i:
            if j.get('author') == author:
                lst.append(j)
    counter1=0
    for k in lst:
        for a in lst:
            if counter1==0:
                None
                counter1+=1
            if a==k and counter1>0:
                lst.remove(k)
               
    
    counter=len(lst)+1
                
    print(lst)
    return "There are" + " " + str(counter) + " " + "books under this author"

#Function 7 - Richard Ofordile, 101190357 
def get_books_by_publisher(publisher:str, dictionary:dict)->list:
    """
    Returns a list of the books published by the specified publisher in the
    given data set

    get_books_by_publisher("Penguin", dictionary)
    >>>["The Infinite Game","Boy Erased: A Memoir", "Getting Things Done: The Art of Stress-Free Productivity"
    ,"No One Is Too Small to Make a Difference","The Magic of Thinking Big"]

    get_books_by_publisher("Vintage", dictionary)
    >>>["We Should All Be Feminists"]

    get_books_by_publisher("Richard Ofordile", dictionary)
    >>>[]
    """
    new_lst = []
    dictionary_book_list=dictionary.values()    
    for i in  dictionary_book_list:
        for j in i:
            if j.get('publisher') == publisher:
                new_lst.append(j)
    
    counter=len(new_lst)
    print(new_lst)
    return "This publisher has released" + " " + str(counter) + " " + "books"

#Function 8 - Coded by: Pietro Adamvoski, 101238885
def get_all_categories_for_book(dic:dict, title:str)->str:
    """Returns the number of categories associated with given book title. Also, 
    returns all the categories associated with given book title. 
    
    >>>get_all_categories_for_book_title('After Anna')
    Number of categories for given title: 4
    Category 1: "Fiction"
    Category 2: "Adventure"
    Category 3: "Thrillers"
    Category 4: "Mystery"
    
    >>>get_all_categories_for_book_title('Ultimate Spider-Man Vol. 11: Carnage')
    Number of categories for given title: 1
    Category 1: "Comics"
    """    
    category_list = []
    counter=0
    for category in dic.keys():
        for book in dic.get(category):
            if book.get("title") == title:
                counter+=1
                if category not in category_list:
                    category_list.append(category)
     
   
    print("Number of categories for given title: ", counter)
    counter=0
    print("The book title",'"', title,'"', "belongs to the following categories:") 
    for i in category_list:
        counter+=1
        print("Category",counter,":",i)
    return "This book belongs in" + " " + str(counter) + " " + "categories"
