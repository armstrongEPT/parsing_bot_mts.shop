import telebot
from telebot import types
import csv
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


def get_phones(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='products__unit')
    phones = []

    for item in items:
        phones.append(
            {
                'title': item.find('div', class_='products__unit__title').get_text(strip=True),
                'link_title': HOST + item.find('div', class_='products__unit__title').find('a').get('href'),
                'title_info': item.find('div', class_='products__unit__info').get_text(strip=True),
                'title_price': item.find('div', class_='products__unit__price').get_text(strip=True)
            }
        )
    return phones



def save_phones(items, path):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(['name', 'link', 'info', 'price'])
        for item in items:
            writer.writerow(
                [item['title'], item['link_title'], item['title_info'], item['title_price']])



def parser_phones():
    html = get_html(URL_Xiaomi_phones)
    if html.status_code == 200:
        xi_phones = []
        for page in range(1):
            html = get_html(URL_Xiaomi_phones, params={'page': page})
            xi_phones.extend(get_phones(html.text))
            save_phones(xi_phones, CSV_xiaomi)
    html2 = get_html(URL_Apple_phones)
    if html2.status_code == 200:
        apple_phones = []
        for page in range(1):
            html2 = get_html(URL_Apple_phones, params={'page': page})
            apple_phones.extend(get_phones(html2.text))
            save_phones(apple_phones, CSV_apple)
    html3 = get_html(URL_Samsung_phones)
    if html3.status_code == 200:
        samsung_phones = []
        for page in range(1):
            html3 = get_html(URL_Apple_phones, params={'page': page})
            samsung_phones.extend(get_phones(html3.text))
            save_phones(samsung_phones, CSV_samsung)
    html4 = get_html(URL_Huawei_phones)
    if html4.status_code == 200:
        huawei_phones = []
        for page in range(1):
            html4 = get_html(URL_Huawei_phones, params={'page': page})
            huawei_phones.extend(get_phones(html4.text))
            save_phones(huawei_phones, CSV_huawei)
    html5 = get_html(URL_Honor_phones)
    if html5.status_code == 200:
        honor_phones = []
        for page in range(1):
            html5 = get_html(URL_Honor_phones, params={'page': page})
            honor_phones.extend(get_phones(html5.text))
            save_phones(honor_phones, CSV_honor)
    html6 = get_html(URL_Realme_phones)
    if html6.status_code == 200:
        realme_phones = []
        for page in range(1):
            html6 = get_html(URL_Realme_phones, params={'page': page})
            realme_phones.extend(get_phones(html6.text))
            save_phones(realme_phones, CSV_realme)
    html7 = get_html(URL_TCL_phones)
    if html7.status_code == 200:
        tcl_phones = []
        for page in range(1):
            html7 = get_html(URL_TCL_phones, params={'page': page})
            tcl_phones.extend(get_phones(html7.text))
            save_phones(tcl_phones, CSV_tcl)
    html8 = get_html(URL_POCO_phones)
    if html8.status_code == 200:
        poco_phones = []
        for page in range(1):
            html8 = get_html(URL_POCO_phones, params={'page': page})
            poco_phones.extend(get_phones(html8.text))
            save_phones(poco_phones, CSV_poco)
    else:
        print('упс')


