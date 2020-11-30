import requests
from bs4 import BeautifulSoup



c += 1
url = str(link)
reponse = requests.get(url)
if reponse.ok:
    soup = BeautifulSoup(reponse.text, 'html.parser')

    title = soup.find('title').text.strip()
    title = title.replace(' | Books to Scrape - Sandbox', '')

    img = soup.find('img')
    image = 'http://books.toscrape.com/' + str(img['src'])
    image = image.replace('../../', '')

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
             "product_page_url": link, 'category': category}
    romans.append(roman)
