import telebot, database, buttons
from geopy import Nominatim

#connection to the bot
token = '1652159514:AAHGAXOo4woxDDdsW3lT6Cf4JSPVACv-XOo'
bot = telebot.TeleBot(token)
geolocator = Nominatim(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')

@bot.message_handler(commands=['start'])
def start_message(message):
    global user_id
    user_id = message.from_user.id
    check_user = database.if_user_exist(user_id)
    if check_user:
        products = database.get_pr_name_id()
        bot.send_message(user_id, 'Welcome', reply_markup=buttons.remove())
        bot.send_message(user_id,'Select menu', reply_markup=buttons.main_menu_buttons(products))
    else:
        bot.send_message(user_id, 'Welcome, we need to register you, Enter your name', reply_markup=buttons.remove())
        #waiting for the data
        bot.register_next_step_handler(message, get_name)

def get_name(message):
    user_name = message.text
    bot.send_message(user_id, 'Enter your number', reply_markup=buttons.num_button())

    bot.register_next_step_handler(message, get_num, user_name)

def get_num(message, user_name):
    if message.contact:
        user_num = message.contact.phone_number
        bot.send_message(user_id, 'Send your location', reply_markup=buttons.location_button())

        bot.register_next_step_handler(message, get_location, user_name, user_num)
    else:
        bot.send_message(user_id, 'Send your contact via button')
        bot.register_next_step_handler(message, get_num, user_name)

def get_location(message, user_name, user_num):
    if message.location:
        user_loc = geolocator.reverse(f'{message.location.longitude},{message.location.latitude}')
        database.register(user_id, user_name, user_num, user_loc)
        bot.send_message(user_id, 'Registered successfully')
        products = database.get_pr_id()
        bot.send_message(user_id, 'Select menu', reply_markup=buttons.main_menu_buttons(products))
    else:
        bot.send_message(user_id, 'Send location via button')
        bot.register_next_step_handler(message, get_location, user_name, user_num)


bot.polling(none_stop=True)
