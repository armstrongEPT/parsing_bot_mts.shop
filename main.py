import telebot
from telebot import types
import csv
import bs4
import requests

# CSV_xiaomi = 'xiaomi_phones.csv'
# CSV_apple = 'apple_phones.csv'
# CSV_huawei = 'huawei_phones.csv'
# CSV_samsung = 'samsung_phones.csv'
# CSV_honor = 'honor.csv'
# CSV_realme = 'realme.csv'
# CSV_poco = 'poco.csv'
# CSV_tcl = 'tcl.csv'
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
# }
#
#
# def get_html(url, params=''):
#     r = requests.get(url, headers=HEADERS, params=params)
#     return r
#
#
# def get_phones(html):
#     soup = bs4.BeautifulSoup(html, 'html.parser')
#     items = soup.find_all('div', class_='products-list__body')
#     phones = []
#
#     for item in items:
#         phones.append(
#             {
#                 'title': item.find('div', class_='products__unit__title').get_text(strip=True),
#                 'phone_image': HOST + item.find('div', class_='products__unit__image').find('img').get('src'),
#                 'link_title': HOST + item.find('div', class_='products__unit__title').find('a').get('href'),
#                 'title_info': item.find('div', class_='products__unit__info').get_text(strip=True),
#                 'title_price': item.find('div', class_='products__unit__price').get_text(strip=True),
#                 'title_id': item.find('div', class_='products__unit').get('id')
#             }
#         )
#     return phones
#
#
# def save_phones(items, path):
#     with open(path, 'w', newline='') as file:
#         writer = csv.writer(file, delimiter=';')
#         writer.writerow(['название', 'изо', 'ссылка', 'инфа', 'цена', 'id'])
#         for item in items:
#             writer.writerow(
#                 [item['title'], item['phone_image'], item['link_title'], item['title_info'], item['title_price'],
#                  item['title_id']])
#
#
# def parser():
#     html = get_html(URL_Xiaomi_phones)
#     html2 = get_html(URL_Apple_phones)
#     html3 = get_html(URL_Samsung_phones)
#     html4 = get_html(URL_Huawei_phones)
#     html5 = get_html(URL_Honor_phones)
#     html6 = get_html(URL_Realme_phones)
#     html7 = get_html(URL_TCL_phones)
#     html8 = get_html(URL_POCO_phones)
#     if html.status_code == 200:
#         xi_phones = []
#         apple_phones = []
#         samsung_phones = []
#         huawei_phones = []
#         honor_phones = []
#         realme_phones = []
#         tcl_phones = []
#         poco_phones = []
#         for page in range(1, 25):
#             xi_phones.extend(get_phones(html.text))
#             apple_phones.extend(get_phones(html2.text))
#             samsung_phones.extend(get_phones(html3.text))
#             huawei_phones.extend(get_phones(html4.text))
#             honor_phones.extend(get_phones(html5.text))
#             realme_phones.extend(get_phones(html6.text))
#             tcl_phones.extend(get_phones(html7.text))
#             poco_phones.extend(get_phones(html8.text))
#             save_phones(xi_phones, CSV_xiaomi)
#             save_phones(apple_phones, CSV_apple)
#             save_phones(samsung_phones, CSV_samsung)
#             save_phones(huawei_phones, CSV_huawei)
#             save_phones(honor_phones, CSV_honor)
#             save_phones(realme_phones, CSV_realme)
#             save_phones(tcl_phones, CSV_tcl)
#             save_phones(poco_phones, CSV_poco)
#     else:
#         print('упс')
#
#
# parser()

bot = telebot.TeleBot('5546001741:AAGClEu550ZujOTGuOzUwWQmX6RsWhALNUo')


@bot.message_handler(commands=['start'])
def start(message):
    kb = types.InlineKeyboardMarkup()
    kb_smartphones = types.InlineKeyboardButton(text='Сматрфоны', callback_data='Смартфоны')
    kb_gadjets = types.InlineKeyboardButton(text='Гаджеты', callback_data='Гаджеты')
    kb_acces = types.InlineKeyboardButton(text='Аксессуары', callback_data='Аксессуары')
    kb_comp = types.InlineKeyboardButton(text='Компьютеры', callback_data='Компьютеры')
    kb_smart_home = types.InlineKeyboardButton(text='Умный дом', callback_data='Умный дом')
    kb_modems = types.InlineKeyboardButton(text='Модемы и роутеры', callback_data='Модемы и роутеры')
    img = open('11.png', 'rb')
    kb.add(kb_smartphones, kb_gadjets, kb_acces, kb_comp, kb_smart_home, kb_modems)
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name} Выбери категорию товаров!', reply_markup=kb)
    bot.send_photo(message.chat.id, img)



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'Смартфоны':
        kb_smartphones = types.InlineKeyboardMarkup()
        kb_Xiaomi = types.InlineKeyboardButton(text='Xiaomi', callback_data='x1')
        kb_Apple = types.InlineKeyboardButton(text='Apple', callback_data='x2')
        kb_Samsung = types.InlineKeyboardButton(text='Samsung', callback_data='x3')
        kb_Huawei = types.InlineKeyboardButton(text='Huawei', callback_data='x4')
        kb_POCO = types.InlineKeyboardButton(text='POCO', callback_data='x5')
        kb_Realme = types.InlineKeyboardButton(text='Realme', callback_data='x6')
        kb_TCL = types.InlineKeyboardButton(text='TCL', callback_data='x7')
        kb_Honor = types.InlineKeyboardButton(text='HONOR', callback_data='x8')
        kb_smartphones.add(kb_Xiaomi, kb_Apple, kb_Samsung, kb_Huawei, kb_POCO, kb_Realme, kb_TCL, kb_Honor)
        bot.send_message(call.message.chat.id, text=f'{call.from_user.first_name} Выберите марку смартфона!',
                         reply_markup=kb_smartphones)

    elif call.data == 'Гаджеты':
        kb_gadj = types.InlineKeyboardMarkup()
        kb_sm_watch = types.InlineKeyboardButton(text='Xiaomi', callback_data='x11')
        kb_headphones = types.InlineKeyboardButton(text='Apple', callback_data='x21')
        kb_fitness = types.InlineKeyboardButton(text='Samsung', callback_data='x31')
        kb_bluetooth = types.InlineKeyboardButton(text='Huawei', callback_data='x41')
        kb_children_watch = types.InlineKeyboardButton(text='POCO', callback_data='x51')
        kb_gadj.add(kb_sm_watch, kb_headphones, kb_fitness, kb_bluetooth, kb_children_watch)
        bot.send_message(call.message.chat.id, text=f'{call.from_user.first_name} Выберите тип гаджета!',
                         reply_markup=kb_gadj)

    elif call.data == 'x1':
        with open('xiaomi_phones.csv') as file:
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x2':
        with open('apple_phones.csv') as file:
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x3':
        with open('samsung_phones.csv') as file:
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x4':
        with open('huawei_phones.csv') as file:
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x5':
        with open('poco.csv') as file:
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x6':
        with open('realme.csv') as file:
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x7':
        with open('tcl.csv') as file:
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x8':
        with open('honor.csv') as file:
            bot.send_document(call.message.chat.id, file)


bot.polling(none_stop=True)
