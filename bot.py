from telebot import TeleBot
from logic import *
from config import *
import random

bot = TeleBot(API_TOKEN)

manager = DB_Manager(DATABASE)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, """Привет! Это бот который проверяет твои знания автомобилей!  
Ответы должны быть в формате: "ВАЗ-2101". 
В Викторине используются автомобили "ВАЗ", "АЗЛК", "ИЖ", "ГАЗ"
""")

@bot.message_handler(commands=['go'])
def get_image(message):
    car_id = random.randint(1,31)
    img = manager.get_car_img(car_id)
    with open(f'images/{img}', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, "Введите название автомобиля")
        bot.register_next_step_handler(message, get_name, car_id=car_id)

def get_name(message, car_id):
    name = message.text
    car_name = manager.get_car_name(car_id)
    if car_name == name:
        bot.send_message(message.chat.id, "Правильно")
    else:
        bot.send_message(message.chat.id, "Вы не угадали")

if __name__ == '__main__':
    manager = DB_Manager(DATABASE)
    bot.infinity_polling()