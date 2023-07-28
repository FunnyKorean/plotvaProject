from telebot import types

def num_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    num = types.KeyboardButton('Send your number', request_contact=True)
    kb.add(num)
    return kb

def location_button():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    loc = types.KeyboardButton('Send your location', request_location=True)
    kb.add(loc)
    return kb

def main_menu_buttons(products_from_db):
    kb = types.InlineKeyboardMarkup(row_width=3)
    #cart
    cart = types.InlineKeyboardButton(text='Cart', callback_data='cart')
    all_products = [types.InlineKeyboardButton(text=f'{i[1]}', callback_data=f'{i[0]}') for i in products_from_db]
    kb.row(cart)
    kb.add(*all_products)

    return kb


def remove():
    types.ReplyKeyboardRemove()



