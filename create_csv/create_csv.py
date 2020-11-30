import csv


class Createcsv:

    def __init__(self, name):
        self.name = name
        print("création du csv :", self.name)

    def TEST(self, book):
        with open("données/" + self.name + "/" + self.name + ".csv", "w") as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
            for i in range(int(len(book))):
                writer.writerow(book[i])
