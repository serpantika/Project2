import requests
from bs4 import BeautifulSoup
import urllib.request
from book import Book
from category import Category
import os

class Scrapper:

    def __init__(self):
        self.categories = []
        print("Le scrapper est lancé !")

    def getCategories(self):
        url = "http://books.toscrape.com/"
        response = requests.get(url)

        if response.ok:
            soup = BeautifulSoup(response.text, features="html.parser")
            books_category = soup.find("ul", {"class": "nav nav-list"}).find_all("li")[1:]

            for li in books_category:
                categoryName = li.find("a")["href"].split('/')[3]
                categoryUrl = 'http://books.toscrape.com/' + li.find('a')['href']
                category = Category(categoryName, categoryUrl)
                if not os.path.exists("données/" + str(categoryName)):
                    os.makedirs("données/" + str(categoryName))
                if not os.path.exists("données/" + str(categoryName + "/image")):
                    os.makedirs("données/" + str(categoryName + '/image'))
                self.categories.append(Category(categoryName, categoryUrl))
                self.getBooksFromCategories(categoryName, categoryUrl, category)
                category.lanceCsv()

    def getBooksFromCategories(self, categoryName, categoryUrl, category):
        self.booksurl = []
        i = 2
        categoryUrlDeux = categoryUrl
        categoryUrlDeux = categoryUrlDeux.replace('index.html', 'page-') + str(i) + ".html"
        url = categoryUrlDeux
        reponse = requests.get(url)
        while reponse.ok:
            self.findH3(reponse, categoryName, category)
            i += 1
            print(categoryUrl)
            categoryUrlDeux = categoryUrl
            categoryUrlDeux = categoryUrlDeux.replace('index.html', 'page-') + str(i) + ".html"
            url = categoryUrlDeux
            reponse = requests.get(url)
        else:
            url = categoryUrl
            print(categoryUrl)
            reponse = requests.get(url)
            if reponse.ok:
                self.findH3(reponse, categoryName, category)

    def getDataFromBook(self, product_page_url, categoryName, category):
        print(product_page_url)
        url = str(product_page_url)
        reponse = requests.get(url)
        if reponse.ok:
            soup = BeautifulSoup(reponse.text, 'html.parser')

            title = soup.find('title').text.strip()
            title = title.replace(' | Books to Scrape - Sandbox', '')

            img = soup.find('img')
            image_url = 'http://books.toscrape.com/' + str(img['src'])
            image_url = image_url.replace('../../', '')

            image = img['alt']
            image = image.replace(":", " ")
            image = image.replace("/", " ")
            image = image.replace('"', " ")
            image = image.replace('...', " ")
            image = image.replace('*', " ")
            image = image.replace('?', " ")
            print(image)
            urllib.request.urlretrieve(str(image_url), 'données/' + str(categoryName) + '/image/' + str(image) + ".jpg")

            product_description = soup.find_all('p')[3].text.strip()

            upc = soup.find_all('td')[0].text.strip()

            price_including_tax = soup.find_all('td')[2].text.strip()
            price_including_tax = price_including_tax.replace('Â', '')

            price_excluding_tax = soup.find_all('td')[3].text.strip()
            price_excluding_tax = price_excluding_tax.replace('Â', '')

            number_available = soup.find_all('td')[5].text.strip()
            number_available = number_available.replace('In stock (', '')
            number_available = number_available.replace(' available)', '')

            review = soup.find_all('p')[2]
            if "One" in str(review):
                review_rating = "One star"
            elif "Two" in str(review):
                review_rating = "Two star"
            elif "Three" in str(review):
                review_rating = "Three star"
            elif "Four" in str(review):
                review_rating = "Four star"
            else:
                review_rating = "Five star"
            book = Book(title, price_including_tax, price_excluding_tax,
                                  product_page_url, upc, number_available, product_description,
                                  review_rating, image_url, image)
            category.addBook(book)

    def findH3(self, reponse, categoryName, category):
        soup = BeautifulSoup(reponse.text, 'html.parser')
        h3s = soup.findAll('h3')
        for h3 in h3s:
            a = h3.find('a')
            product_page_url = a['href']
            product_page_url = product_page_url.replace("../../..", "")
            product_page_url = 'http://books.toscrape.com/catalogue' + product_page_url
            self.getDataFromBook(product_page_url, categoryName, category)
