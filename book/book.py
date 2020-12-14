class Book:

    def __init__(self, title, price_including_tax, price_excluding_tax,
                 product_page_url, upc, number_available, product_description,
                 review_rating, image_url, image):
        self.title = title
        self.price_including_tax = price_including_tax
        self.price_excluding_tax = price_excluding_tax
        self.product_page_url = product_page_url
        self.upc = upc
        self.number_available = number_available
        self.product_description = product_description
        self.review_rating = review_rating
        self.image_url = image_url
        self.image = image

    def booktocsv(self):
        return (self.title + ";" + self.price_including_tax + ";" + self.price_excluding_tax + ";" +
                self.product_page_url + ";" + self.upc + ";" + self.number_available + ";" +
                self.review_rating + ";" + self.image_url + ";" + self.image + ";" + self.product_description)
