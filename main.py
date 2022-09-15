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






# bot = telebot.TeleBot('5546001741:AAGClEu550ZujOTGuOzUwWQmX6RsWhALNUo')
#
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     kb = types.InlineKeyboardMarkup()
#     kb_smartphones = types.InlineKeyboardButton(text='Сматрфоны', callback_data='Смартфоны')
#     kb_gadjets = types.InlineKeyboardButton(text='Гаджеты', callback_data='Гаджеты')
#     kb_acces = types.InlineKeyboardButton(text='Аксессуары', callback_data='Аксессуары')
#     kb_comp = types.InlineKeyboardButton(text='Компьютеры', callback_data='Компьютеры')
#     kb_smart_home = types.InlineKeyboardButton(text='Умный дом', callback_data='Умный дом')
#     kb_modems = types.InlineKeyboardButton(text='Модемы и роутеры', callback_data='Модемы и роутеры')
#     img = open('11.png', 'rb')
#     kb.add(kb_smartphones, kb_gadjets, kb_acces, kb_comp, kb_smart_home, kb_modems)
#     bot.send_photo(message.chat.id, img)
#     bot.send_message(message.chat.id, f'Привет {message.from_user.first_name} Выбери категорию товаров!', reply_markup=kb)
#
#
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     if call.data == 'Смартфоны':
#         kb_smartphones = types.InlineKeyboardMarkup()
#         kb_Xiaomi = types.InlineKeyboardButton(text='Xiaomi', callback_data='x1')
#         kb_Apple = types.InlineKeyboardButton(text='Apple', callback_data='x2')
#         kb_Samsung = types.InlineKeyboardButton(text='Samsung', callback_data='x3')
#         kb_Huawei = types.InlineKeyboardButton(text='Huawei', callback_data='x4')
#         kb_POCO = types.InlineKeyboardButton(text='POCO', callback_data='x5')
#         kb_Realme = types.InlineKeyboardButton(text='Realme', callback_data='x6')
#         kb_TCL = types.InlineKeyboardButton(text='TCL', callback_data='x7')
#         kb_Honor = types.InlineKeyboardButton(text='HONOR', callback_data='x8')
#         img = open('11.png', 'rb')
#         kb_smartphones.add(kb_Xiaomi, kb_Apple, kb_Samsung, kb_Huawei, kb_POCO, kb_Realme, kb_TCL, kb_Honor)
#         bot.send_photo(call.message.chat.id, img)
#         bot.send_message(call.message.chat.id, text=f'{call.from_user.first_name} Выберите тип из категории и получите файл!', reply_markup=kb_smartphones)
#
#     elif call.data == 'x1':
#         with open('xiaomi_phones.csv', 'r') as file:
#             bot.send_message(call.message.chat.id, text='собираю информацию, пожалуйста подождите')
#             bot.send_document(call.message.chat.id, file)
#     elif call.data == 'x2':
#         with open('apple_phones.csv') as file:
#             bot.send_document(call.message.chat.id, file)
#     elif call.data == 'x3':
#         with open('samsung_phones.csv') as file:
#             bot.send_document(call.message.chat.id, file)
#     elif call.data == 'x4':
#         with open('huawei_phones.csv') as file:
#             bot.send_document(call.message.chat.id, file)
#     elif call.data == 'x5':
#         with open('poco.csv') as file:
#             bot.send_document(call.message.chat.id, file)
#     elif call.data == 'x6':
#         with open('realme.csv') as file:
#             bot.send_document(call.message.chat.id, file)
#     elif call.data == 'x7':
#         with open('tcl.csv') as file:
#             bot.send_document(call.message.chat.id, file)
#     elif call.data == 'x8':
#         with open('honor.csv') as file:
#             bot.send_document(call.message.chat.id, file)
#
#     elif call.data == 'Гаджеты':
#         kb_gadj = types.InlineKeyboardMarkup()
#         kb_sm_watch = types.InlineKeyboardButton(text='Умные часы', callback_data='x11')
#         kb_headphones = types.InlineKeyboardButton(text='Наушники', callback_data='x21')
#         kb_fitness = types.InlineKeyboardButton(text='Фитнес браслеты', callback_data='x31')
#         kb_bluetooth = types.InlineKeyboardButton(text='Bluetooth колонки', callback_data='x41')
#         kb_children_watch = types.InlineKeyboardButton(text='Детские умные часы', callback_data='x51')
#         img = open('11.png', 'rb')
#         kb_gadj.add(kb_sm_watch, kb_headphones, kb_fitness, kb_bluetooth, kb_children_watch)
#         bot.send_photo(call.message.chat.id, img)
#         bot.send_message(call.message.chat.id, text=f'{call.from_user.first_name} Выберите тип из категории и получите файл!', reply_markup=kb_gadj)
#
#     elif call.data == 'Аксессуары':
#         kb_acsess = types.InlineKeyboardMarkup()
#         kb_zas = types.InlineKeyboardButton(text='Защита', callback_data='x211')
#         kb_pit = types.InlineKeyboardButton(text='Питание', callback_data='x221')
#         kb_audio = types.InlineKeyboardButton(text='Аудио', callback_data='x231')
#         kb_mem = types.InlineKeyboardButton(text='Память', callback_data='x241')
#         kb_ant = types.InlineKeyboardButton(text='Антенны', callback_data='x251')
#         img = open('11.png', 'rb')
#         kb_acsess.add(kb_zas, kb_pit, kb_audio, kb_mem, kb_ant)
#         bot.send_photo(call.message.chat.id, img)
#         bot.send_message(call.message.chat.id, text=f'{call.from_user.first_name} Выберите тип из категории и получите файл!', reply_markup=kb_acsess)
#
#     elif call.data == 'Компьютеры':
#         kb_comp = types.InlineKeyboardMarkup()
#         kb_plan = types.InlineKeyboardButton(text='Планшеты', callback_data='x311')
#         kb_nout = types.InlineKeyboardButton(text='Ноутбуки', callback_data='x321')
#         kb_tv_pr = types.InlineKeyboardButton(text='ТВ приставки', callback_data='x331')
#         kb_tv = types.InlineKeyboardButton(text='Телевизоры', callback_data='x341')
#         img = open('11.png', 'rb')
#         kb_comp.add(kb_plan, kb_nout, kb_tv_pr, kb_tv)
#         bot.send_photo(call.message.chat.id, img)
#         bot.send_message(call.message.chat.id, text=f'{call.from_user.first_name} Выберите тип из категории и получите файл!', reply_markup=kb_comp)
#
#     elif call.data == 'Умный дом':
#         kb_home = types.InlineKeyboardMarkup()
#         kb_tech = types.InlineKeyboardButton(text='Умная техника', callback_data='x411')
#         kb_dat = types.InlineKeyboardButton(text='Датчики и свет', callback_data='x421')
#         kb_kol = types.InlineKeyboardButton(text='Колонки', callback_data='x431')
#         img = open('11.png', 'rb')
#         kb_home.add(kb_tech, kb_dat, kb_kol)
#         bot.send_photo(call.message.chat.id, img)
#         bot.send_message(call.message.chat.id, text=f'{call.from_user.first_name} Выберите тип из категории и получите файл!', reply_markup=kb_home)
#
#     elif call.data == 'Модемы и роутеры':
#         kb_mod = types.InlineKeyboardMarkup()
#         kb_mr = types.InlineKeyboardButton(text='Модемы и роутеры', callback_data='x511')
#         img = open('11.png', 'rb')
#         kb_mod.add(kb_mr)
#         bot.send_photo(call.message.chat.id, img)
#         bot.send_message(call.message.chat.id, text=f'{call.from_user.first_name} Выберите тип из категории и получите файл!', reply_markup=kb_mod)
#
#
#
#
# bot.polling(none_stop=True)
