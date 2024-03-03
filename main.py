import os
from telebot import TeleBot
import random
import time

my_secret = os.environ['TOKEN']
bot = TeleBot(my_secret)

@bot.message_handler(commands=['start'])
def on_start(message):
    bot.send_message(message.chat.id, "اهلا بك في سنه التغيير هذا بوت بشكل شهري يرسلك تحديات تخلي عامك اجمل")
    while True:
        loo = random.choice(["تحدي 1", 'تحدي2 ', " تحدي 3 "])
        bot.send_message(message.chat.id, loo)
        time.sleep(259200)  

bot.polling()
