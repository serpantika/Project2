from categorie import get_books
import requests
from bs4 import BeautifulSoup
import csv
import urllib.request

# from données import data
books = get_books()
a = 0

# for category in books:
c = 0
romans = []
roman = dict
for link in books['travel']:
    c += 1
    a += 1
    print(c)
    url = str(link)
    reponse = requests.get(url)
    print(reponse.encoding)
    if reponse.ok:
        soup = BeautifulSoup(reponse.text, 'html.parser')

        title = soup.find('title').text.strip()
        title = title.replace(' | Books to Scrape - Sandbox', '')

        img = soup.find('img')
        image = 'http://books.toscrape.com/' + str(img['src'])
        image = image.replace('../../', '')
        urllib.request.urlretrieve(str(image), str(a) + ".jpg")

        description = soup.find_all('p')[3].text.strip()

        upc = soup.find_all('td')[0].text.strip()

        price = soup.find_all('td')[2].text.strip()
        price = price.replace('Â', '')

        pricenot = soup.find_all('td')[3].text.strip()
        pricenot = pricenot.replace('Â', '')

        disponible = soup.find_all('td')[5].text.strip()
        disponible = disponible.replace('In stock (', '')
        disponible = disponible.replace(' available)', '')

        review = soup.find_all('p')[2]
        if "One" in str(review):
            rate = "One star"
        elif "Two" in str(review):
            rate = "Two star"
        elif "Three" in str(review):
            rate = "Three star"
        elif "Four" in str(review):
            rate = "Four star"
        else:
            rate = "Five star"

        roman = {"title": title, "price_including_tax": price, "price_excluding_tax": pricenot,
                 "universal_ product_code (upc)": upc, "number_available": disponible,
                 "product_description": description, "review_rating": rate, "image_url": image,
                 "product_page_url": link, 'category': 'travel'}
        romans.append(roman)

        # romans = data(link, 'travel', c, romans)
with open('travel' + ".csv", "w", encoding = "ISO-8859-1" ) as csvfile:
    fieldnames = ['product_page_url', 'universal_ product_code (upc)', 'title', "price_including_tax",
                  'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating',
                  'image_url']
    writer = csv.Dictwriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(c):
        writer.writerow(romans[i])
print(romans[2])
