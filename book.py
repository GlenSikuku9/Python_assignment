class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    
    def read(self):
        return f"Reading '{self.title}' by {self.author}."
    
#Subclass with inheritance
class EBook(Book):
    def __init__(self,title,author,pages,file_size):
        super().__init__(title,author,pages)
        self.file_size=file_size

    def read(self):
        return f"Reading the ebook '{self.title}' on a device."
    
#Encapsulation example
class Library:
    def __init__(self):
        self.__books=[] #Private
    
    def add_book(self,book):
        self.__books.append(book)

    def show_books(self):
        return [book.title for book in self.__books]
    
#Test
physical_book=Book("1984","George Orwell", 328)
ebook=EBook("The Martian", "Andy Weir", 384, "2MB")

library=Library()
library.add_book(physical_book)
library.add_book(ebook)

print(physical_book.read())
print(ebook.read())       
print(library.show_books())