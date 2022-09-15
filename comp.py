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


def get_comp(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='products__unit')
    comp = []

    for item in items:
        comp.append(
            {
                'title': item.find('div', class_='products__unit__title').get_text(strip=True),
                'link_title': HOST + item.find('div', class_='products__unit__title').find('a').get('href'),
                'title_info': item.find('div', class_='products__unit__info').get_text(strip=True),
                'title_price': item.find('div', class_='products__unit__price').get_text(strip=True)
            }
        )
    return comp


def save_comp(items, path):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(['name', 'link', 'info', 'price'])
        for item in items:
            writer.writerow(
                [item['title'], item['link_title'], item['title_info'], item['title_price']])


def parser_comp():
    html = get_html(URL_tablet_samsung)
    if html.status_code == 200:
        ts = []
        for page in range(1):
            html = get_html(URL_tablet_samsung, params={'page': page})
            ts.extend(get_comp(html.text))
            save_comp(ts, CSV_ts)
    html2 = get_html(URL_tablet_huawei)
    if html2.status_code == 200:
        th = []
        for page in range(1):
            html = get_html(URL_tablet_huawei, params={'page': page})
            th.extend(get_comp(html.text))
            save_comp(th, CSV_th)
    html3 = get_html(URL_tablet_lenovo)
    if html3.status_code == 200:
        tl = []
        for page in range(1):
            html = get_html(URL_tablet_lenovo, params={'page': page})
            tl.extend(get_comp(html.text))
            save_comp(tl, CSV_tl)
    html4 = get_html(URL_tablet_xiaomi)
    if html4.status_code == 200:
        tx = []
        for page in range(1):
            html = get_html(URL_tablet_xiaomi, params={'page': page})
            tx.extend(get_comp(html.text))
            save_comp(tx, CSV_tx)
    html5 = get_html(URL_tablet_prestigio)
    if html5.status_code == 200:
        tp = []
        for page in range(1):
            html = get_html(URL_tablet_prestigio, params={'page': page})
            tp.extend(get_comp(html.text))
            save_comp(tp, CSV_tp)
    html6 = get_html(URL_tablet_tcl)
    if html6.status_code == 200:
        tc = []
        for page in range(1):
            html = get_html(URL_tablet_tcl, params={'page': page})
            tc.extend(get_comp(html.text))
            save_comp(tc, CSV_tc)
    html7 = get_html(URL_laptops_apple)
    if html7.status_code == 200:
        la = []
        for page in range(1):
            html = get_html(URL_laptops_apple, params={'page': page})
            la.extend(get_comp(html.text))
            save_comp(la, CSV_la)
    html8 = get_html(URL_laptops_honor)
    if html8.status_code == 200:
        lh = []
        for page in range(1):
            html = get_html(URL_laptops_honor, params={'page': page})
            lh.extend(get_comp(html.text))
            save_comp(lh, CSV_lh)
    html9 = get_html(URL_laptops_huawei)
    if html9.status_code == 200:
        lhh = []
        for page in range(1):
            html = get_html(URL_laptops_huawei, params={'page': page})
            lhh.extend(get_comp(html.text))
            save_comp(lhh, CSV_lhh)
    html10 = get_html(URL_laptops_prestigio)
    if html10.status_code == 200:
        lp = []
        for page in range(1):
            html = get_html(URL_laptops_prestigio, params={'page': page})
            lp.extend(get_comp(html.text))
            save_comp(lp, CSV_lp)
    html11 = get_html(URL_tv_box_apple)
    if html11.status_code == 200:
        ta = []
        for page in range(1):
            html = get_html(URL_tv_box_apple, params={'page': page})
            ta.extend(get_comp(html.text))
            save_comp(ta, CSV_ta)
    html12 = get_html(URL_tv_box_xiaomi)
    if html12.status_code == 200:
        tx = []
        for page in range(1):
            html = get_html(URL_tv_box_xiaomi, params={'page': page})
            tx.extend(get_comp(html.text))
            save_comp(tx, CSV_tx)
    html13 = get_html(URL_tv_box_yandex)
    if html13.status_code == 200:
        ty = []
        for page in range(1):
            html = get_html(URL_tv_box_yandex, params={'page': page})
            ty.extend(get_comp(html.text))
            save_comp(ty, CSV_ty)
    html14 = get_html(URL_tv)
    if html14.status_code == 200:
        tv = []
        for page in range(1):
            html = get_html(URL_tv, params={'page': page})
            tv.extend(get_comp(html.text))
            save_comp(tv, CSV_tv)
    else:
        print('упс')
