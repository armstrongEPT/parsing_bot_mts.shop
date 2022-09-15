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


def get_gadjets(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='products__unit')
    gadjets = []

    for item in items:
        gadjets.append(
            {
                'title': item.find('div', class_='products__unit__title').get_text(strip=True),
                'link_title': HOST + item.find('div', class_='products__unit__title').find('a').get('href'),
                'title_info': item.find('div', class_='products__unit__info').get_text(strip=True),
                'title_price': item.find('div', class_='products__unit__price').get_text(strip=True)

            }
        )
    return gadjets


def save_gadjets(items, path):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(['name', 'link', 'info', 'price'])
        for item in items:
            writer.writerow(
                [item['title'], item['link_title'], item['title_info'], item['title_price']])


def parser_gadjets():
    html11 = get_html(URL_smart_watches_apple)
    if html11.status_code == 200:
        swa = []
        for page in range(1, 10):
            html = get_html(URL_smart_watches_apple, params={'page': page})
            swa.extend(get_gadjets(html.text))
            save_gadjets(swa, CSV_swa)
    html12 = get_html(URL_smart_watches_samsung)
    if html12.status_code == 200:
        sws = []
        for page in range(1, 10):
            html = get_html(URL_smart_watches_samsung, params={'page': page})
            sws.extend(get_gadjets(html.text))
            save_gadjets(sws, CSV_sws)
    html13 = get_html(URL_smart_watches_honor)
    if html13.status_code == 200:
        swh = []
        for page in range(1, 10):
            html = get_html(URL_smart_watches_honor, params={'page': page})
            swh.extend(get_gadjets(html.text))
            save_gadjets(swh, CSV_swh)
    html14 = get_html(URL_smart_watches_huawei)
    if html14.status_code == 200:
        swhh = []
        for page in range(1, 10):
            html = get_html(URL_smart_watches_huawei, params={'page': page})
            swhh.extend(get_gadjets(html.text))
            save_gadjets(swhh, CSV_swhh)
    html15 = get_html(URL_smart_watches_canyon)
    if html15.status_code == 200:
        swc = []
        for page in range(1, 10):
            html = get_html(URL_smart_watches_canyon, params={'page': page})
            swc.extend(get_gadjets(html.text))
            save_gadjets(swc, CSV_swc)
    html16 = get_html(URL_smart_watches_xiaomi)
    if html16.status_code == 200:
        swx = []
        for page in range(1, 10):
            html = get_html(URL_smart_watches_xiaomi, params={'page': page})
            swx.extend(get_gadjets(html.text))
            save_gadjets(swx, CSV_swx)
    html17 = get_html(URL_whireles_headphones_apple)
    if html17.status_code == 200:
        wha = []
        for page in range(1, 10):
            html = get_html(URL_whireles_headphones_apple, params={'page': page})
            wha.extend(get_gadjets(html.text))
            save_gadjets(wha, CSV_wha)
    html18 = get_html(URL_whireles_headphones_honor)
    if html18.status_code == 200:
        whh = []
        for page in range(1, 10):
            html = get_html(URL_whireles_headphones_honor, params={'page': page})
            whh.extend(get_gadjets(html.text))
            save_gadjets(whh, CSV_whh)
    html19 = get_html(URL_whireles_headphones_samsung)
    if html19.status_code == 200:
        whs = []
        for page in range(1, 10):
            html = get_html(URL_whireles_headphones_samsung, params={'page': page})
            whs.extend(get_gadjets(html.text))
            save_gadjets(whs, CSV_whs)
    html20 = get_html(URL_whireles_headphones_jbl)
    if html20.status_code == 200:
        whj = []
        for page in range(1, 10):
            html = get_html(URL_whireles_headphones_jbl, params={'page': page})
            whj.extend(get_gadjets(html.text))
            save_gadjets(whj, CSV_whj)
    html21 = get_html(URL_whireles_headphones_huawei)
    if html21.status_code == 200:
        whhu = []
        for page in range(1, 10):
            html = get_html(URL_whireles_headphones_huawei, params={'page': page})
            whhu.extend(get_gadjets(html.text))
            save_gadjets(whhu, CSV_whhu)
    html22 = get_html(URL_whireles_headphones_beats)
    if html22.status_code == 200:
        whb = []
        for page in range(1, 10):
            html = get_html(URL_whireles_headphones_beats, params={'page': page})
            whb.extend(get_gadjets(html.text))
            save_gadjets(whb, CSV_whb)
    html23 = get_html(URL_whireles_headphones_xiaomi)
    if html23.status_code == 200:
        whb = []
        for page in range(1, 10):
            html = get_html(URL_whireles_headphones_xiaomi, params={'page': page})
            whb.extend(get_gadjets(html.text))
            save_gadjets(whb, CSV_whb)
    html24 = get_html(URL_whireles_headphones_canyon)
    if html24.status_code == 200:
        whc = []
        for page in range(1, 10):
            html = get_html(URL_whireles_headphones_canyon, params={'page': page})
            whc.extend(get_gadjets(html.text))
            save_gadjets(whc, CSV_whc)
    html25 = get_html(URL_fitness_bracers_huawei)
    if html25.status_code == 200:
        fbh = []
        for page in range(1, 10):
            html = get_html(URL_fitness_bracers_huawei, params={'page': page})
            fbh.extend(get_gadjets(html.text))
            save_gadjets(fbh, CSV_fbh)
    html26 = get_html(URL_fitness_bracers_xaiomi)
    if html26.status_code == 200:
        fbx = []
        for page in range(1, 10):
            html = get_html(URL_fitness_bracers_xaiomi, params={'page': page})
            fbx.extend(get_gadjets(html.text))
            save_gadjets(fbx, CSV_fbx)
    html27 = get_html(URL_fitness_bracers_honor)
    if html27.status_code == 200:
        fbhh = []
        for page in range(1, 10):
            html = get_html(URL_fitness_bracers_honor, params={'page': page})
            fbhh.extend(get_gadjets(html.text))
            save_gadjets(fbhh, CSV_fbhh)
    html28 = get_html(URL_bluetooth_steaker_jbl)
    if html28.status_code == 200:
        bsj = []
        for page in range(1, 10):
            html = get_html(URL_bluetooth_steaker_jbl, params={'page': page})
            bsj.extend(get_gadjets(html.text))
            save_gadjets(bsj, CSV_bsj)
    html29 = get_html(URL_bluetooth_steaker_yandex)
    if html29.status_code == 200:
        bsy = []
        for page in range(1, 10):
            html = get_html(URL_bluetooth_steaker_yandex, params={'page': page})
            bsy.extend(get_gadjets(html.text))
            save_gadjets(bsy, CSV_bsy)
    html30 = get_html(URL_bluetooth_steaker_xiaomi)
    if html30.status_code == 200:
        bsx = []
        for page in range(1, 10):
            html = get_html(URL_bluetooth_steaker_xiaomi, params={'page': page})
            bsx.extend(get_gadjets(html.text))
            save_gadjets(bsx, CSV_bsx)
    html31 = get_html(URL_kids_smart_watches_elari)
    if html31.status_code == 200:
        kswe = []
        for page in range(1, 10):
            html = get_html(URL_kids_smart_watches_elari, params={'page': page})
            kswe.extend(get_gadjets(html.text))
            save_gadjets(kswe, CSV_kswe)
    html32 = get_html(URL_kids_smart_watches_canyon)
    if html32.status_code == 200:
        kswc = []
        for page in range(1, 10):
            html = get_html(URL_kids_smart_watches_canyon, params={'page': page})
            kswc.extend(get_gadjets(html.text))
            save_gadjets(kswc, CSV_kswc)
    html33 = get_html(URL_kids_smart_watches_huawei)
    if html33.status_code == 200:
        kswh = []
        for page in range(1, 10):
            html = get_html(URL_kids_smart_watches_huawei, params={'page': page})
            kswh.extend(get_gadjets(html.text))
            save_gadjets(kswh, CSV_kswh)
    else:
        print('упс')
