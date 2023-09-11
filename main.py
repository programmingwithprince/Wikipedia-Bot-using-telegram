import wikipedia
import telebot

TOKEN = "BOT TOKEN HERE"
wikipedia.set_lang("en")
bot = telebot.TeleBot(TOKEN, parse_mode=None) 
@bot.message_handler(commands=['start', 'help'])

def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	try:
	    print(message.text)
	    #raw = wikipedia.search(message.text)
#	    print(raw)
	    result = wikipedia.summary(message.text, sentences = 5)
	    bot.reply_to(message, result)           
	except Exception as e:
	    print(e)
	    bot.reply_to(message,'Unable to process your request currently! provide more details.'+str(e))
bot.infinity_polling()        