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


def choose_product_count(amount = 1, plus_or_minus =''):
    kb = types.InlineKeyboardMarkup(row_width=3)

    back = types.InlineKeyboardButton(text='Back', callback_data='back')
    plus = types.InlineKeyboardButton(text='+', callback_data='increment')
    minus = types.InlineKeyboardButton(text='-', callback_data='decrement')
    count = types.InlineKeyboardButton(text=str(amount), callback_data=str(amount))
    add_to_cart = types.InlineKeyboardButton(text='Add to Cart', callback_data='to_cart')

    #callback_data plus or minus

    if plus_or_minus == 'increment':
        new_amount = int(amount) + 1
        count = types.InlineKeyboardButton(text=str(new_amount), callback_data=str(new_amount))
    elif plus_or_minus == 'decrement':
        if amount > 1:
            new_amount = int(amount) - 1
            count = types.InlineKeyboardButton(text=str(new_amount), callback_data=str(new_amount))
    kb.add(minus, count, plus)
    kb.row(back, add_to_cart)

    return kb

def cart_buttons():
    kb = types.InlineKeyboardMarkup(row_width=3)

    order = types.InlineKeyboardButton(text='Make Order', callback_data='order')
    clear = types.InlineKeyboardButton(text='Clar', callback_data='clear')
    back = types.InlineKeyboardButton(text='Back', callback_data='back')

    kb.add(clear,order,back)

    return kb




