# import csv
# import bs4
# import requests
#
# CSV_xiaomi = 'xiaomi_phones.csv'
# HOST = 'https://shop.mts.by/'
# URL_Xiaomi_phones = 'https://shop.mts.by/phones/Xiaomi/'
# URL_Huawei_phones = 'https://shop.mts.by/phones/Huawei/'
# URL_Apple_phones = 'https://shop.mts.by/phones/Apple/'
# URL_Samsung_phones = 'https://shop.mts.by/phones/Samsung/'
# URL_Realme_phones = 'https://shop.mts.by/phones/realme/'
# URL_Honor_phones = 'https://shop.mts.by/phones/realme/'
# URL_POCO_phones = 'https://shop.mts.by/phones/poco/'
# URL_TCL_phones = 'https://shop.mts.by/phones/tcl/'
# HEADERS = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
#     }
#
# def get_html(url, params=''):
#     r = requests.get(url, headers=HEADERS, params=params)
#     return r
#
# def get_content(html):
#     soup = bs4.BeautifulSoup(html, 'html.parser')
#     items = soup.find_all('div', class_='products-list__body')
#     xiaomi_phones = []
#
#     for item in items:
#         xiaomi_phones.append(
#             {
#             'title': item.find('div', class_='products__unit__title').get_text(strip=True),
#             'phone_image': HOST + item.find('div', class_='products__unit__image').find('img').get('src'),
#             'link_title': HOST + item.find('div', class_='products__unit__title').find('a').get('href'),
#             'title_info': item.find('div', class_='products__unit__info').get_text(strip=True),
#             'title_price': item.find('div', class_='products__unit__price').get_text(strip=True),
#             'title_id': item.find('div', class_='products__unit').get('id')
#             }
#         )
#     return xiaomi_phones
#
#
#
# def save_xi_phones(items, path):
#     with open(path, 'w', newline='') as file:
#         writer = csv.writer(file, delimiter=';')
#         writer.writerow(['название', 'изо', 'ссылка', 'инфа', 'цена', 'id'])
#         for item in items:
#             writer.writerow([item['title'], item['phone_image'], item['link_title'], item['title_info'], item['title_price'], item['title_id']])
#
#
# def parser():
#     html = get_html(URL_Xiaomi_phones)
#     if html.status_code == 200:
#         xi_phones = []
#         for page in range(1, 9):
#             html = get_html(URL_Xiaomi_phones, params={'page': page})
#             xi_phones.extend(get_content(html.text))
#             save_xi_phones(xi_phones, CSV_xiaomi)
#     else:
#         print('упс')
#
#
# parser()







            # xiaomi_id = URL_Xiaomi_phones.split('/')[-2]
            # apple_id = URL_Apple_phones.split('/')[-2]
            # tcl_id = URL_TCL_phones.split('/')[-2]
            # xiaomi_phones[xiaomi_id] = {
            #     'title': title,
            #     'phone_image': phone_image,
            #     'link_title': link_title,
            #     'title_info': title_info,
            #     'title_price': title_price,
            #     'titile_id': title_id
            # }
    #         apple_phones[apple_id] = {
    #             'title': title,
    #             'phone_image': phone_image,
    #             'link_title': link_title,
    #             'title_info': title_info,
    #             'title_price': title_price,
    #             'titile_id': title_id
    #         }
    #         tcl_phones[tcl_id] = {
    #             'title': title,
    #             'phone_image': phone_image,
    #             'link_title': link_title,
    #             'title_info': title_info,
    #             'title_price': title_price,
    #             'titile_id': title_id
    #         }
    #
    # with open('xiaomi_phones.json', 'w', encoding='utf-8') as file:
    #     json.dump(xiaomi_phones, file, indent=4, ensure_ascii=False)
    # with open('apple_phones.json', 'w', encoding='utf-8') as file:
    #     json.dump(apple_phones, file, indent=4, ensure_ascii=False)
    # with open('tcl_phones.json', 'w', encoding='utf-8') as file:
    #     json.dump(tcl_phones, file, indent=4, ensure_ascii=False)



# html = get_html(URL_Xiaomi_phones)
# get_content(html.text)
# html = get_html(URL_Apple_phones)
# get_content(html.text)
# html = get_html(URL_TCL_phones)
# get_content(html.text)





























# import json
# import bs4
# import requests
#
#
# HOST = 'https://shop.mts.by/'
# URL_Xiaomi_phones = 'https://shop.mts.by/phones/Xiaomi/'
# URL_Huawei_phones = 'https://shop.mts.by/phones/Huawei/'
# URL_Apple_phones = 'https://shop.mts.by/phones/Apple/'
# URL_Samsung_phones = 'https://shop.mts.by/phones/Samsung/'
# URL_Realme_phones = 'https://shop.mts.by/phones/realme/'
# URL_Honor_phones = 'https://shop.mts.by/phones/realme/'
# URL_POCO_phones = 'https://shop.mts.by/phones/poco/'
# URL_TCL_phones = 'https://shop.mts.by/phones/tcl/'
# HEADERS = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
#     }
#
# def get_html(url, params=''):
#     r = requests.get(url, headers=HEADERS, params=params)
#     return r
#
# def get_content(html):
#     soup = bs4.BeautifulSoup(html, 'html.parser')
#     items = soup.find_all('div', class_='products-list__body')
#     xiaomi_phones = {}
#     apple_phones = {}
#     tcl_phones = {}
#     for item in items:
#             title = item.find('div', class_='products__unit__title').get_text(strip=True),
#             phone_image = HOST + item.find('div', class_='products__unit__image').find('img').get('src'),
#             link_title = HOST + item.find('div', class_='products__unit__title').find('a').get('href'),
#             title_info = item.find('div', class_='products__unit__info').get_text(strip=True),
#             title_price = item.find('div', class_='products__unit__price').get_text(strip=True),
#             title_id = item.find('div', class_='products__unit').get('id')
#             xiaomi_id = URL_Xiaomi_phones.split('/')[-2]
#             apple_id = URL_Apple_phones.split('/')[-2]
#             tcl_id = URL_TCL_phones.split('/')[-2]
#             xiaomi_phones[xiaomi_id] = {
#                 'title': title,
#                 'phone_image': phone_image,
#                 'link_title': link_title,
#                 'title_info': title_info,
#                 'title_price': title_price,
#                 'titile_id': title_id
#             }
#             apple_phones[apple_id] = {
#                 'title': title,
#                 'phone_image': phone_image,
#                 'link_title': link_title,
#                 'title_info': title_info,
#                 'title_price': title_price,
#                 'titile_id': title_id
#             }
#             tcl_phones[tcl_id] = {
#                 'title': title,
#                 'phone_image': phone_image,
#                 'link_title': link_title,
#                 'title_info': title_info,
#                 'title_price': title_price,
#                 'titile_id': title_id
#             }
#
#     with open('xiaomi_phones.json', 'w', encoding='utf-8') as file:
#         json.dump(xiaomi_phones, file, indent=4, ensure_ascii=False)
#     with open('apple_phones.json', 'w', encoding='utf-8') as file:
#         json.dump(apple_phones, file, indent=4, ensure_ascii=False)
#     with open('tcl_phones.json', 'w', encoding='utf-8') as file:
#         json.dump(tcl_phones, file, indent=4, ensure_ascii=False)
#
#
#
# html = get_html(URL_Xiaomi_phones)
# get_content(html.text)
# html = get_html(URL_Apple_phones)
# get_content(html.text)
# html = get_html(URL_TCL_phones)
# get_content(html.text)