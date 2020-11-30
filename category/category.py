from create_csv import Createcsv


class Category:

    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.books = []
        print("La catégorie trouvée est :", self.name, "et l'url est :", self.url)

    def addBook(self, book):
        print("Le livre", book.title, "est ajouté à la catégorie", self.name, "et l'url est", self.url,
              "avec un prix de", book.price_including_tax, "et sans taxe de",
              book.price_excluding_tax, "ayant comme url", book.product_page_url, "et comme upc",
              book.upc, "avec une note de", book.review_rating, "pour un nombre encore disponible de",
              book.number_available, "parlant de", book.product_description,
              "et le lien d'image", book.image_url)
        self.books.append(book)

    def lanceCsv(self):
        liste = Createcsv(self.name)
        liste.TEST(self.books)