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


def get_acess(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='products__unit')
    acess = []

    for item in items:
        acess.append(
            {
                'title': item.find('div', class_='products__unit__title').get_text(strip=True),
                'link_title': HOST + item.find('div', class_='products__unit__title').find('a').get('href'),
                'title_info': item.find('div', class_='products__unit__info').get_text(strip=True),
                'title_price': item.find('div', class_='products__unit__price').get_text(strip=True)
            }
        )
    return acess


def save_acess(items, path):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(['name', 'link', 'info', 'price'])
        for item in items:
            writer.writerow(
                [item['title'], item['link_title'], item['title_info'], item['title_price']])


def parser_acess():
    html = get_html(URL_protection)
    if html.status_code == 200:
        prot = []
        for page in range(1):
            html = get_html(URL_protection, params={'page': page})
            prot.extend(get_acess(html.text))
            save_acess(prot, CSV_prot)
    html2 = get_html(URL_power)
    if html2.status_code == 200:
        power = []
        for page in range(1):
            html = get_html(URL_power, params={'page': page})
            power.extend(get_acess(html.text))
            save_acess(power, CSV_power)
    html3 = get_html(URL_audio)
    if html3.status_code == 200:
        audio = []
        for page in range(1):
            html = get_html(URL_audio, params={'page': page})
            audio.extend(get_acess(html.text))
            save_acess(audio, CSV_audio)
    html4 = get_html(URL_memory)
    if html4.status_code == 200:
        mem = []
        for page in range(1):
            html = get_html(URL_memory, params={'page': page})
            mem.extend(get_acess(html.text))
            save_acess(mem, CSV_memory)
    html5 = get_html(URL_ant)
    if html5.status_code == 200:
        ant = []
        for page in range(1):
            html = get_html(URL_ant, params={'page': page})
            ant.extend(get_acess(html.text))
            save_acess(ant, CSV_ant)
    else:
        print('упс')