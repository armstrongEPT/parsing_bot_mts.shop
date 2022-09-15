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


def get_home(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='products__unit')
    home = []

    for item in items:
        home.append(
            {
                'title': item.find('div', class_='products__unit__title').get_text(strip=True),
                'link_title': HOST + item.find('div', class_='products__unit__title').find('a').get('href'),
                'title_info': item.find('div', class_='products__unit__info').get_text(strip=True),
                'title_price': item.find('div', class_='products__unit__price').get_text(strip=True)
            }
        )
    return home


def save_home(items, path):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(['name', 'link', 'info', 'price'])
        for item in items:
            writer.writerow(
                [item['title'], item['link_title'], item['title_info'], item['title_price']])


def parser_home():
    html = get_html(URL_smart_tec_xiaomi)
    if html.status_code == 200:
        smtx = []
        for page in range(1):
            html = get_html(URL_smart_tec_xiaomi, params={'page': page})
            smtx.extend(get_home(html.text))
            save_home(smtx, CSV_smtx)
    html2 = get_html(URL_smart_tec_yandex)
    if html2.status_code == 200:
        smty = []
        for page in range(1):
            html = get_html(URL_smart_tec_yandex, params={'page': page})
            smty.extend(get_home(html.text))
            save_home(smty, CSV_smty)
    html3 = get_html(URL_dat)
    if html3.status_code == 200:
        dat = []
        for page in range(1):
            html = get_html(URL_dat, params={'page': page})
            dat.extend(get_home(html.text))
            save_home(dat, CSV_dat)
    html4 = get_html(URL_speaker)
    if html4.status_code == 200:
        spe = []
        for page in range(1):
            html = get_html(URL_speaker, params={'page': page})
            spe.extend(get_home(html.text))
            save_home(spe, CSV_spe)
    else:
        print('упс')