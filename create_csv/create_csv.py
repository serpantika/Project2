import csv
from book import Book

class Createcsv:

    def __init__(self, name):
        self.name = name
        print("création du csv :", self.name)

    def TEST(self, book):
        print(len(book))
        with open("données/" + self.name + "/" + self.name + ".csv", "w", encoding = "UTF-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow("title; price_including_tax; price_excluding_tax;product_page_url; upc;"
                            " number_available; product_description; review_rating; image_url; image")
            for i in range(int(len(book))):
                writer.writerow(book[i].booktocsv())
