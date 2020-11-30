import csv


class Createcsv:

    def __init__(self, name):
        self.name = name
        print("création du csv :", self.name)

    def TEST(self, book):
        with open(self.name + ".csv", "w", encoding="ISO-8859-1") as csvfile:
            writer = csv.writer(csvfile)
            for i in range(int(len(book))):
                writer.writerow(book[i])
