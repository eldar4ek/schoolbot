import requests
import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = '6275139911:AAGVsCGEnbSp7UjTSebGYOy9Qe2U5ZwFooA'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Понедельник")
    button2 = types.KeyboardButton("Вторник")
    button3 = types.KeyboardButton("Среда")
    button4 = types.KeyboardButton("Четверг")
    button5 = types.KeyboardButton("Пятница")
    button6 = types.KeyboardButton("О программе и авторе")
    markup.add(button1, button2, button3, button4, button5, button6)
    bot.send_message(message.chat.id,"Привет, напиши свой день недели с заглавной буквы или нажми на кнопку, а я вышлю тебе расписание занятий!", reply_markup=markup) 

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Понедельник":
        bot.send_message(message.chat.id,['\n1. Разговор о важном.'
                                          '\n2. Биология.'
                                         '\n3. Алгебра.'
                                          '\n4. Иностранный язык.'
                                         '\n5. География.'
                                          '\n6. Физкультура.'
                                         '\n7. Второй Ин.яз.'])        
    elif message.text=="Вторник":
         bot.send_message(message.chat.id,['\n1. Технология.'
                                          '\n2. Химия.'
                                         '\n3. Русский язык.'
                                          '\n4. Исскуство.'
                                         '\n5. Литература.'
                                          '\n6. Физика.'
                                         '\n7. Алгебра.'])
    elif message.text=="Среда":
        bot.send_message(message.chat.id,['\n1. Физкультура.'
                                          '\n2. География.'
                                         '\n3. Русский язык.'
                                          '\n4. Химия.'
                                         '\n5. Литература.'
                                          '\n6. Геометрия.'
                                         '\n7. Иностранный язык.'])
    elif message.text=="Четверг":
         bot.send_message(message.chat.id,['\n1. История.'
                                          '\n2. Русский Язык.'
                                         '\n3. Физика.'
                                          '\n4. Черчение.'
                                         '\n5. Алгебра.'
                                          '\n6. Иностранный язык.'
                                         '\n7. ОБЖ.'])      
    elif message.text=="Пятница":
        bot.send_message(message.chat.id,['\n1. Обществознание.'
                                          '\n2. История.'
                                         '\n3. Биология.'
                                          '\n4. Геометрия.'
                                         '\n5. Русский язык.'
                                          '\n6. Информатика.'])
    elif message.text=="О программе и авторе":
        bot.send_message(message.chat.id,['\n1. Программа создана для того,что бы знать какие предметы будут в определенный день.'
                                           "\n2. Автор данного бота: Эльдар Билалов. Телеграмм:Eldarbilalov3."])
bot.infinity_polling()