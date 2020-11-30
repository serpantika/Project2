import csv

class Createcsv:
    def __init__(self, name):
        self.name = name

    def Create_csv(self, categoryName):
        with open(categoryName + ".csv", "w", encoding="ISO-8859-1") as csvfile:
            fieldnames = ['product_page_url', 'universal_ product_code (upc)', 'title', "price_including_tax",
                          'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating',
                          'image_url']
            writer = csv.Dictwriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for i in range():
                writer.writerow()
