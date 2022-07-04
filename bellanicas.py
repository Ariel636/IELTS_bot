from typing import ChainMap
import telebot
import telegram
import time
import sqlite3
from time import gmtime, strftime
from telegram import ParseMode
from telebot import types
bot = telebot.TeleBot('5312915445:AAENRrI95NMoobGAhTLniD0N4TQK3V69aKY')
@bot.message_handler(content_types=['text', 'photo'])
def uno(message):
    connect= sqlite3.connect('database.db')
    cursor= connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS UserA(
        user_id INTEGER,
        First_Name STRING,
        Last_Name STRING,
        Username STRING,
        Date INTEGER
    )""")

    connect.commit()

    user_id=message.from_user.id
    First_Name=message.from_user.first_name
    Last_Name=message.from_user.last_name
    Username=message.from_user.username
    Date=strftime( "%Y.%m.%d", gmtime() )
    cursor.execute(f"SELECT user_id FROM UserA WHERE user_id= {user_id}")
    data=cursor.fetchone()
    if data is None:
        UserA = [message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username, strftime( "%Y.%m.%d", gmtime() )]
        cursor.execute("INSERT INTO UserA VALUES(?,?,?,?,?);", UserA)
        connect.commit()
    else:
        pass

        if message.from_user.id==233473811 or message.from_user.id==908927889 or message.from_user.id==1707358502:
            try:
                if message.text.lower()== '/start' or message.text.lower()=='/restart':
                    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEmSNibfJC8FHw-adNCTSJ-ZnhzlDJiwACFAADe8B9Ezjtl9FtGtV5JAQ")
                    rusya=types.ReplyKeyboardMarkup(resize_keyboard=True)
                    rasp=types.KeyboardButton('Получить книги')
                    checkkk=types.KeyboardButton('Проверить Writing')
                    support=types.KeyboardButton('Получить поддержку')
                    socialka=types.KeyboardButton('Поблагодарить моего разработчика')
                    rusya.row(rasp)
                    rusya.row(checkkk)
                    rusya.row(socialka) 
                    rusya.row(support)
                    bot.send_message(message.chat.id, text='Привет 'f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a>\nЯ создан помогать тебе в подготовке к IELTS!", parse_mode='html', reply_markup=rusya)
                    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEmSVibfNdrDwmfDHo8z2nZuPMFu-XDQACQgIAAnvAfRMvCaa3aK6FnyQE")
                elif message.text.lower()=='поблагодарить моего разработчика':
                    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEmU1ibgnVcQenGcxw36HoL3BX0q1vUwACQgIAAnvAfRMvCaa3aK6FnyQE")
                    bot.send_message(message.chat.id, text=f"<a href='https://t.me/Original_Ariel'>Думаю ему будет гораздо приятнее, если вы напишете ему в лс:)</a>", parse_mode='html')
                    bot.send_message(908927889, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = {message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = Благодарность', parse_mode='html')
                elif message.text.lower()=='вернуться назад🔙':
                    backu=types.ReplyKeyboardMarkup(resize_keyboard=True)
                    rasp=types.KeyboardButton('Получить книги')
                    checkk=types.KeyboardButton('Проверить Writing')
                    support=types.KeyboardButton('Получить поддержку')
                    socialka=types.KeyboardButton('Поблагодарить моего разработчика')
                    backu.row(checkk)
                    backu.row(rasp)
                    backu.row(socialka) 
                    backu.row(support)
                    bot.send_message(message.chat.id, text='С возвращением в главное меню!', reply_markup=backu)
                    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEmUVibgSlUATYc4hwHdaRe5wzhgTzPQACSgEAAnvAfRNGfk6AseBabiQE")
                elif message.text.lower()=='получить поддержку':
                    bot.send_message(908927889, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = {message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = поддержку вызвала', parse_mode='html')
                    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEmUlibgbLvYmtb_Xk6MB957dK0gisawACMAADe8B9E-gE9BzCedyGJAQ")
                    bot.send_message(message.chat.id, text='''Если вы нажали на эту кнопку, думаю вам сейчас нелегко, или просто очень скучно.
                    \nТем не менее, я желаю вам терпения и прошу знать следующее:\n
                    \nВы уже должны были привыкнуть к трудностям, как никак вам удалось стать лучшим куратором за всю историю лицея, что аж из-за вас в этом году вообще никому эту номинацию не дали.
                    \nДля подростков, IELTS является чем то вроде самого важного экзамена десятилетия. Но с вашим опытом, этот экзамен можно рассмотреть просто как подготовка у очередному уроку с 2ТН3-невыносимо, но, когда закончите, станет легче.
                    \nА щас вставайте епт и учитесь, харэ жалеть себя.''')
                    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEmUdibga-PD-TYRKTVAtZjC0ah8B98gACGQADe8B9E4fn-su6s6Q4JAQ")
                elif message.text.lower()=='/get' or message.text.lower()=='получить книги':
                    books=types.ReplyKeyboardMarkup(resize_keyboard=True)
                    back=types.KeyboardButton('Вернуться назад🔙')
                    bank=types.KeyboardButton('IELTS Knowledge Bank🔐')
                    vocab=types.KeyboardButton('IELTS Vocabulary🧠')
                    practise=types.KeyboardButton('IELTS Practice Tests🥵')
                    reading=types.KeyboardButton('IELTS Reading Section📖')
                    writing=types.KeyboardButton('IELTS Writing Section🪶')
                    speaking=types.KeyboardButton('IELTS Speaking Section🙊')
                    books.row(back)
                    books.row(bank)
                    books.row(vocab)
                    books.row(practise)
                    books.row(reading)
                    books.row(writing)
                    books.row(speaking)
                    bot.send_message(message.chat.id, text='Выбирай',reply_markup=books) 
                elif message.text=='IELTS Knowledge Bank🔐': 
                    bot.send_message(908927889, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = {message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = книжку ищет', parse_mode='html')
                    bot.send_message(message.chat.id, text=f"Материалы для полного ознакомления с IELTS:\n1. <a href='https://yadi.sk/i/duVxjAD5Y20aHQ'>The Official Cambridge Guide to IELTS</a>\n+ <a href='https://drive.google.com/drive/folders/1ZQMcFvo9uCftF6eitF9WKTENl6lOfDwu?usp=sharing'>Аудио файл</a>", parse_mode='html')
                
                elif message.text=='IELTS Vocabulary🧠': 
                    bot.send_message(908927889, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = {message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = книжку ищет', parse_mode='html')
                    bot.send_message(message.chat.id, text=f'''Материалы для прокачки словаря для IELTS:\n1. <a href='https://drive.google.com/file/d/1gHxj_3eKHPg1gJoBvsNxqYLJUvU8v-h6/view?usp=drivesdk'>Dr. Lin Lougheed Essential Words for the IELTS</a>
                    \n2. <a href='https://drive.google.com/file/d/1g_hVzJjGvjWTf4GxSNMoJYqX9_PB5w3E/view?usp=drivesdk'>Learning Academic Words in Context</a>
                    \n3. <a href='https://drive.google.com/file/d/1gbTAci-l3-bq94nJ3ZoYx3zxg0gh7q4N/view?usp=drivesdk'>IELTS Advanced Vocabulary</a>
                    \n4. <a href='https://drive.google.com/file/d/1gifI6FIazhrAbSTXGI06RoKeh5cwjEoe/view?usp=drivesdk'>IELTS Vocabulary by Collins</a>\n+ <a href='https://drive.google.com/file/d/1gdQkWiPqs7zNVK9ogBGr2vaCYn-haa0m/view?usp=drivesdk'>Аудио</a>
                    \n5. <a href='https://drive.google.com/file/d/1gijkWuQBrViQx1P7MWGl1au6V3MlgUFx/view?usp=drivesdk'>Penguin Vocabulary Advanced</a>''', parse_mode='html')
                
                elif message.text=='IELTS Practice Tests🥵': 
                    bot.send_message(908927889, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = {message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = книжку ищет', parse_mode='html')
                    bot.send_message(message.chat.id, text=f'''Практис тесты по IELTS:\n1. <a href='https://drive.google.com/file/d/1glctykribnvwuMUeqND5jzLyo5KisViv/view?usp=drivesdk'>Kaplan IELTS Premier with 8 PT</a>
                    \n2. <a href='https://drive.google.com/file/d/1gq0F0x8FWlzfXD2XDk_uXgtIGxqvfgKO/view?usp=drivesdk'>Barron's IELTS Practise Exams</a>\n
                    \n3. <a href='https://drive.google.com/file/d/1gt044SoLH-N3beWRXfxZC_11iKf7LS9U/view?usp=drivesdk'>Cambridge IELTS 4</a>\n+ <a href='https://drive.google.com/file/d/1gz1nAqXydhe22OJhttcRfJ8v6rsdeBiu/view?usp=drivesdk'>Аудио</a>
                    \n4. <a href='https://drive.google.com/file/d/1h8fmTqZUty-OScAirdNf-8Lbv7aOf2Kr/view?usp=drivesdk'>Cambridge IELTS 5</a>
                    \n5. <a href='https://drive.google.com/file/d/1hCqgx3f3UIMFXae5VCOZaM_0KYkRDQk3/view?usp=drivesdk'>Cambridge IELTS 6</a>\n+ <a href='https://drive.google.com/file/d/1hFVRU8lqzqAKO4YOE-PrjJxnaPW5-13-/view?usp=drivesdk'>Аудио</a>
                    \n6. <a href='https://drive.google.com/file/d/1hOlRxu2XRS2LQzwyQAupg63VdOu2Wag6/view?usp=drivesdk'>Cambridge IELTS 8</a>\n+ <a href='https://drive.google.com/file/d/1hOQ8brm-DxogJhc308xyzZBw4CCvD796/view?usp=drivesdk'>Аудио</a>
                    \n7. <a href='https://drive.google.com/file/d/1iCGTZgjVE83PSqngph55T2H2V7m5ZpOu/view?usp=drivesdk'>Cambridge IELTS 10</a>\n+ <a href='https://drive.google.com/file/d/1i6YimrFFDhPKHgcFH9VXhIK5KCTxqZIP/view?usp=drivesdk'>Аудио</a>
                    \n8. <a href='https://drive.google.com/file/d/1iIhXPd7GXb2NzSb5irJcnlhKKOR72HRy/view?usp=drivesdk'>Cambridge IELTS 11</a>\n+ <a href='https://drive.google.com/file/d/1iNwfwjgYxttCzVoFVf6BG4kHH4JrYsw7/view?usp=drivesdk'>Аудио</a>
                    \n9. <a href='https://drive.google.com/file/d/1iPXYPpb9o7DiCSF5nDQCj6kfp_6dL4Bv/view?usp=drivesdk'>Cambridge IELTS 12</a>\n+ <a href='https://drive.google.com/file/d/1iUtPTGpPEXDADYq3HE41hiQwYBKnK4Kl/view?usp=drivesdk'>Аудио</a>
                    \n10. <a href='https://drive.google.com/file/d/1iXe7oOWo8vd199Dja-uUYG8QaVKuK0SR/view?usp=drivesdk'>Cambridge IELTS 13</a>\n+ <a href='https://drive.google.com/file/d/1iXqBjfcj9mZ_o_tNtTbfVH1VxlcvIENb/view?usp=drivesdk'>Аудио</a>
                    \n11. <a href='https://drive.google.com/file/d/1idl_w4swOOVWGigT8GO15yFS15fOIU-B/view?usp=drivesdk'>Cambridge IELTS 14</a>\n+ <a href='https://drive.google.com/file/d/1j-CKzR_MrbC7o13kNlz7jYmVJxVLTwhA/view?usp=drivesdk'>Аудио</a>''', parse_mode='html')

                elif message.text=='IELTS Reading Section📖': 
                    bot.send_message(908927889, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = {message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = книжку ищет', parse_mode='html')
                    bot.send_message(message.chat.id, text=f"Материалы для прокачки Reading-секции IELTS:\n1. <a href='https://drive.google.com/file/d/1j13QJ_LWArkp1dPnn-R6ZNehdssz0odM/view?usp=drivesdk'>IELTS Reading Formula by Memarzadeh</a>", parse_mode='html')

                elif message.text=='IELTS Writing Section🪶': 
                    bot.send_message(908927889, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = {message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = книжку ищет', parse_mode='html')
                    bot.send_message(message.chat.id, text=f'''Материалы для прокачки Writing-секции IELTS:\n1. <a href='https://drive.google.com/file/d/1jLm2kTYtajrmDOJ5hpIKpVK3ui2FJV-_/view?usp=drivesdk'>Writing tasks and samples</a>
                    \n2. <a href='https://drive.google.com/file/d/1jHKq5YwlIcqG0M7wDsNJ5qK2b0O3pnPm/view?usp=drivesdk'>Linking Words</a>
                    \n3. <a href='https://drive.google.com/file/d/1jGdqroHXA873S-ex-QM-tS2hwjxeQW40/view?usp=drivesdk'>How to write at a band 9 level by Ryan Higgins</a>
                    \n4. <a href='https://drive.google.com/file/d/1jC9uf6El_GvZL_aqmdCJeKLyuEPIV1Ck/view?usp=drivesdk'>Practical IELTS Writing Strategies</a>
                    \n5. <a href='https://drive.google.com/file/d/1jFMsv8zboXPwg4FXwQplOfq-uDHANOhZ/view?usp=drivesdk'>IELTS Academic Writing Task 1</a>
                    \n6. <a href='https://drive.google.com/file/d/1jRP2-R1U4ibVC-B3hLnrEHDnHnQcVD4P/view?usp=drivesdk'>IELTS Academic Writing Task 2</a>
                    \n7. <a href='https://drive.google.com/file/d/1jSk7c6kEPHMLpXdNZ-XJUqDSlYTIh6cD/view?usp=drivesdk'>169 IELTS Essay Samples</a>
                    \n8. <a href='https://drive.google.com/file/d/1j38ZzyhXJXl6DCI7Gp8xDvN9amFJe2rD/view?usp=drivesdk'>32 IELTS Essay Samples Band 9</a>''', parse_mode='html')

                elif message.text=='IELTS Speaking Section🙊': 
                    bot.send_message(908927889, f'ID: {message.from_user.id} \nFirst name = {message.from_user.first_name} \nLast name = {message.from_user.last_name}\nUsername = {message.from_user.username}\nTime = {strftime( "%Y.%m.%d", gmtime() )}\nHour = {strftime( "%H:%M:%S", gmtime() )} \nMessage = книжку ищет', parse_mode='html')
                    bot.send_message(message.chat.id, text=f'''Материалы для прокачки Speaking-секции IELTS:\n1. <a href='https://drive.google.com/file/d/1jeUldUKU2RFl5PBqhSxuJgOtc1WIWVoP/view?usp=drivesdk'>IELTS Speaking Topics</a>
                    \n2. <a href='https://drive.google.com/file/d/1jLm2kTYtajrmDOJ5hpIKpVK3ui2FJV-_/view?usp=drivesdk'>IELTS Vocabulary by Topic</a>
                    \n3. <a href='https://drive.google.com/file/d/1jdz2gIuGwCRSLiqEIrHC31-fsJ0Kj7Tk/view?usp=drivesdk'>Collins Speaking for IELTS</a>''', parse_mode='html')
                elif message.text.lower()=='/check' or message.text=='Проверить Writing':
                    bot.send_message(message.chat.id, text='''https://ielts69.com/check-ielts-writing-evaluation-and-correction-service\n
http://ieltscdt.com/ielts-writing-essay-evaluation.php\n
http://www.ieltscdt.com/check-ielts-essay.php''')
                elif message.text==message.text:
                    bot.send_message(1412330377, text=message.text)
            except:
                bot.send_message(908927889, text='Че то пошло не по плану')
        elif message.from_user.id==1412330377:
            try:
                bot.send_message(233473811, text=message.text)
                bot.send_message(1707358502, text=message.text)
                bot.send_message(message.chat.id, text='Sent!')
            except:
                bot.send_message(908927889, text='Че то пошло не по плану')
        else:
            bot.send_message(message.chat.id, text='Бот не для вас был создан. Прошу не тратить время мое и ваше.\nЕсли хотите получить доступ к боту-пишите разрабу.')



bot.polling(none_stop=True, interval=0)