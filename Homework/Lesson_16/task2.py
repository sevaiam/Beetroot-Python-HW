# Task 2
# Library
# Write a class structure that implements a library. Classes:
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []
# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the
# books list for the current library.
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year
# All 3 classes must have a readable __repr__ and __str__ methods.
# Also, the book class should have a class variable which holds the amount of all existing books


class Library:

    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def __repr__(self):
        return f'{self.name} contains these books: {self.books}'

    # def __str__(self):
    #     return self.name

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        self.authors.append(author)
        return book

    def add_book(self, new_book):
        self.books.append(new_book)

    def group_by_author(self, author):
        return author.authors

    def group_by_year(self, year):
        year_list = []
        for book in self.books:
            if year in book.year:
                year_list.append(book)
        return year_list


class Book:
    books_total = 0

    def __init__(self, name, year, author):
        self.book_name = name
        self.book_year = year
        self.book_author = author
        self.books_total += 1

    def __repr__(self):
        return f'<"{self.book_name}" by {self.book_author.author_name}, {self.book_year}>'

    def __str__(self):
        return self.book_name


class Author:

    def __init__(self, name, country, birthday):
        self.author_name = name
        self.author_country = country
        self.author_birthday = birthday
        self.books = []

    def __repr__(self):
        return f'{self.author_name} from {self.author_country}, born in {self.author_birthday}'

    def __str__(self):
        return self.author_name


lib1 = Library('National Odessa Library')
lib2 = Library('Kiev Library')
auth1 = Author('Taras Schevchenko', 1814, 'Ukraine')
auth2 = Author('Hryhorii Skovoroda', 1722, 'Ukraine')
book1 = Book('Kobzar', 1840, auth1)
book2 = Book('The Garden of Divine Songs', 1785, auth2)

lib1.add_book(book1)
lib1.add_book(book2)

print(lib1)