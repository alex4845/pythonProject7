import datetime

import telebot
from telebot import types
import sqlite3

from datetime import date
bot = telebot.TeleBot('5921930950:AAFDGklrmWGIyrQyzywlcZKCQ2jV5DVolmw')

def write_credit(credit, dat):
    conn = sqlite3.connect('MAX_bot_table.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS list_1
               (number INTEGER PRIMARY KEY, credit INTEGER (10), date TEXT (20))""")
    cursor.execute('INSERT INTO list_1 (credit, date) VALUES (?,?)',
                   (credit, dat))
    conn.commit()
    cursor.execute("SELECT * FROM list_1")
    res = cursor.fetchall()
    print("База расход")
    for i in res:
        print(i)

def write_debet(debet, dat):
    conn = sqlite3.connect('MAX_bot_table.db')
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS list_2
               (number INTEGER PRIMARY KEY, debet INTEGER (10), date TEXT (20))""")
    cursor.execute('INSERT INTO list_2 (debet, date) VALUES (?,?)',
                   (debet, dat))
    conn.commit()
    cursor.execute("SELECT * FROM list_2")
    res = cursor.fetchall()
    print("База доход")
    for i in res:
        print(i)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    a = str(message.text)
    st, s, stt = "Р", "", "П"
    dat = str(date.today())
    if st in a:
        for el in a[a.index(st):]:
            if el.isdigit():
                s = s + el
            elif el == " " or el == "Р": continue
            else: break
        credit = int(s)
        write_credit(credit, dat)
    elif stt in a:
        for el in a[a.index(stt):]:
            if el.isdigit():
                s = s + el
            elif el == " " or el == "П": continue
            else: break
        debet = int(s)
        write_debet(debet, dat)
    elif a == "Итого" or a == "итого":
        bot.send_message(message.from_user.id, "С какой даты? (год-мес-чис)")
        bot.register_next_step_handler(message, get_date1)

def get_date1(message):
    global date1
    date1 = str(message.text)
    bot.send_message(message.from_user.id, "По какую дату? (год-мес-чис)")
    bot.register_next_step_handler(message, get_date2)

def get_date2(message):
    global date2
    date2 = str(message.text)
    conn = sqlite3.connect('MAX_bot_table.db')
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(credit) FROM list_1 WHERE date>=? AND date<=?", [(date1), (date2)])
    res = str(cursor.fetchall())
    bot.send_message(message.from_user.id, f'Всего расход:  {res[2:-3]} руб')
    cursor.execute("SELECT SUM(debet) FROM list_2 WHERE date>=? AND date<=?", [(date1), (date2)])
    res1 = str(cursor.fetchall())
    bot.send_message(message.from_user.id, f'Всего доход:  {res1[2:-3]} руб')

bot.polling(none_stop=True, interval=0)