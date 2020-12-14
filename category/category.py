from create_csv import Createcsv


class Category:

    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def lanceCsv(self):
        liste = Createcsv(self.name)
        liste.TEST(self.books)
