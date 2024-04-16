import telebot 

bot = telebot.TeleBot('6562327431:AAHpfqV5Pr5pDQrxbbnTf72Bb7mgIzQz1kM')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name} {message.from_user.last_name}')
    
bot.polling(none_stop=True)
    
