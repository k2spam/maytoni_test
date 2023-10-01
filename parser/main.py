import datetime
import requests
import re
import random
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def collect_data():
    url = 'https://maytoni.ru/catalog/decorative/?SHOWALL=1#product_23'
    ua = UserAgent()
    headers = {
        'User-Agent': ua.random
    }
    response = requests.get(url, headers=headers)
    with open('pages/lights.html', 'w') as file:
        file.write(response.text)

def parse_data():
    regex = r"\s([a-zA-Z0-9\s]+[а-яА-Я0-9-]+)"
    file = open('pages/lights.html', 'r').read()
    soup = BeautifulSoup(file, 'lxml')
    cards = soup.find_all('div', class_='catalog-card')
    min_dt = 1672520400000
    max_dt = 1696107600000
    step_dt = 24*60*60*1000
    json = ""

    if(len(cards)):
        for key, card in enumerate(cards):
            title = card.find('div', class_='catalog-card__title')
            articleWrap = card.find('div', class_='catalog-card__article')
            article = articleWrap.find('span') if articleWrap is not None else None
            imageWrap = card.find('picture', class_='catalog-card__img-img')
            image = imageWrap.find('img') if imageWrap is not None else None
            price = card.find('span', class_='price')
            status = card.find('div', class_='label--new')
            datetime = random.randrange(min_dt, max_dt, step_dt)

            title = title.text.strip() if title is not None else "Светильник"
            subtitle = "".join(re.findall(regex, title))
            article = article.text.strip() if article is not None else "MOD174CL-09G"
            title = "".join(re.sub(regex, "", title))
            image = f'https://maytoni.ru{image["src"]}' if image is not None else "https://maytoni.ru/upload/resize_cache/iblock/6d0/690_690_0/4r39a9q9v0p4zarjy4ofw88wiod8a6s4.jpeg"
            price = price.text.strip() if price is not None else "12 345 ₽"
            status = "new" if status is not None else "not new"

            json += f'{{ "id":"{key}", "title": "{title}", "subtitle": "{subtitle}", "article":"{article}", "image": "{image}", "price": "{price}", "status": "{status}", "datetime": "{datetime}" }},'
        json = json[:-1]
        json = f'[{json}]'
        with open('json/lights.json', 'w') as file:
            file.write(json)

def main():
    # collect_data()
    parse_data()

if __name__ == '__main__':
    main()