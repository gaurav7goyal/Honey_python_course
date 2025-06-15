'''
Create a Libarary Class
Also Manage Book Class
'''
class Book():
    '''
    Create a Book class with  title , issued , author, borrowed
    '''
    def __init__(self, title,auther):
        self.title = title
        self.author = auther
        self.borrowed =  None
        self.is_issued =  False
        
    def get_book_details(self):
        book_details =  f"\nBook name:{self.title} Book Author:{ self.author} , borrowed:{self.borrowed}, is_issued {self.is_issued}\n"
        return book_details

store =  []
class Libarary():
    '''
    Libarary class handle book 
    '''

    def add_book(self, book):
        store.append(book)

    def borrowed_book(self, title, borrowed_name):
        '''
        Based on title and borrowed_name provide book to user
        '''
        book = [ i  for i in store if i.title == title ]
        print(book)
        book[0].borrowed = borrowed_name
        book[0].is_issued = True
        return f'Book Issued {book[0].get_book_details()}'
    
    def return_book(self, title, borrowed_name):
        pass

    def book_avaliable(self,title):
        pass
    
    def show_status(self, title):
        pass 

    def issued_book(self):
        '''
        return Book title and borrowed Name 
        '''
        pass
    def total_book(self):
        '''
        Return Total book count
        '''
        pass
    

lib = Libarary()
b1= Book('python','Robert')
lib.add_book(b1)
print(lib.borrowed_book('python','Gaurav'))