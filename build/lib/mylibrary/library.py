# this is a library

class Library():
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(
            {
                "title": title,
                "author": author,
            }
        )
        print(f'Book {title} succsesfully added')

    def remove_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                print(f"Book {book['title']} succesfully removed")
            else:
                print(f'book {book['title']} was not found!')

    def search_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                print(f"title: {book['title']} | author: {book['author']}")
            else:
                print(f"there's no book with {title} title!")

    def show_books(self):
        if not self.books:
            print("there's no book in shelf")

        for book in self.books:
            print(f"title: {book['title']} | author: {book['author']}")

        
                


l = Library()

l.add_book('1984','goerge orwell')

print(l.books)

l.remove_book('1984')

print(l.books)

print(__name__)