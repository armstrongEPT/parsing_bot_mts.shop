import telebot
from telebot import types
import csv
import bs4
import requests
from my_urls import *
from my_csv import *
from phones_func import *
from gadjets_func import *
from modens import*
from comp import *
from acessoires import *
from home import *


parser_phones()
parser_home()
parser_comp()
parser_acess()
parser_modems()
parser_gadjets()







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
    img = open('images/logo.png', 'rb')
    kb.add(kb_smartphones, kb_gadjets, kb_acces, kb_comp, kb_smart_home, kb_modems)
    bot.send_photo(message.chat.id, img)
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name} Выбери категорию товаров!', reply_markup=kb)

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
        img = open('images/phones.png', 'rb')
        kb_smartphones.add(kb_Xiaomi, kb_Apple, kb_Samsung, kb_Huawei, kb_POCO, kb_Realme, kb_TCL, kb_Honor)

        bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text=f'{call.from_user.first_name} Выберите тип из категории и получите файл!', reply_markup=kb_smartphones)

    elif call.data == 'x1':
        with open('xiaomi_phones.csv', 'r') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x2':
        with open('apple_phones.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x3':
        with open('samsung_phones.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x4':
        with open('huawei_phones.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x5':
        with open('poco.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x6':
        with open('realme.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x7':
        with open('tcl.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x8':
        with open('honor.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)

    elif call.data == 'Гаджеты':
        kb_gadj = types.InlineKeyboardMarkup()
        kb_sm_watch = types.InlineKeyboardButton(text='Умные часы', callback_data='x11')
        kb_headphones = types.InlineKeyboardButton(text='Наушники', callback_data='x21')
        kb_fitness = types.InlineKeyboardButton(text='Фитнес браслеты', callback_data='x31')
        kb_bluetooth = types.InlineKeyboardButton(text='Bluetooth колонки', callback_data='x41')
        kb_children_watch = types.InlineKeyboardButton(text='Детские умные часы', callback_data='x51')
        img = open('images/gadj.png', 'rb')
        kb_gadj.add(kb_sm_watch, kb_headphones, kb_fitness, kb_bluetooth, kb_children_watch)
        bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text=f'{call.from_user.first_name} Выберите тип из категории и получите файл!', reply_markup=kb_gadj)

    elif call.data == 'x11':
        kb_x11 = types.InlineKeyboardMarkup()
        kb_sm_watch_apple = types.InlineKeyboardButton(text='Apple', callback_data='x11x')
        kb_sm_watch_samsung = types.InlineKeyboardButton(text='Samsung', callback_data='x21x')
        kb_sm_watch_xiaomi = types.InlineKeyboardButton(text='Xiaomi', callback_data='x31x')
        kb_sm_watch_huawei = types.InlineKeyboardButton(text='Huawei', callback_data='x41x')
        kb_sm_watch_honor = types.InlineKeyboardButton(text='Honor', callback_data='x51x')
        kb_sm_watch_canyon = types.InlineKeyboardButton(text='Canyon', callback_data='x61x')
        kb_x11.add(kb_sm_watch_apple, kb_sm_watch_samsung, kb_sm_watch_xiaomi, kb_sm_watch_huawei, kb_sm_watch_honor, kb_sm_watch_canyon)
        bot.send_message(call.message.chat.id, text=f'{call.from_user.first_name} Выберите тип из категории и получите файл!', reply_markup=kb_x11)

    elif call.data == 'x11x':
        with open('smart_watches_apple.csv', 'r') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x21x':
        with open('smart_watches_samsung.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x31x':
        with open('smart_watches_xiaomi.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x41x':
        with open('smart_watches_huawei.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x51x':
        with open('smart_watches_honor.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x61x':
        with open('smart_watches_canyon.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)

    elif call.data == 'x21':
        kb_x21 = types.InlineKeyboardMarkup()
        kb_headphones_apple = types.InlineKeyboardButton(text='Apple', callback_data='x11a')
        kb_headphones_honor = types.InlineKeyboardButton(text='Samsung', callback_data='x21a')
        kb_headphones_samsung = types.InlineKeyboardButton(text='Xiaomi', callback_data='x31a')
        kb_headphones_jbl = types.InlineKeyboardButton(text='Huawei', callback_data='x41a')
        kb_headphones_huawei = types.InlineKeyboardButton(text='Honor', callback_data='x51a')
        kb_headphones_beats = types.InlineKeyboardButton(text='Canyon', callback_data='x61a')
        kb_headphones_canyon = types.InlineKeyboardButton(text='Canyon', callback_data='x71a')
        kb_x21.add(kb_headphones_apple, kb_headphones_honor, kb_headphones_samsung, kb_headphones_jbl, kb_headphones_huawei, kb_headphones_beats, kb_headphones_canyon)
        bot.send_message(call.message.chat.id,text=f'{call.from_user.first_name} Выберите тип из категории и получите файл!', reply_markup=kb_x21)

    elif call.data == 'x11a':
        with open('whireles_headphones_apple.csv', 'r') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x21a':
        with open('whireles_headphones_honor.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x31a':
        with open('whireles_headphones_samsung.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x41a':
        with open('whireles_headphones_jbl.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x51a':
        with open('whireles_headphones_huawei.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x61a':
        with open('whireles_headphones_beats.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x71a':
        with open('whireles_headphones_canyon.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)

    elif call.data == 'x31':
        kb_x31 = types.InlineKeyboardMarkup()
        kb_fitness_bracer_huawei= types.InlineKeyboardButton(text='Huawei', callback_data='x11q')
        kb_fitness_bracer_xiaomi = types.InlineKeyboardButton(text='Xiaomi', callback_data='x21q')
        kb_fitness_bracer_honor = types.InlineKeyboardButton(text='Honor', callback_data='x31q')
        kb_x31.add(kb_fitness_bracer_huawei, kb_fitness_bracer_xiaomi, kb_fitness_bracer_honor)
        bot.send_message(call.message.chat.id, text=f'{call.from_user.first_name} Выберите тип из категории и получите файл!', reply_markup=kb_x31)

    elif call.data == 'x11q':
        with open('fitness_bracer_huawei.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x21q':
        with open('fitness_bracer_xiaomi.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x31q':
        with open('fitness_bracer_honor.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)

    elif call.data == 'x41':
        kb_x41 = types.InlineKeyboardMarkup()
        kb_bluetooth_steaker_jbl = types.InlineKeyboardButton(text='Jbl', callback_data='x11w')
        kb_bluetooth_steaker_yandex = types.InlineKeyboardButton(text='Yandex', callback_data='x21w')
        kb_bluetooth_steaker_xiaomi = types.InlineKeyboardButton(text='Xiaomi', callback_data='x31w')
        kb_x41.add(kb_bluetooth_steaker_jbl, kb_bluetooth_steaker_yandex, kb_bluetooth_steaker_xiaomi)
        bot.send_message(call.message.chat.id, text=f'{call.from_user.first_name} Выберите тип из категории и получите файл!', reply_markup=kb_x41)

    elif call.data == 'x11w':
        with open('bluetooth_steaker_jbl.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x21w':
        with open('bluetooth_steaker_yandex.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x31w':
        with open('bluetooth_steaker_xiaomi.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)

    elif call.data == 'x51':
        kb_x51 = types.InlineKeyboardMarkup()
        kb_kids_smart_watches_elari = types.InlineKeyboardButton(text='Elari', callback_data='x11e')
        kb_kids_smart_watches_canyon = types.InlineKeyboardButton(text='Canyon', callback_data='x21e')
        kb_kids_smart_watches_huawei = types.InlineKeyboardButton(text='Huawei', callback_data='x31e')
        kb_x51.add(kb_kids_smart_watches_elari, kb_kids_smart_watches_canyon, kb_kids_smart_watches_huawei)
        bot.send_message(call.message.chat.id, text=f'{call.from_user.first_name} Выберите тип из категории и получите файл!', reply_markup=kb_x51)

    elif call.data == 'x11e':
        with open('kids_smart_watches_elari.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x21e':
        with open('kids_smart_watches_canyon.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x31e':
        with open('kids_smart_watches_huawei.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)

    elif call.data == 'Аксессуары':
        kb_acsess = types.InlineKeyboardMarkup()
        kb_zas = types.InlineKeyboardButton(text='Защита', callback_data='x211qw')
        kb_power = types.InlineKeyboardButton(text='Питание', callback_data='x221qw')
        kb_audio = types.InlineKeyboardButton(text='Аудио', callback_data='x231qw')
        kb_mem = types.InlineKeyboardButton(text='Память', callback_data='x241qw')
        kb_ant = types.InlineKeyboardButton(text='Антенны', callback_data='x251qw')
        img = open('images/ac.png', 'rb')
        kb_acsess.add(kb_zas, kb_power, kb_audio, kb_mem, kb_ant)
        bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text=f'{call.from_user.first_name} Выберите тип из категории и получите файл!', reply_markup=kb_acsess)

    elif call.data == 'x211qw':
        with open('property.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x221qw':
        with open('power.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x231qw':
        with open('audio.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x241qw':
        with open('memory.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x251qw':
        with open('antennas.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)

    elif call.data == 'Компьютеры':
        kb_comp = types.InlineKeyboardMarkup()
        kb_plan = types.InlineKeyboardButton(text='Планшеты', callback_data='x311')
        kb_nout = types.InlineKeyboardButton(text='Ноутбуки', callback_data='x321')
        kb_tv_pr = types.InlineKeyboardButton(text='ТВ приставки', callback_data='x331')
        kb_tv = types.InlineKeyboardButton(text='Телевизоры', callback_data='x341')
        img = open('images/comp.png', 'rb')
        kb_comp.add(kb_plan, kb_nout, kb_tv_pr, kb_tv)
        bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text=f'{call.from_user.first_name} Выберите тип из категории и получите файл!', reply_markup=kb_comp)

    elif call.data == 'x311':
        kb_x311 = types.InlineKeyboardMarkup()
        kb_tablet_samsung = types.InlineKeyboardButton(text='Samsung', callback_data='x311w')
        kb_tablet_huawei = types.InlineKeyboardButton(text='Huawei', callback_data='x321w')
        kb_tablet_lenovo = types.InlineKeyboardButton(text='Lenovo', callback_data='x331w')
        kb_tablet_xiaomi = types.InlineKeyboardButton(text='Xiaomi', callback_data='x341w')
        kb_tablet_prestigio = types.InlineKeyboardButton(text='Prestigio', callback_data='x351w')
        kb_tablet_tcl = types.InlineKeyboardButton(text='TCL', callback_data='x361w')
        kb_x311.add(kb_tablet_samsung, kb_tablet_huawei, kb_tablet_lenovo, kb_tablet_xiaomi, kb_tablet_prestigio, kb_tablet_tcl)
        bot.send_message(call.message.chat.id, text=f'{call.from_user.first_name} Выберите тип из категории и получите файл!', reply_markup=kb_x311)

    elif call.data == 'x311w':
        with open('tablet_samsung.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x321w':
        with open('tablet_huawei.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x331w':
        with open('tablet_lenovo.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x341w':
        with open('tablet_xiaomi.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x351w':
        with open('tablet_prestigio.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x361w':
        with open('tablet_tcl.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)

    elif call.data == 'x321':
        kb_x321 = types.InlineKeyboardMarkup()
        kb_laptops_apple = types.InlineKeyboardButton(text='Apple', callback_data='x311e')
        kb_laptops_honor = types.InlineKeyboardButton(text='Honor', callback_data='x321e')
        kb_laptops_huawei = types.InlineKeyboardButton(text='Huawei', callback_data='x331e')
        kb_laptops_prestigio = types.InlineKeyboardButton(text='Prestigio', callback_data='x341e')
        kb_x321.add(kb_laptops_apple, kb_laptops_honor, kb_laptops_huawei, kb_laptops_prestigio)
        bot.send_message(call.message.chat.id, text=f'{call.from_user.first_name} Выберите тип из категории и получите файл!', reply_markup=kb_x321)

    elif call.data == 'x311e':
        with open('laptops_apple.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x321e':
        with open('laptops_honor.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x331e':
        with open('laptops_huawei.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x341e':
        with open('laptops_prestigio.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)

    elif call.data == 'x331':
        kb_x331 = types.InlineKeyboardMarkup()
        kb_tv_box_apple = types.InlineKeyboardButton(text='Apple', callback_data='x311t')
        kb_tv_box_xiaomi = types.InlineKeyboardButton(text='Xiaomi', callback_data='x321t')
        kb_tv_box_yandex = types.InlineKeyboardButton(text='Yandex', callback_data='x331t')
        kb_x331.add(kb_tv_box_apple, kb_tv_box_xiaomi, kb_tv_box_yandex)
        bot.send_message(call.message.chat.id, text=f'{call.from_user.first_name} Выберите тип из категории и получите файл!', reply_markup=kb_x331)

    elif call.data == 'x311t':
        with open('tv_box_apple.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x321t':
        with open('tv_box_xiaomi.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)
    elif call.data == 'x331t':
        with open('tv_box_yandex.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)

    elif call.data == 'x341':
        with open('tv.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)

    elif call.data == 'Умный дом':
        kb_home = types.InlineKeyboardMarkup()
        kb_tech = types.InlineKeyboardButton(text='Умная техника', callback_data='x411')
        kb_dat = types.InlineKeyboardButton(text='Датчики и свет', callback_data='x421')
        kb_kol = types.InlineKeyboardButton(text='Колонки', callback_data='x431')
        img = open('images/home.png', 'rb')
        kb_home.add(kb_tech, kb_dat, kb_kol)
        bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text=f'{call.from_user.first_name} Выберите тип из категории и получите файл!', reply_markup=kb_home)

    elif call.data == 'x421':
        with open('dat.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)

    elif call.data == 'x431':
        with open('speaker.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)

    elif call.data == 'x411':
        kb_home1 = types.InlineKeyboardMarkup()
        kb_smart_tec_xiaomi = types.InlineKeyboardButton(text='Xiaomi', callback_data='x411w')
        kb_smart_tec_yandex = types.InlineKeyboardButton(text='Yandex', callback_data='x421w')
        kb_home1.add(kb_smart_tec_xiaomi, kb_smart_tec_yandex)
        bot.send_message(call.message.chat.id, text=f'{call.from_user.first_name} Выберите тип из категории и получите файл!', reply_markup=kb_home1)

    elif call.data == 'x411w':
        with open('smart_tec_xiaomi.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)

    elif call.data == 'x421w':
        with open('smart_tec_yandex.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)

    elif call.data == 'Модемы и роутеры':
        kb_mod = types.InlineKeyboardMarkup()
        kb_mr = types.InlineKeyboardButton(text='Модемы и роутеры', callback_data='x511')
        img = open('images/mod.png', 'rb')
        kb_mod.add(kb_mr)
        bot.send_photo(call.message.chat.id, img)
        bot.send_message(call.message.chat.id, text=f'{call.from_user.first_name} Выберите тип из категории и получите файл!', reply_markup=kb_mod)

    elif call.data == 'x511':
        with open('modem.csv') as file:
            bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
            bot.send_document(call.message.chat.id, file)



bot.polling(none_stop=True)
