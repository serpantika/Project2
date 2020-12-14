import csv


class Createcsv:

    def __init__(self, name):
        self.name = name
        print("création du csv :", self.name)

    def TEST(self, book):
        with open("données/" + self.name + "/" + self.name + ".csv", "w", encoding="UTF-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=" ", quotechar=" ", quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["title; image; upc; price_including_tax; price_excluding_tax;"
                            " number_available; review_rating; product_page_url; image_url; product_description"])
            for i in range(int(len(book))):
                writer.writerow([book[i].booktocsv()])
