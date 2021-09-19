#import
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from settings import TOKEN
import logging

logging .basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                     level=logging.INFO,
                     filename='bot.log')

def sms(bot, update):
    print('')
    bot.message.reply_text('Пропустил звонки📱 пропустил сообщения😢 '
                           '\nперезвоню🚫 отдыхаю🏄‍♂ нету времени🕖'.format(bot.message.chat.first_name)) # отправляем ответ

def snd(bot, update):
    bot.sendDocument(chat_id, data, {fileName: 'file.pdf'});

#parrot() Отвечает темже сообщением которое ему прислали
def parrot(bot, update):
    print(bot.message.text) # печатаем на экран сообщение пользователя
    bot.message.reply_text(bot.message.text) # отправляем обратно текст пользователя


def main():
    my_bot = Updater(TOKEN)
    my_bot.dispatcher.add_handler(CommandHandler('start', sms))
    logging.info('Start bot')
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot)) # обработчик текстового сообщения

    my_bot.start_polling()
    my_bot.idle()



main()