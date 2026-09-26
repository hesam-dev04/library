from mylibrary.library import Library
from time import sleep

def main():
    library = Library()

    while True:
        print('---===Library Management System===---')
        print('1 - add book')
        print('2 - remove book')
        print('3 - search book')
        print('4 - show books')
        print('5 - Exit')

        choice = input('Your choice: ')

        if choice == '1':
            title = input('Enter the Title of the book: ')
            author = input('Ennter the Author of the book: ')
            library.add_book(title,author)

        elif choice == '2':
            title = input('Enter the Title of the book you want to remove: ')
            library.remove_book(title)

        elif choice == '3':
            title = input('Search the Title of the book: ')
            library.search_book(title)

        elif choice == '4':
            library.show_books()

        elif choice == '5':
            print('Exiting the library...')
            sleep(2)
            break

        else:
            print('unexpected entry!')

if __name__ == '__main__':
    main()

        