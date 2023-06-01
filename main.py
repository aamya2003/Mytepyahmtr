import telebot

bot = telebot.TeleBot("5494825038:AAE-K27Fj3ki7JDVyj8_2EF4gjCoyrcYiKo")


@bot.message_handler()
def SayHello(message):
    bot.send_message(message.chat.id, "Hello")


bot.infinity_polling(skip_pending=True)
