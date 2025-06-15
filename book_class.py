'''
We need to create Book classs
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
    


# b1= Book('python','Robert','Gaurav')
# b2= Book('python1','Robert','Gaurav')
# b3= Book('python2','Robert','Gaurav')
# b4= Book('python3','Robert','Gaurav')
# print(b1.get_book_details())
# print(b2.get_book_details())
# print(b3.get_book_details())
# print(b4.get_book_details())   
for i in range(5):
    book_name =  input('Enter book Name:')
    book_author =  input('Enter Book Author: ')
    book_borrowed =  input('Enter book Borrowed:')
    b1= Book(book_name,book_author,book_borrowed)
    print(b1.get_book_details())