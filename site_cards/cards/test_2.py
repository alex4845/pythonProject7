
import telebot
from telebot import types
import sqlite3
def telegramm_base():
    conn = sqlite3.connect('telegramm_table.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS list_1
           (number INTEGER PRIMARY KEY, name TEXT (30), sur_name TEXT (30), education TEXT (100),
           adress TEXT (50), age INTEGER (3))""")
    cursor.execute('INSERT INTO list_1 (name, sur_name, education, adress, age) VALUES (?,?,?,?,?)',
                   (name, surname, education, adress, age))
    conn.commit()



bot = telebot.TeleBot('5917858144:AAHRyeAdLmAfuDsuZAAv5jUXs4U9cG3sa34')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет! Если ты хочешь участвовать в Open Call"
                                               " в Художественном Комбинате, то тебе необходимо зарегистрироваться."
                                               " Отправь 'да', если хочешь начать процесс регистрации")
    elif message.text == "да" or message.text == "Да":
        bot.send_message(message.from_user.id, "Как ваше имя?")
        bot.register_next_step_handler(message, get_name)
    elif message.text == "Список" or message.text == "список":
        bot.send_message(message.from_user.id, "Зарегистрированы на данный момент:")
        conn = sqlite3.connect('telegramm_table.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM list_1")
        res = cursor.fetchall()
        for i in res:
            a = str(i)
            bot.send_message(message.from_user.id, a[1:-1])
    else:
        bot.send_message(message.from_user.id, "Ну пока...")

def get_name(message):
    global name
    name = str(message.text)
    bot.send_message(message.from_user.id, f"Ваша фамилия, {message.text}?")
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    global surname
    surname = str(message.text)
    bot.send_message(message.from_user.id, "Хорошо. Какое у вас образование (укажите учебное заведение)?")
    bot.register_next_step_handler(message, get_education)

def get_education(message):
    global education
    education = str(message.text)
    bot.send_message(message.from_user.id, "Ок. Ваш адрес?")
    bot.register_next_step_handler(message, get_adress)

def get_adress(message):
    global adress
    adress = str(message.text)
    bot.send_message(message.from_user.id, "Сколько вам лет?")
    bot.register_next_step_handler(message, get_age)

def get_age(message):
    global age
    age = str(message.text)
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = f'Вам {age} лет, вас зовут {name} {surname} и ваш адрес {adress}?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Вы записаны. Мы вас известим дополнительно. Спасибо')
        telegramm_base()

    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Что-то не так? Пишите "да" и повторите регистрацию')

bot.polling(none_stop=True, interval=0)
