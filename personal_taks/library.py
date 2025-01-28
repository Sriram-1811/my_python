class Library:
    def __init__(self):
        self.books=[]

    def add_book(self,title):
        self.books.append(title)
        print(title,"book was successfully added into library")

    def remove_books(self,title):
        if title in self.books:
            self.books.remove(title)
            print(title,"book removed successfully from library")
        else:
            print("book named",title,"was not found in the library")
    
    def list_books(self):
        if len(self.books)!=0:
            for book in self.books:
                print(book)
        else:
            print("library is empty")

l1=Library()

l1.add_book("Rich Dad, Poor Dad")
l1.add_book("Psycology Money")
l1.add_book("atomic habits")
l1.add_book("1991")

l1.list_books()

l1.remove_books("1983")
l1.remove_books("1991")

