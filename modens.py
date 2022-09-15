import bs4
import requests
from my_urls import *
from my_csv import *

HOST = 'https://shop.mts.by/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}


def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_modems(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='products__unit')
    modems = []

    for item in items:
        modems.append(
            {
                'title': item.find('div', class_='products__unit__title').get_text(strip=True),
                'link_title': HOST + item.find('div', class_='products__unit__title').find('a').get('href'),
                'title_info': item.find('div', class_='products__unit__info').get_text(strip=True),
                'title_price': item.find('div', class_='products__unit__price').get_text(strip=True),
            }
        )
    return modems


def save_modems(items, path):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(['name', 'link', 'info', 'price', 's'])
        for item in items:
            writer.writerow(
                [item['title'], item['link_title'], item['title_info'], item['title_price']])


def parser_modems():
    html = get_html(URL_mod)
    if html.status_code == 200:
        modems = []
        for html in range(1):
            html = get_html(URL_mod)
            modems.extend(get_modems(html.text))
            save_modems(modems, CSV_modem)
    else:
        print('упс')