import requests
from bs4 import BeautifulSoup


BASE_URL = 'http://books.toscrape.com/'


def findh3(category, reponse, books):
    soup = BeautifulSoup(reponse.text, 'html.parser')
    h3s = soup.findAll('h3')
    for h3 in h3s:
        a = h3.find('a')
        link = a['href']
        link = link.replace("../../..", "")
        link = 'http://books.toscrape.com/catalogue' + link
        if category in books:
            books[category].append(link)
        else:
            books[category] = [link]


def get_books():
    categorys = dict()
    books = dict()
    url = BASE_URL
    reponse = requests.get(url)
    if reponse.ok:
        soup = BeautifulSoup(reponse.text, 'html.parser')
        books_category = soup.find("ul",{"class": "nav nav-list"}).find_all('li')[1:]
        i = 2
        for li in books_category:
            urlcategory = 'http://books.toscrape.com/' + li.find('a')['href']
            category = urlcategory.replace("http://books.toscrape.com/catalogue/category/books/", "")
            category = category.replace('_' + str(i)+'/index.html', '')
            i += 1
            categorys[category] = urlcategory

    for category in categorys:
        i = 2
        urlcategorydeux = categorys[category]
        urlcategorydeux = urlcategorydeux.replace('index.html', 'page-') + str(i) + ".html"
        url = urlcategorydeux
        reponse = requests.get(url)
        while reponse.ok:
            findh3(category, reponse, books)
            i += 1
            urlcategorydeux = categorys[category]
            urlcategorydeux = urlcategorydeux.replace('index.html', 'page-') + str(i) + ".html"
            url = urlcategorydeux
            reponse = requests.get(url)
        else:
            url = categorys[category]
            reponse = requests.get(url)
            if reponse.ok:
                findh3(category, reponse, books)
    return books
