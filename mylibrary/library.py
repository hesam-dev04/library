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
            

    def search_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                print(f"title: {book['title']} | author: {book['author']}")
            

    def show_books(self):
        if not self.books:
            print("there's no book in shelf")

        for book in self.books:
            print(f"title: {book['title']} | author: {book['author']}")

        