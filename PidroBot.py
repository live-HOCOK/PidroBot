import telebot
from src import constants
from src.commands import pidro, stats, answer_all_mentions
from src.database import Database


bot = telebot.TeleBot(constants.TOKEN)
db = Database()


@bot.message_handler(commands=['pidro'])
def command_pidro(message):
    answer = pidro(message, db)
    bot.send_message(message.chat.id, answer)


@bot.message_handler(commands=['stats'])
def command_stats(message):
    answer = stats(message, db)
    bot.send_message(message.chat.id, answer)


@bot.message_handler(content_types=['text'])
def read_all_message(message):
    answer = answer_all_mentions(message, db)
    if answer:
        bot.send_message(message.chat.id, answer)


print('Bot is started')
bot.polling()
