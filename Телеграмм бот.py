#Использую библиотеку telegrammbot
import telebot
Token = ("5927748938:AAHD_TQuzioNi_YdmduMJKkLtLT9Jx2qwPM")
#Присваиваю переменной bot значение токена
bot = telebot.TeleBot(Token)
#Реакция на команду "start"
@bot.message_handler(commands=["start"])
def welcome(message):
#Отправляю стикер и потом сообщение
    sti=open('static/welcome.webp', "rb")
    bot.send_sticker(message.chat.id,sti) 
    bot.send_message(message.chat.id, (тут текст) .format(message.from_user, bot.get_me()),
    parse_mode="html")
@bot.message_handler(content_types=["text"])
def ancaramessi(message):
    bot.send_message(message.chat.id, message.text)


#Бесконечная работа бота
bot.polling(non_stop=True)